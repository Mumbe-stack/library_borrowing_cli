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
    Member(name="Victoria Bernice", email="victoria@gmail.com"),
    Member(name="Tori Byrant", email="torib@gmail.com")
]

books = [
    Book(title="1984", author="George Orwell", available_copies=3),
    Book(title="The Great Gatsby", author="F. Scott Fitzgerald", available_copies=2),
    Book(title="To Kill a Mockingbird", author="Harper Lee", available_copies=4),
    Book(title="Brave New World", author="Aldous Huxley", available_copies=3),
    Book(title="Pride and Prejudice", author="Jane Austen", available_copies=5),
    Book(title="The Catcher in the Rye", author="J.D. Salinger", available_copies=2),
    Book(title="The Hobbit", author="J.R.R. Tolkien", available_copies=4),
    Book(title="Fahrenheit 451", author="Ray Bradbury", available_copies=3),
    Book(title="Moby Dick", author="Herman Melville", available_copies=2),
    Book(title="Jane Eyre", author="Charlotte Brontë", available_copies=3),
    Book(title="The Lord of the Rings", author="J.R.R. Tolkien", available_copies=5),
    Book(title="Animal Farm", author="George Orwell", available_copies=4),
    Book(title="Wuthering Heights", author="Emily Brontë", available_copies=2),
    Book(title="Crime and Punishment", author="Fyodor Dostoevsky", available_copies=3),
    Book(title="The Odyssey", author="Homer", available_copies=2),
    Book(title="The Brothers Karamazov", author="Fyodor Dostoevsky", available_copies=2),
    Book(title="Les Misérables", author="Victor Hugo", available_copies=3),
    Book(title="Don Quixote", author="Miguel de Cervantes", available_copies=2),
    Book(title="Frankenstein", author="Mary Shelley", available_copies=3),
    Book(title="Dracula", author="Bram Stoker", available_copies=2)
]


session.add_all(members + books)
session.commit()