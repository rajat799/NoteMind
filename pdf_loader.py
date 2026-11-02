import pymupdf
pages = [] 


def load_pdf(filename):
  try:
    with pymupdf.open(filename) as doc:
    

      for page in doc: # iterate the document pages
          # get page no
          page_number = page.number + 1

          # Extract Text
          text = page.get_text() # extracts as a string

          if not text.strip():
              continue

          page_data = {
              "page_no": page_number,
              "text":text
          }

          pages.append(page_data)

    return pages

      # print(pages)

  except Exception as e:
      print(f"Error processing PDF: {e}")


