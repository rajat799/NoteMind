from pathlib import Path
import pymupdf
from collections import Counter




def extract_images(pdf_path):

    xref_counts = Counter()

    output_folder = Path("images")
    output_folder.mkdir(exist_ok=True)

    with pymupdf.open(pdf_path) as doc:
        image_records = []
        image_id = 1
        for page in doc:
            for img in page.get_images(full=True):
                xref_counts[img[0]] += 1
            page_number = page.number + 1

            images = page.get_images(full=True)

            print(f"Page {page_number}: {len(images)} images")

            image_number = 1
            for img in images:

                xref = img[0]
                # xref_counts[xref] += 1

                if xref_counts[xref] > 1:
                  continue
                image_data = doc.extract_image(xref)
                extension = image_data["ext"]
                image_bytes = image_data["image"]

                filename = f"page_{page_number}_image_{image_number}.{extension}"
                image_path = output_folder / filename

                image_path.write_bytes(image_bytes)

                print(f"Saved: {image_path}")

                image_data_record = {
                    "image_id": image_id,
                    "page_number": page_number,
                    "xref": xref,
                    "image_path": str(image_path),
                    "extension": extension
                }

                image_records.append(image_data_record)
                image_id += 1

                image_number += 1

        return image_records