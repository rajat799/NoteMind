from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

# Single text function (query)
def generate_embedding(text):
    if not text or not text.strip():
      raise ValueError("Text cannot be empty")
    embedding = model.encode(text)
    return embedding

# Multiple text function (chunks)
def generate_embeddings(texts):
    if not texts:
      raise ValueError("Input list cannot be empty")

    if not all(isinstance(text, str) and text.strip() for text in texts):
      raise ValueError("All inputs must be non-empty strings")
    
    embeddings = model.encode(texts)
    return embeddings