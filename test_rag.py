from core.parser import parse_pdf
from core.chunker import chunk_pages
from core.retriever import Retriever
from core.generator import Generator

PDF_PATH = r"C:/Users/Yash Raut/Downloads/DocWise_Test_Document.pdf"

print("=== Docwise RAG Test ===\n")

pages = parse_pdf(PDF_PATH)
print(f"Parsed {len(pages)} pages")

chunks = chunk_pages(pages)
print(f"Created {len(chunks)} chunks")

retriever = Retriever()
retriever.ingest_document("test_doc", chunks)

generator = Generator()
question = "What was the patient's age and visit date?"

print(f"\nQuestion: {question}")

retrieved = retriever.retrieve(question)
result = generator.generate(question, retrieved)

print(f"\nAnswer: {result['answer']}")
print(f"Pages used: {result['pages_used']}")