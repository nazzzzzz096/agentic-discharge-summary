import json
from pathlib import Path

from backend.tools.pdf_to_image import pdf_to_images
from backend.tools.ocr_tools import extract_text


def build_document_store(pdf_path: str) -> dict:
    """
    Build a document store from a PDF.

    Args:
        pdf_path (str):
            Path to uploaded PDF.

    Returns:
        dict:
            OCR extracted document store.
    """

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    images = pdf_to_images(pdf_path)

    document_store = {}

    print(f"Processing {len(images)} pages")

    for idx, image_path in enumerate(images):

        print(f"Processing page {idx+1}")

        try:

            ocr_file = (
                output_dir /
                f"page_{idx+1}.txt"
            )

            if ocr_file.exists():

                print(
                    f"Loading cached page {idx+1}"
                )

                with open(
                    ocr_file,
                    "r",
                    encoding="utf-8"
                ) as f:

                    text = f.read()

            else:

                print(
                    f"OCR page {idx+1}"
                )

                text = extract_text(
                    image_path
                )

                with open(
                    ocr_file,
                    "w",
                    encoding="utf-8"
                ) as f:

                    f.write(text)

            document_store[
                f"page_{idx+1}"
            ] = text

        except Exception as e:

            document_store[
                f"page_{idx+1}"
            ] = f"ERROR: {str(e)}"

    with open(
        output_dir / "document_store.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            document_store,
            f,
            indent=2,
            ensure_ascii=False
        )

    return document_store