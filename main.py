from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from books import app as books_app
from api.routes import book_routes  # Assuming this is where your router is defined



from api.router import api_router
from core.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(books_app, prefix="/api", tags=["books"]) 


@app.get("/healthcheck")
async def health_check():
    """Checks if server is active."""
    return {"status": "active"}
