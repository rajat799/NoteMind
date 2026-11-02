from vector_store.chroma_store import search_documents
from llm.ollama_client import generate_response

def retrieve_context(collection, question, top_k=3):

    results = search_documents(
        collection,
        question,
        n_results=top_k
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    retrieved_chunks = []

    for document, metadata, distance in zip(
        documents,
        metadatas,
        distances
    ):
        retrieved_chunks.append({
            "text": document,
            "page_number": metadata["page_number"],
            "document_name": metadata["document_name"],
            "distance": distance
        })

    return retrieved_chunks

def build_prompt(question, retrieved_chunks):
    context = ""

    for chunk in retrieved_chunks:
        context += (
            f"\nSource: {chunk['document_name']}, "
            f"Page: {chunk['page_number']}\n"
            f"{chunk['text']}\n"
        )

    prompt = f"""
You are an educational assistant.

Answer the question using only the provided context.
If the answer is not available in the context,
say that there is insufficient information.
Do not invent facts.

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

    return prompt

def answer_question(collection, question, top_k=3):

    # Step 1: Retrieve relevant chunks
    retrieved_chunks = retrieve_context(
        collection,
        question,
        top_k
    )

    # Step 2: Build the augmented prompt
    prompt = build_prompt(
        question,
        retrieved_chunks
    )

    # Step 3: Generate answer using Ollama
    answer = generate_response(prompt)

    return {
        "question": question,
        "answer": answer,
        "sources": retrieved_chunks
    }