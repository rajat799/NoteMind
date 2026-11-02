from vector_store.chroma_store import (
    initialize_chroma,
    create_collection,
    add_documents,
    search_documents
)

# Connect to ChromaDB
client = initialize_chroma()

# Get or create collection
collection = create_collection(client)

# Sample document chunks
chunks = [
    {
        "chunk_id": 1,
        "page_number": 1,
        "text": "Hibernate is an ORM framework."
    },
    {
        "chunk_id": 2,
        "page_number": 2,
        "text": "Hibernate maps Java objects to database tables."
    },
    {
        "chunk_id": 3,
        "page_number": 3,
        "text": "Hibernate supports database operations."
    }
]

# Store chunks
total = add_documents(
    collection,
    chunks,
    "hibernate"
)

print("Chunks stored:", total)
print("Total records:", collection.count())

# Test semantic search

query = "Explain Hibernate ORM."

results = search_documents(
    collection,
    query,
    n_results=3
)

print("\nSearch results:")

for i in range(len(results["documents"][0])):

    print(f"\nResult {i+1}")

    print("Document:", results["documents"][0][i])

    print("Metadata:", results["metadatas"][0][i])

    print("Distance:", results["distances"][0][i])