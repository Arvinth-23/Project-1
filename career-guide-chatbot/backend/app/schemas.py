from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime

# ... (existing schemas) ...

class UserBase(BaseModel):
    name: str
    email: str
    college: Optional[str] = None
    major: Optional[str] = None
    graduation_year: Optional[int] = None
    preferences: Optional[Dict[str, Any]] = {}

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    college: Optional[str] = None
    major: Optional[str] = None
    graduation_year: Optional[int] = None
    preferences: Optional[Dict[str, Any]] = None

class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class UserPreferences(BaseModel):
    preferences: Dict[str, Any]
class MessageCreate(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    user_id: int
    message: str
    session_id: Optional[int] = None

class ChatResponse(BaseModel):
    session_id: int
    reply: str
    timestamp: datetime