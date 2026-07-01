from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL

class Embedder:
    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL)

    def embed(self, text: str) -> list:
        return self.model.encode(text).tolist()

    def embed_batch(self, texts: list[str]) -> list:
        return self.model.encode(texts).tolist()