from fastapi import APIRouter
from pydantic import BaseModel
from state import retriever,generator

router = APIRouter()

class ChatRequest(BaseModel):
    doc_id: str
    question: str


@router.post("/chat")

def chat(request: ChatRequest):
    try: 
        retriever.load_document(request.doc_id)

        chunks = retriever.retrieve(request.question)

        if not chunks:
            return {
                "answer": "I couldn't find relevant information in this document.",
                "pages_used": []
            }
        
        result = generator.generate(request.question, chunks)

        return {
            "answer" : result["answer"],
            "pages_used" : result["pages_used"]
        }
    

    except Exception as e:
        return {"error": str(e)}