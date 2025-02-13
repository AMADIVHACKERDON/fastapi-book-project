from api.db.sessions import engine
from api.models.book import Base

# Function to create all tables
def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("Database tables created successfully!")
