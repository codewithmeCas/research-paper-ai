"""All the project settings live here so they're easy to find and change."""

from pathlib import Path

# Folder paths

BASE_DIR: Path = Path(__file__).resolve().parent

OUTPUTS_DIR: Path = BASE_DIR / "outputs"
SUMMARIES_DIR: Path = OUTPUTS_DIR / "summaries"
PRESENTATIONS_DIR: Path = OUTPUTS_DIR / "presentations"
TEMP_UPLOADS_DIR: Path = BASE_DIR / "temp_uploads"

# Create these folders if they don't exist yet, so the app doesn't crash
# the first time it tries to save something.
for folder in (SUMMARIES_DIR, PRESENTATIONS_DIR, TEMP_UPLOADS_DIR):
    folder.mkdir(parents=True, exist_ok=True)

# File upload limits

MAX_PDF_SIZE_MB: int = 25
MAX_PDF_SIZE_BYTES: int = MAX_PDF_SIZE_MB * 1024 * 1024

# AI model settings

# Smaller, faster version of BART that runs on a CPU.
SUMMARIZATION_MODEL_NAME: str = "sshleifer/distilbart-cnn-12-6"

# The model can only handle this many tokens at a time, so longer text
# gets split into chunks before being summarized.
MODEL_MAX_INPUT_TOKENS: int = 1024

SUMMARY_MAX_LENGTH: int = 150
SUMMARY_MIN_LENGTH: int = 40

KEYWORD_MODEL_NAME: str = "all-MiniLM-L6-v2"
NUMBER_OF_KEYWORDS: int = 10

# Section detection settings

# Different papers word their headings differently, so this maps each
# official section name to the different ways it might appear.
SECTION_NAME_SYNONYMS: dict[str, list[str]] = {
    "Abstract": ["abstract"],
    "Introduction": ["introduction", "background"],
    "Methodology": [
        "methodology",
        "methods",
        "materials and methods",
        "approach",
        "experimental setup",
    ],
    "Results": ["results", "findings", "evaluation"],
    "Discussion": ["discussion"],
    "Conclusion": ["conclusion", "conclusions", "summary and conclusion"],
    "References": ["references", "bibliography", "works cited"],
}

# The order sections should appear in on the slides.
PRESENTATION_SECTION_ORDER: list[str] = [
    "Abstract",
    "Introduction",
    "Methodology",
    "Results",
    "Discussion",
    "Conclusion",
]

# PowerPoint styling

PRESENTATION_TITLE_FONT_SIZE: int = 32
PRESENTATION_HEADING_FONT_SIZE: int = 26
PRESENTATION_BODY_FONT_SIZE: int = 16

MAX_CHARACTERS_PER_SLIDE: int = 700