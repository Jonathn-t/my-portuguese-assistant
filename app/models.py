# app/models.py

from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Lesson(Base):
    __tablename__ = 'lessons'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
