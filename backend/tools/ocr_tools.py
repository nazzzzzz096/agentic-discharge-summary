import easyocr

reader = easyocr.Reader(
    ['en'],
    gpu=False
)


def extract_text(image_path):
    """
    Extract text from image using EasyOCR.

    Args:
        image_path (str):
            Path to image.

    Returns:
        str:
            OCR extracted text.
    """

    result = reader.readtext(
        image_path,
        detail=0
    )

    text = "\n".join(result)

    return text