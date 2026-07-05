import os
import uuid # generates unique ids
import shutil # performs managing files operations
from fastapi import APIRouter, UploadFile, File
from core.parser import parse_pdf, get_pdf_metadata
from core.chunker import chunk_pages
from state import retriever

router = APIRouter()

UPLOAD_DIR = "./uploaded_pdfs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.endswith(".pdf"):
        return {"error" : "Only PDF files are supported"}
    
    doc_id = str(uuid.uuid4())[:8] #creates unique id everytime having 8 characters
    file_path = f"{UPLOAD_DIR}/{doc_id}.pdf"

    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file,f)

    
    try:
        metadata = get_pdf_metadata(file_path)
        pages = parse_pdf(file_path)

        if not pages:
             return {"error": "Could not extract text from this PDF. It may be scanned."}
        
        chunks = chunk_pages(pages)
        retriever.ingest_document(doc_id, chunks)


        return {
            "doc_id": doc_id,
            "filename": file.filename,
            "page_count": metadata["page_count"],
            "chunks_created": len(chunks),
            "message": f"Successfully processed '{file.filename}'"
        }
    
    except Exception as e:
        return {"error":f"Failed to process PDF: {str(e)}"}

