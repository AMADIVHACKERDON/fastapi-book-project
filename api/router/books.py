from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db.sessions import get_db  # This function provides the DB session
from models.book import Book  # The Book model to query the database

# Create a router for handling book-related routes
router = APIRouter()

# Define the GET endpoint to fetch a book by its ID
@router.get("/api/v1/books/{book_id}")
def get_book(book_id: int, db: Session = Depends(get_db)):
    # Query the database to find the book by its ID
    book = db.query(Book).filter(Book.id == book_id).first()
    
    # If the book doesn't exist, raise a 404 error
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Return the book details if found
    return book
