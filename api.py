from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import upload, chat

app = FastAPI(title="Docwise API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router)
app.include_router(chat.router)

@app.get("/")
def root():
    return {"message": "Docwise API is running"}
