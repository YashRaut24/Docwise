from core.parser import parse_pdf, get_pdf_metadata
from core.chunker import chunk_pages

# Use any PDF you have on your computer
# If you don't have one, download any free PDF from the internet
PDF_PATH = r"C:\Users\Yash Raut\Downloads\DocWise_Test_Document.pdf"

# Parse
print("=== PDF Metadata ===")
metadata = get_pdf_metadata(PDF_PATH)
for key, value in metadata.items():
    print(f"  {key}: {value}")

print("\n=== Page Content ===")
pages = parse_pdf(PDF_PATH)
print(f"Total pages with content: {len(pages)}")

for page in pages[:3]:  # Show first 3 pages only
    print(f"\nPage {page.page_number} ({page.char_count} chars):")
    print(f"  {page.text[:200]}...")

print("\n=== Chunks ===")
chunks = chunk_pages(pages)
print(f"Total chunks: {len(chunks)}")

for chunk in chunks[:5]:  # Show first 5 chunks
    print(f"\n[Chunk {chunk.chunk_index} — Page {chunk.page_number}]")
    print(f"  {chunk.text[:150]}...")