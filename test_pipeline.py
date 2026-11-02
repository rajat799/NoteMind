from pdf_loader import load_pdf
from chunker import create_chunk
from image_extractor import extract_images


image_records = extract_images("chap8_Hibernate.pdf")

print("Total images:", len(image_records))

for image in image_records:
    print(image)


pages = load_pdf("chap8_Hibernate.pdf")

chunks = create_chunk(pages, chunk_size=20, overlap=5)

for chunk in chunks:
  print(chunk)

