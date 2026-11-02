import chromadb
from embeddings.embedding_model import generate_embeddings, generate_embedding



def initialize_chroma():
  client = chromadb.PersistentClient(path="./chroma_db")

  return client

def create_collection(client):
    collection = client.get_or_create_collection(
        name="student_documents",
        metadata={"hnsw:space": "cosine"}
    )

    return collection

def add_documents(collection, chunks, document_name):
    if not chunks:
        raise ValueError("No document chunks provided")

    texts = [chunk["text"] for chunk in chunks]

    embeddings = generate_embeddings(texts)

    ids = [
        f"{document_name}_chunk_{chunk['chunk_id']}"
        for chunk in chunks
    ]

    metadatas = [
        {
            "page_number": chunk["page_number"],
            "document_name": document_name,
            "chunk_id": chunk["chunk_id"]
        }
        for chunk in chunks
    ]

    collection.upsert(
        ids=ids,
        documents=texts,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )

    return len(chunks)

# Search docs function
def search_documents(collection, query, n_results=3):
    if not query or not query.strip():
      raise ValueError("Query cannot be empty")

    query_embedding = generate_embedding(query) # for the user single query

    # Perform similarity search
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=n_results,
        include=["documents", "metadatas", "distances"]
    )

    return results


