from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, Member, Book, BorrowRecord
from lib.helpers import format_book, format_member
from datetime import date

engine = create_engine('sqlite:///lib/db/app.db')
Session = sessionmaker(bind=engine)
session = Session()

def list_books():
    print("\nAvailable Books:")
    for book in session.query(Book).all():
        print(format_book(book))

def list_members():
    print("\nRegistered Members:")
    for member in session.query(Member).all():
        print(format_member(member))

def borrow_book():
    list_members()
    member_id = int(input("Enter Member ID: "))
    list_books()
    book_id = int(input("Enter Book ID to borrow: "))

    book = session.get(Book, book_id)
    if book.available_copies <= 0:
        print("Book not available.")
        return

    borrow = BorrowRecord(
        member_id=member_id,
        book_id=book_id,
        borrow_date=date.today()
    )
    book.available_copies -= 1
    session.add(borrow)
    session.commit()
    print("Book borrowed successfully!")
    
    member = session.get(Member, member_id)
    if member:
        session.delete(member)
        session.commit()

def return_book():
    record_id = int(input("Enter Borrow Record ID to return: "))
    record = session.get(BorrowRecord, record_id)
    if record and not record.return_date:
        record.return_date = date.today()
        book = session.get(Book, record.book_id)
        book.available_copies += 1
        session.commit()
        print("Book returned successfully!")
    else:
        print("Invalid record ID or book already returned.")

def main():
    while True:
        print("\nLibrary CLI")
        print("1. List Books")
        print("2. List Members")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            list_books()
        elif choice == '2':
            list_members()
        elif choice == '3':
            borrow_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()