from vector_store.chroma_store import (
    initialize_chroma,
    create_collection
)

from rag.rag_pipeline import retrieve_context
from rag.rag_pipeline import answer_question

client = initialize_chroma()
collection = create_collection(client)

question = "Explain how photosynthesis works."

result = answer_question(
    collection,
    question,
    top_k=3
)

print("\n========== NOTEMIND ANSWER ==========")
print("\nQuestion:", result["question"])
print("\nAnswer:", result["answer"])

print("\n========== SOURCES ==========")

for source in result["sources"]:
    print(
        f"Document: {source['document_name']} | "
        f"Page: {source['page_number']} | "
        f"Distance: {source['distance']:.4f}"
    )