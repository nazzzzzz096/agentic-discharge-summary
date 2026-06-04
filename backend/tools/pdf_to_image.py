import fitz
from pathlib import Path

def pdf_to_images(pdf_path:str):

    output_dir=Path("temp")
    output_dir.mkdir(exist_ok=True)

    pdf = fitz.open(pdf_path)

    image_paths = []
    
    for page_num in range(len(pdf)):

        page = pdf.load_page(page_num)

        pix = page.get_pixmap(matrix=fitz.Matrix(2,2))

        image_path =output_dir / f"page_{page_num+1}.png"

        pix.save(str(image_path))

        image_paths.append(str(image_path))
    pdf.close()

    return image_paths