import fitz
from PIL import Image
import os

def pdf_to_tiff(pdf_path, output_dir):

    pdf_document = fitz.open(pdf_path)

    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)

        zoom = 6.0  
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)

        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        img = img.convert("L")

        img = img.convert("1")

        file_index = 1
        while True:
            tiff_filename = os.path.join(output_dir, f"{file_index:08d}.tiff")
            if not os.path.exists(tiff_filename):
                break
            file_index += 1

        img.save(tiff_filename, compression="group4", dpi=(300, 300))

    pdf_document.close()

