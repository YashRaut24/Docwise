import fitz
from dataclasses import dataclass

@dataclass
class PageContent:
    page_number: int
    text: str
    char_count: int

def parse_pdf(file_path: str) -> list[PageContent]:
    """
    Extract text from each page of a PDF.
    Returns a list of PageContent objects with page number and text.
    """

    pages = []

    doc = fitz.open(file_path)

    for page_num in range(len(doc)):
        page = doc[page_num]

        text = page.get_text("text")
        text = clean_text(text)

        if text.strip():
            pages.append(PageContent(
                page_number=page_num + 1, 
                text=text,
                char_count=len(text)
            ))

    doc.close()
    return pages

def clean_text(text: str) -> str:
    """Remove common PDF noise."""
    lines = text.split("\n")
    cleaned = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if line.isdigit():
            continue

        if len(line) < 3:
            continue

        cleaned.append(line)

    return " ".join(cleaned)

def get_pdf_metadata(file_path: str) -> dict:
    """Extract basic metadata from a PDF."""
    doc = fitz.open(file_path)
    metadata = doc.metadata
    page_count = len(doc)
    doc.close()

    return {
        "title": metadata.get("title", "Unknown"),
        "author": metadata.get("author", "Unknown"),
        "page_count": page_count,
        "subject": metadata.get("subject", "")
    }
