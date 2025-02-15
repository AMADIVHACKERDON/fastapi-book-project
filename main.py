from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware


from core.config import settings
from api.routes.book_routes import router as book_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(book_router, prefix="/api/v1", tags=["books"])


@app.get("/healthcheck")
async def health_check():
    """Checks if server is active."""
    return {"status": "active"}
