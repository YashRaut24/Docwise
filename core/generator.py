from groq import Groq
from config import GROQ_API_KEY, LLM_MODEL
from prompts.system import DOCWISE_SYSTEM_PROMPT


class Generator:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def generate(self, question: str, chunks: list[dict]) -> dict:
        """
        Generate an answer using retrieved chunks.
        chunks: list of {"text": ..., "page_number": ...}
        Returns answer text + list of page numbers used.
        """
        context_parts = []
        for chunk in chunks:
            context_parts.append(
                f"[Page {chunk['page_number']}]: {chunk['text']}"
            )
        context = "\n\n".join(context_parts)

        response = self.client.chat.completions.create(
            model=LLM_MODEL,
            messages=[
                {"role": "system", "content": DOCWISE_SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": f"Context:\n{context}\n\nQuestion: {question}"
                }
            ],
            temperature=0.3,
            max_tokens=400
        )

        answer = response.choices[0].message.content

        # Extract unique page numbers from used chunks
        pages_used = sorted(set(chunk["page_number"] for chunk in chunks))

        return {
            "answer": answer,
            "pages_used": pages_used
        }