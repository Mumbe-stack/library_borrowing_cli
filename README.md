# 📚 Library Book Borrowing System (CLI + ORM)
# Overview
This command-line application simulates a basic library management system. It allows users to:
    View available books
    View registered members
    Borrow books
    Return borrowed books
    It demonstrates core backend development skills using Python, SQLAlchemy ORM, and Pipenv, while following CLI and OOP best practices.

# Features
Interactive Command-Line Interface
Three models: Member, Book, and BorrowRecord
One-to-many relationships:
    Member → BorrowRecord
    Book → BorrowRecord
Uses SQLAlchemy ORM to manage the database
Automatic seeding of data
Input validation for IDs and borrowing logic
Uses Python lists and dictionaries for formatting and interaction
Virtual environment managed with Pipenv

# Project Structure
library_borrowing_cli/
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib/
    ├── cli.py
    ├── helpers.py
    ├── db/
    │   ├── models.py
    │   ├── seed.py
    │   ├── app.db
    │   └── __init__.py
    └── __init__.py

# Setup Instructions
Clone the repo
    git clone https://github.com/Mumbe-stack/library_borrowing_cli
cd library_borrowing_cli
Install dependencies
    pipenv install
    Seed the database
pipenv run python -m lib.db.seed
Run the application
    pipenv run python -m lib.cli

# CLI Menu Options
Library CLI
1. List Books
2. List Members
3. Borrow Book
4. Return Book
5. Exit

1. List Books – Shows all books and their availability
2. List Members – Displays all members
3. Borrow Book – Prompts for Member and Book ID
4. Return Book – Prompts for BorrowRecord ID
5. Exit – Ends the program

# Dependencies
Python 3.8+
SQLAlchemy
Pipenv

# Learning Goals
ORM design using SQLAlchemy
Managing Python environments with Pipenv
CLI design and user interaction
Data modeling with class relationships
Use of lists and dictionaries for functionality

# Author
Mercy Mumbe (https://github.com/Mumbe-stack)