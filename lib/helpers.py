from datetime import date

def format_book(book):
    return f"{book.id}. {book.title} by {book.author} (Available: {book.available_copies})"

def format_member(member):
    return f"{member.id}. {member.name} ({member.email})"