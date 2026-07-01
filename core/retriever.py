import chromadb
from core.embedder import Embedder
from core.chunker import Chunk
from config import CHROMA_PATH, TOP_K_RESULTS


class Retriever:
    def __init__(self):
        self.embedder = Embedder()
        self.client = chromadb.PersistentClient(path=CHROMA_PATH)
        self.active_collection = None
        self.active_doc_id = None

    def ingest_document(self, doc_id: str, chunks: list[Chunk]):
        """
        Create a new collection for this document and store all chunks.
        Each PDF gets its own isolated collection.
        """
        try:
            self.client.delete_collection(doc_id)
        except Exception:
            pass

        collection = self.client.create_collection(
            name=doc_id,
            metadata={"hnsw:space": "cosine"}
        )

        texts = [chunk.text for chunk in chunks]
        embeddings = self.embedder.embed_batch(texts)

        collection.add(
            ids=[f"chunk_{chunk.chunk_index}" for chunk in chunks],
            embeddings=embeddings,
            documents=texts,
            metadatas=[{"page_number": chunk.page_number} for chunk in chunks]
        )

        self.active_collection = collection
        self.active_doc_id = doc_id

        print(f"Ingested {len(chunks)} chunks for document '{doc_id}'")

    def load_document(self, doc_id: str):
        """Load a previously ingested document as the active collection."""
        self.active_collection = self.client.get_collection(doc_id)
        self.active_doc_id = doc_id

    def retrieve(self, query: str, k: int = TOP_K_RESULTS) -> list[dict]:
        """
        Search the active document collection.
        Returns chunks with their page numbers attached.
        """
        if not self.active_collection:
            raise ValueError("No document loaded. Upload a PDF first.")

        query_embedding = self.embedder.embed(query)
        results = self.active_collection.query(
            query_embeddings=[query_embedding],
            n_results=k
        )

        chunks_with_pages = []
        for doc, metadata in zip(
            results["documents"][0],
            results["metadatas"][0]
        ):
            chunks_with_pages.append({
                "text": doc,
                "page_number": metadata["page_number"]
            })

        return chunks_with_pages