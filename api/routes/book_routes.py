from typing import List

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from api.db.schemas import Book, Genre, InMemoryDB

router = APIRouter()

db = InMemoryDB()
db.books = {
    1: Book(
        id=1,
        title="The Hobbit",
        author="J.R.R. Tolkien",
        publication_year=1937,
        genre=Genre.SCI_FI,
    ),
    2: Book(
        id=2,
        title="The Lord of the Rings",
        author="J.R.R. Tolkien",
        publication_year=1954,
        genre=Genre.FANTASY,
    ),
    3: Book(
        id=3,
        title="The Return of the King",
        author="J.R.R. Tolkien",
        publication_year=1955,
        genre=Genre.FANTASY,
    ),
}



@router.get("/", response_model=List[Book], status_code=status.HTTP_200_OK)
async def get_all_books():
    return list(db.books.values())  # Assuming db.books is a dictionary of books
    
@router.get("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
async def get_book(book_id: int):
    if book_id in db.books:
        return db.books[book_id]
    raise HTTPException(status_code=404, detail="Book not found")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    if book.id in db.books:
        raise HTTPException(status_code=400, detail="Book ID already exists")
    db.add_book(book)
    return book  # ✅ FastAPI will handle serialization
    

@router.put("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
async def update_book(book_id: int, book: Book) -> Book:
    try:
        return db.update_book(book_id, book)  # ✅ No need for JSONResponse
    except ValueError:
        raise HTTPException(status_code=404, detail="Book not found")
    
@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    try:
        db.delete_book(book_id)  # ✅ Use the method instead of direct deletion
        return
    except ValueError:
        raise HTTPException(status_code=404, detail="Book not found")

    return
