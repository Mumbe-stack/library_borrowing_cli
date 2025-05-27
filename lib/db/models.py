from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Member(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    borrow_records = relationship("BorrowRecord", back_populates="member")

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    available_copies = Column(Integer)

    borrow_records = relationship("BorrowRecord", back_populates="book")

class BorrowRecord(Base):
    __tablename__ = 'borrow_records'

    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey('members.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    borrow_date = Column(Date)
    return_date = Column(Date, nullable=True)

    member = relationship("Member", back_populates="borrow_records")
    book = relationship("Book", back_populates="borrow_records")