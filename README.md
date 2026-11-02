# NoteMind – AI-Powered Document Question Answering System

NoteMind is an AI-powered document learning assistant that uses Retrieval-Augmented Generation (RAG) to help students ask questions about their study materials and receive context-based answers.

## Features

- **PDF Text Extraction:** Extracts text and page information from PDF documents using PyMuPDF.
- **Text Chunking:** Splits extracted content into smaller chunks for efficient retrieval.
- **Semantic Embeddings:** Uses Sentence Transformers (`all-MiniLM-L6-v2`) to generate 384-dimensional embeddings.
- **Vector Database:** Stores document chunks, embeddings and metadata using ChromaDB.
- **Semantic Search:** Retrieves relevant document chunks based on user questions.
- **LLM Integration:** Uses Qwen 2.5 3B through Ollama for local answer generation.
- **RAG Pipeline:** Combines retrieved document context with user questions to generate grounded answers.
- **Source References:** Retains document names and page numbers for retrieved content.

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| PDF Processing | PyMuPDF |
| Embedding Model | Sentence Transformers |
| Embedding Model Name | all-MiniLM-L6-v2 |
| Vector Database | ChromaDB |
| Local LLM Runtime | Ollama |
| Language Model | Qwen 2.5 3B |
| HTTP Client | Requests |

## Architecture

1. Extract text and page information from PDF documents.
2. Split the extracted text into smaller chunks.
3. Generate embeddings for each chunk.
4. Store embeddings, text and metadata in ChromaDB.
5. Convert the student's question into an embedding.
6. Retrieve the most relevant chunks using semantic search.
7. Construct a prompt using the retrieved context.
8. Send the prompt to Qwen through Ollama.
9. Return the generated answer along with source metadata.

## Project Setup

### 1. Clone the repository

```bash
git clone https://github.com/rajat799/NoteMind.git
cd NoteMind
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Download Ollama from https://ollama.com/download.

Pull the required model:

```bash
ollama pull qwen2.5:3b
```

### 5. Run the model

```bash
ollama run qwen2.5:3b
```

### 6. Run the application tests

From the project root:

```bash
python -m tests.test_embeddings
python -m tests.test_chroma_store
python -m tests.test_rag
```

Note: The current test scripts use sample document chunks. The PDF ingestion and RAG pipeline are under active development.

## Current Project Status

The initial RAG pipeline is implemented and tested with sample Hibernate document chunks.

Current capabilities include PDF text extraction, chunking, embedding generation, vector storage, semantic retrieval and context-based answer generation.

## Future Enhancements

- Relevance thresholding and improved retrieval quality
- Citation validation and improved source attribution
- Automated PDF ingestion
- Support for multiple uploaded documents
- FastAPI backend
- React frontend
- Interactive document-based chat
- Quiz generation and student learning analytics

## Author

Developed as a personal AI/Generative AI learning and portfolio project.