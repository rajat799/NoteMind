def create_chunk(pages, chunk_size, overlap):
  chunks = []
  chunk_id = 1

  if chunk_size <= 0:
    raise ValueError("Chunk size should be greater than 0")


  if overlap < 0 or overlap >= chunk_size:
    raise ValueError("overlap should be greater than 0 and smaller than chunk size")

  for page in pages:
    page_number = page["page_no"]
    
    words = page["text"].split()
    
    start = 0

    # loop
    while start < len(words):
      if start >= len(words) - overlap:
        break
      end = start + chunk_size

      chunk_word = words[start:end]

      chunk_text = " ".join(chunk_word)


      chunk_data = {
        "chunk_id":chunk_id,
        "page_number":page_number,
        "text":chunk_text
      }

      chunks.append(chunk_data)

      chunk_id += 1

      start += chunk_size - overlap

  return chunks


# # main
# pages = [
#     {
#         "page_number": 1,
#         "text": "I am learning Python and building a RAG application for students"
#     }
# ]

# chunks = create_chunk(pages, 5, 2)

# for chunk in chunks:
#   print(chunk)

