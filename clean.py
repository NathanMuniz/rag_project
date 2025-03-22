import chromadb
import shutil

def clean_chroma_db(db_path="db/"):
    """Deletes all collections and completely removes ChromaDB storage."""
    try:
        # Connect to ChromaDB
        client = chromadb.PersistentClient(path=db_path)

        # List and delete all collections
        collections = client.list_collections()
        for col in collections:
            client.delete_collection(col.name)
            print(f"Deleted collection: {col.name}")

        # Remove the entire database folder
        shutil.rmtree(db_path)
        print(f"ChromaDB at '{db_path}' has been completely removed.")

    except FileNotFoundError:
        print("Database directory already deleted.")
    except Exception as e:
        print(f"Error: {e}")

# Run the function
clean_chroma_db()
