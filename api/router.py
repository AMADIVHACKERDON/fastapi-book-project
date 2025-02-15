from fastapi import APIRouter

from api.routes.book_routes import router as books_router  # Correct import


api_router = APIRouter()
api_router.include_router(books_router, prefix="/books", tags=["books"])
