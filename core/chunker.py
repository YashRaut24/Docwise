from dataclasses import dataclass
from core.parser import PageContent


@dataclass
class Chunk:
    text: str
    page_number: int
    chunk_index: int


def chunk_pages(pages: list[PageContent], chunk_size: int = 500, overlap: int = 50) -> list[Chunk]:
    """
    Split pages into overlapping chunks, preserving page number metadata.
    Each chunk knows which page it came from.
    """
    chunks = []
    chunk_index = 0

    for page in pages:
        text = page.text

        if len(text) <= chunk_size:
            chunks.append(Chunk(
                text=text,
                page_number=page.page_number,
                chunk_index=chunk_index
            ))
            chunk_index += 1
        else:
            start = 0
            while start < len(text):
                end = start + chunk_size
                chunk_text = text[start:end].strip()

                if chunk_text:
                    chunks.append(Chunk(
                        text=chunk_text,
                        page_number=page.page_number,
                        chunk_index=chunk_index
                    ))
                    chunk_index += 1

                start += chunk_size - overlap

    return chunks