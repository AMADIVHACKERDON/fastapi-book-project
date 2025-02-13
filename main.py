from fastapi import FastAPI
from books import app as books_app
from fastapi.middleware.cors import CORSMiddleware
from api.routes import book_routes
from api.router import api_router
from core.config import settings
from api.routes.books import router as book_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(book_router, prefix="/books")


@app.get("/healthcheck")
async def health_check():
    """Checks if server is active."""
    return {"status": "active"}
