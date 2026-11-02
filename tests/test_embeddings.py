print("Starting embedding tests...")

from embeddings.embedding_model import (
    generate_embedding,
    generate_embeddings
)

print("Model imported successfully!")

query = "What is hibernate?"

print("Generating single embedding...")
query_vector = generate_embedding(query)

print("Single embedding:", query_vector.shape)
print(query_vector)
chunks = [
    "Hibernate is an ORM framework.",
    "Hibernate maps Java objects to database tables.",
    "Hibernate supports database operations."
]

print("Generating multiple embeddings...")
chunk_vectors = generate_embeddings(chunks)

print("Multiple embeddings:", chunk_vectors.shape)

print("All tests completed!")

# to run this file: python -u -m tests.test_embeddings