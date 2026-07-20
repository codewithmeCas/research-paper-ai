# Research Paper AI

I made this project to make reading research papers a lot easier. Just upload a research paper PDF and it does the rest. It summarizes the paper, finds sections like the abstract, methodology, results, and conclusion, pulls out the key terms, and even creates a PowerPoint presentation you can download. It's built with Python and (eventually) Streamlit.

Everything will run locally using open-source AI models, so there's no need for any paid APIs.

## Project Status

Still working on it! I'm building one part at a time.

### Finished
- `config.py` – Stores all the settings like folder paths, AI model names, section names, and PowerPoint options.
- `core/pdf_extractor.py` – Reads text from research paper PDFs and handles things like missing files, corrupted PDFs, password-protected PDFs, and scanned PDFs with no readable text.
- Unit tests for both files (5 tests passing with `pytest`).

### Next up
- `core/text_cleaner.py` – Clean up extracted text.
- `core/section_detector.py` – Find different sections in the paper.
- `core/summarizer.py` – Generate summaries using AI.
- `core/keyword_extractor.py` – Extract important keywords.
- `core/ppt_generator.py` – Create the PowerPoint presentation.
- `app.py` – Build the Streamlit web app.

## How it works

1. Upload a research paper PDF.
2. Extract all the text.
3. Clean up the text.
4. Detect sections like the Abstract, Methodology, Results, and Conclusion.
5. Summarize each section with a local AI model.
6. Extract important keywords.
7. Generate a PowerPoint presentation.
8. Download the summary and presentation.

## Running the tests

```bash
pip install PyMuPDF pytest
pytest tests/ -v
```

## Tech Stack

- Python
- PyMuPDF
- Streamlit (planned)
- Hugging Face Transformers (planned)
- KeyBERT (planned)
- python-pptx (planned)