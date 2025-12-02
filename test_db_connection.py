#test_db_connection.py
from database.db_connection import db

def test_connection():
    try:
        #list collections in database as a test
        collections = db.list_collection_names()
        print("Successfully connected to MongoDB!")
        print(f"Current collections: {collections}")
    except Exception as e:
        print("Error connecting to MongoDB:", e)

if __name__ == "__main__":
    test_connection()
