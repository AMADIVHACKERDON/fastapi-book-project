from fastapi.testclient import TestClient
from main import app 
from api.db.schemas import Genre

client = TestClient(app)
def test_get_all_books():
    response = client.get("/api/v1/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure it returns a dictionary
    assert len(response.json()) > 0  # Ensure there is at least 1 book
    assert isinstance(response.json()[0], dict)  # Ensure the first item is a dictionary


def test_get_single_book():
    response = client.get("/api/v1/books/1")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "The Hobbit"
    assert data["author"] == "J.R.R. Tolkien"


def test_create_book():
    new_book = {
        "id": 4,
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "publication_year": 1997,
        "genre": Genre.FANTASY,
    }
    response = client.post("/api/v1/books/", json=new_book)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 4
    assert data["title"] == "Harry Potter and the Sorcerer's Stone"


def test_update_book():
    updated_book = {
        "id": 1,
        "title": "The Hobbit: An Unexpected Journey",
        "author": "J.R.R. Tolkien",
        "publication_year": 1937,
        "genre": "Fantasy",
    }
    response = client.put("/api/v1/books/1", json=updated_book)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "The Hobbit: An Unexpected Journey"


def test_delete_book():
    client.post(
        "/api/v1/books/",
        json={
            "id": 99,
            "title": "Temporary Book",
            "author": "Test Author",
            "publication_year": 2022,
            "genre": Genre.FANTASY,
        },
    )

    # Now delete it
    response = client.delete("/api/v1/books/99")
    assert response.status_code == 204

    # Ensure it's gone
    response = client.get("/api/vi/books/99")
    assert response.status_code == 404
