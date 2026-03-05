from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    college = Column(String)
    major = Column(String)
    graduation_year = Column(Integer)
    preferences = Column(JSON, default={})   # e.g., {"interests": ["AI", "finance"]}
    created_at = Column(DateTime, default=datetime.utcnow)

class ChatSession(Base):
    __tablename__ = "chat_sessions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User")

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("chat_sessions.id"))
    role = Column(String)      # 'user' or 'assistant'
    content = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
    session = relationship("ChatSession")

class CareerPath(Base):
    __tablename__ = "career_paths"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    description = Column(Text)
    required_skills = Column(JSON)   # list of skills
    average_salary = Column(String)
    education_level = Column(String) # e.g., "Bachelor's"
    courses = relationship("Course", back_populates="career")

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    provider = Column(String)   # university, platform, etc.
    career_id = Column(Integer, ForeignKey("career_paths.id"))
    career = relationship("CareerPath", back_populates="courses")