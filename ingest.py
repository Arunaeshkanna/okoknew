import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from utils.scraper import scrape_website
from utils.splitter import split_text

def ingest_website(url):
    os.makedirs("data/faiss_index", exist_ok=True)

    text = scrape_website(url)
    chunks = split_text(text)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_texts(chunks, embeddings)
    vectorstore.save_local("data/faiss_index")

    with open("data/INGESTED.flag", "w") as f:
        f.write("done")

    return "✅ Website ingested and indexed with FAISS"
