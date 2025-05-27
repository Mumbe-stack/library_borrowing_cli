from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, Member, Book, BorrowRecord

engine = create_engine('sqlite:///lib/db/app.db')
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

members = [
    Member(name="Alice Johnson", email="alice@example.com"),
    Member(name="Bob Smith", email="bob@example.com")
]

books = [
    Book(title="1984", author="George Orwell", available_copies=3),
    Book(title="The Great Gatsby", author="F. Scott Fitzgerald", available_copies=2)
]

session.add_all(members + books)
session.commit()