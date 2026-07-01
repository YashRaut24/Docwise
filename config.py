import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
LLM_MODEL = "llama-3.1-8b-instant"
CHROMA_PATH = "./chroma_docwise"
TOP_K_RESULTS = 5
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50