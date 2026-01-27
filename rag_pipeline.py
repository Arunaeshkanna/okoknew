import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq


def get_rag_answer(query, chat_history):
    if not os.path.exists("data/INGESTED.flag"):
        return "⚠️ Please ingest a website before asking questions."

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(
        "data/faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    docs = retriever.get_relevant_documents(query)

    context = "\n\n".join(doc.page_content for doc in docs)

    # 🔹 Build conversation history
    history_text = ""
    for q, a in chat_history[-5:]:  # last 5 turns
        history_text += f"User: {q}\nAssistant: {a}\n\n"

    llm = ChatGroq(
        model_name="llama-3.1-8b-instant",
        temperature=0
    )

    prompt = f"""
You are an expert assistant.

Conversation History:
{history_text}

Use the following context to answer the latest question.
Give a **detailed and clear explanation**, not a one-line answer.

Context:
{context}

User Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)
    return response.content
