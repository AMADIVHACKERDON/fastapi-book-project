from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import declarative_base
import enum
from api.db.sessions import Base


# Enum for the genre of books
class Genre(str, enum.Enum):
    FANTASY = "Fantasy"
    SCI_FI = "Sci-Fi"
    MYSTERY = "Mystery"
    ROMANCE = "Romance"

# Book model definition
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    publication_year = Column(Integer)
    genre = Column(Enum(Genre))

    def __repr__(self):
        return f"<Book(title={self.title}, author={self.author})>"
