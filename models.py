from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, column
from sqlalchemy.orm import relationship

from database import Base

class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)

class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))
    question = relationship("Question", backref="answers")

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = column(String, unique=True, nullable=False)
