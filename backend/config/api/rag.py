from sentence_transformers import SentenceTransformer
import chromadb

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create Chroma DB client
client = chromadb.Client()

# Create collection
collection = client.get_or_create_collection(name="books")


# ---------------------------
# ADD BOOKS TO VECTOR DB
# ---------------------------
def add_books_to_db(books):
    documents = []
    ids = []

    for book in books:
        text = f"{book.title} {book.description}"
        documents.append(text)
        ids.append(str(book.id))

    embeddings = model.encode(documents).tolist()

    collection.add(
        documents=documents,
        embeddings=embeddings,
        ids=ids
    )


# ---------------------------
# SEARCH SIMILAR BOOKS
# ---------------------------
def search_books(query):
    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    return results['documents'][0]