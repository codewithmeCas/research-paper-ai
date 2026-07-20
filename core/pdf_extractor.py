"""
Reads PDF files and pulls the text out of them.

This file only handles extracting text. Cleaning it up and detecting
sections happens elsewhere.
"""

from pathlib import Path

import fitz  # PyMuPDF

from utils.logger import get_logger

logger = get_logger(__name__)


class PDFExtractionError(Exception):
    """Raised when a PDF can't be opened or has no readable text."""


def extract_text_from_pdf(pdf_path: Path) -> str:
    """
    Extract all text from a PDF file, page by page.

    Args:
        pdf_path: Path to the PDF file on disk.

    Returns:
        The full extracted text, with pages separated by double newlines.

    Raises:
        PDFExtractionError: If the file doesn't exist, isn't a valid PDF,
            is password-protected, or has no extractable text.
    """
    if not pdf_path.exists():
        raise PDFExtractionError(f"File not found: {pdf_path}")

    try:
        pdf_document = fitz.open(pdf_path)
    except fitz.FileDataError as error:
        raise PDFExtractionError(
            "This file could not be read as a PDF. It may be corrupted."
        ) from error

    if pdf_document.is_encrypted:
        pdf_document.close()
        raise PDFExtractionError(
            "This PDF is password-protected. Please upload an unlocked PDF."
        )

    if pdf_document.page_count == 0:
        pdf_document.close()
        raise PDFExtractionError("This PDF has no pages.")

    extracted_pages: list[str] = []
    for page in pdf_document:
        extracted_pages.append(page.get_text())

    # page_count must be read before closing the document.
    total_page_count = pdf_document.page_count
    pdf_document.close()

    full_text = "\n\n".join(extracted_pages)

    if len(full_text.strip()) < 50:
        raise PDFExtractionError(
            "No readable text was found in this PDF. It may be a scanned "
            "image without a text layer, which this app cannot process."
        )

    logger.info("Extracted %d characters from %s (%d pages).",
                len(full_text), pdf_path.name, total_page_count)

    return full_text