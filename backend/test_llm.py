from app.services.retriever import Retriever
from app.services.llm_service import LLMService

# Ask a question
question = "How is authentication implemented?"

# Retrieve relevant chunks
retriever = Retriever()
chunks = retriever.retrieve(question)

print("\nRetrieved", len(chunks), "chunks.\n")

# Generate answer
llm = LLMService(provider="gemini")

answer = llm.answer_question(question, chunks)

print("=" * 70)
print("FINAL ANSWER")
print("=" * 70)
print(answer)