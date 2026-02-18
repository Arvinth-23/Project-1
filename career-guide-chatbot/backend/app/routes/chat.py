from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app import schemas
from app.database import get_db
from app.services.llm import get_chat_response
from datetime import datetime
from app import models





router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/", response_model=schemas.ChatResponse)
async def chat(request: schemas.ChatRequest, db: AsyncSession = Depends(get_db)):
    # 1. Get or create chat session
    if request.session_id:
        session = await db.get(models.ChatSession, request.session_id)
        if not session:
            raise HTTPException(status_code=404, detail="Session not found")
    else:
        session = models.ChatSession(user_id=request.user_id)
        db.add(session)
        await db.commit()
        await db.refresh(session)

    # 2. Save user message
    user_msg = models.Message(
        session_id=session.id,
        role="user",
        content=request.message,
        timestamp=datetime.utcnow()
    )
    db.add(user_msg)
    await db.commit()

    # 3. Fetch recent conversation history (last 10 messages)
    stmt = select(models.Message).where(
        models.Message.session_id == session.id
    ).order_by(models.Message.timestamp.desc()).limit(10)
    result = await db.execute(stmt)
    history = result.scalars().all()[::-1]  # chronological order

    # 4. Build conversation context for LLM
    conversation = [{"role": m.role, "content": m.content} for m in history]

    # 5. Optionally fetch user profile for personalization
    user = await db.get(models.User, request.user_id)
    user_context = f"User is a {user.major} major at {user.college}, graduating in {user.graduation_year}." if user else ""

    # 6. Call LLM service
    assistant_reply = await get_chat_response(conversation, user_context)

    # 7. Save assistant reply
    assistant_msg = models.Message(
        session_id=session.id,
        role="assistant",
        content=assistant_reply,
        timestamp=datetime.utcnow()
    )
    db.add(assistant_msg)
    await db.commit()

    return schemas.ChatResponse(
        session_id=session.id,
        reply=assistant_reply,
        timestamp=assistant_msg.timestamp
    )