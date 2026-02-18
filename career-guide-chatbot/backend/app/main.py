from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import uuid
from app.services.llm import get_chat_response

app = FastAPI(title="Career Guide Chatbot")

# ---------------- CORS ----------------
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store conversation history in memory (in production, use database)
conversations = {}

# ---------------- REQUEST MODEL ----------------
class ChatRequest(BaseModel):
    user_id: int
    message: str
    session_id: Optional[str] = None

class Message(BaseModel):
    role: str
    content: str

# ---------------- ROUTER ----------------
chat_router = APIRouter()

@chat_router.post("/chat/")
async def chat_endpoint(data: ChatRequest):
    # create new session if not exists
    session_id = data.session_id or str(uuid.uuid4())
    
    if session_id not in conversations:
        conversations[session_id] = []
    
    # Add user message to conversation history
    conversations[session_id].append({
        "role": "user",
        "content": data.message
    })
    
    # Get response from OpenAI
    try:
        reply = await get_chat_response(conversations[session_id])
        
        # Add assistant response to conversation history
        conversations[session_id].append({
            "role": "assistant",
            "content": reply
        })
        
        return {
            "reply": reply,
            "session_id": session_id,
            "status": "success"
        }
    except Exception as e:
        return {
            "reply": f"Error processing request: {str(e)}",
            "session_id": session_id,
            "status": "error"
        }

@chat_router.get("/history/{session_id}")
async def get_history(session_id: str):
    if session_id in conversations:
        return {
            "session_id": session_id,
            "messages": conversations[session_id]
        }
    return {
        "session_id": session_id,
        "messages": [],
        "error": "Session not found"
    }

app.include_router(chat_router)

@app.get("/")
async def root():
    return {"message": "Career Guide Chatbot Backend Running"}