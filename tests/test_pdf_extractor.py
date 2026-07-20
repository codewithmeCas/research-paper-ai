"""
Tests for core/pdf_extractor.py, focused on error handling since that's
the riskiest part of dealing with user-uploaded files.

Run with: pytest tests/test_pdf_extractor.py
"""

import sys
from pathlib import Path

import fitz
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.pdf_extractor import PDFExtractionError, extract_text_from_pdf


def test_raises_error_for_missing_file(tmp_path: Path) -> None:
    fake_path = tmp_path / "does_not_exist.pdf"
    with pytest.raises(PDFExtractionError, match="not found"):
        extract_text_from_pdf(fake_path)


def test_raises_error_for_corrupted_file(tmp_path: Path) -> None:
    fake_pdf = tmp_path / "corrupted.pdf"
    fake_pdf.write_text("This is not actually a PDF file.")

    with pytest.raises(PDFExtractionError):
        extract_text_from_pdf(fake_pdf)


def test_extracts_text_from_a_real_pdf(tmp_path: Path) -> None:
    # Build a minimal real PDF with PyMuPDF so this test doesn't depend
    # on an external sample file.
    document = fitz.open()
    page = document.new_page()
    page.insert_text((72, 72), "Abstract\nThis is a simple test paper about testing.")
    test_pdf_path = tmp_path / "test_paper.pdf"
    document.save(test_pdf_path)
    document.close()

    extracted_text = extract_text_from_pdf(test_pdf_path)
    assert "test paper about testing" in extracted_text


def test_raises_error_for_empty_pdf(tmp_path: Path) -> None:
    # A page with no text simulates a scanned image PDF with no text layer.
    document = fitz.open()
    document.new_page()
    empty_pdf_path = tmp_path / "empty.pdf"
    document.save(empty_pdf_path)
    document.close()

    with pytest.raises(PDFExtractionError, match="No readable text"):
        extract_text_from_pdf(empty_pdf_path)


def test_raises_error_for_password_protected_pdf(tmp_path: Path) -> None:
    # Build a real encrypted PDF to confirm the encryption check actually
    # works, instead of just assuming it would.
    document = fitz.open()
    page = document.new_page()
    page.insert_text((72, 72), "Secret content protected by a password.")
    encrypted_pdf_path = tmp_path / "encrypted.pdf"
    document.save(
        str(encrypted_pdf_path),
        encryption=fitz.PDF_ENCRYPT_AES_256,
        owner_pw="owner123",
        user_pw="user123",
    )
    document.close()

    with pytest.raises(PDFExtractionError, match="password-protected"):
        extract_text_from_pdf(encrypted_pdf_path)