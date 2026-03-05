from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Optional
from datetime import datetime

from app.database import get_db
from app import schemas
from app import models



router = APIRouter(prefix="/users", tags=["Users"])

# -------------------- Create User --------------------
@router.post("/", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(
    user: schemas.UserCreate,
    db: AsyncSession = Depends(get_db)
):
    # Check if email already exists
    stmt = select(models.User).where(models.User.email == user.email)
    result = await db.execute(stmt)
    existing_user = result.scalar_one_or_none()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # Create new user
    db_user = models.User(
        name=user.name,
        email=user.email,
        college=user.college,
        major=user.major,
        graduation_year=user.graduation_year,
        preferences=user.preferences or {},
        created_at=datetime.utcnow()
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


# -------------------- Get User by ID --------------------
@router.get("/{user_id}", response_model=schemas.UserOut)
async def get_user(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    user = await db.get(models.User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user


# -------------------- Update User --------------------
@router.put("/{user_id}", response_model=schemas.UserOut)
async def update_user(
    user_id: int,
    user_update: schemas.UserUpdate,
    db: AsyncSession = Depends(get_db)
):
    user = await db.get(models.User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    # Update fields if provided
    update_data = user_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(user, field, value)

    await db.commit()
    await db.refresh(user)
    return user


# -------------------- Delete User --------------------
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    user = await db.get(models.User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    await db.delete(user)
    await db.commit()
    return None


# -------------------- Get User Preferences --------------------
@router.get("/{user_id}/preferences", response_model=schemas.UserPreferences)
async def get_preferences(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    user = await db.get(models.User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return schemas.UserPreferences(preferences=user.preferences)


# -------------------- Update User Preferences --------------------
@router.put("/{user_id}/preferences", response_model=schemas.UserPreferences)
async def update_preferences(
    user_id: int,
    prefs: schemas.UserPreferences,
    db: AsyncSession = Depends(get_db)
):
    user = await db.get(models.User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    user.preferences = prefs.preferences
    await db.commit()
    await db.refresh(user)
    return schemas.UserPreferences(preferences=user.preferences)


# -------------------- List All Users (Admin only?) --------------------
@router.get("/", response_model=List[schemas.UserOut])
async def list_users(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    stmt = select(models.User).offset(skip).limit(limit)
    result = await db.execute(stmt)
    users = result.scalars().all()
    return users