import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from ingest import ingest_website
from rag_pipeline import get_rag_answer

st.set_page_config(page_title="RAG Chatbot with Memory", layout="wide")

st.title("🦙 RAG Website Chatbot (with Chat History)")
st.write("Status: App loaded successfully ✅")

# ---------------- Session State ----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- Sidebar ----------------
st.sidebar.header("Website Ingestion")
url = st.sidebar.text_input("Enter Website URL")

if st.sidebar.button("Ingest Website"):
    if url:
        try:
            with st.spinner("Ingesting website..."):
                st.sidebar.success(ingest_website(url))
            st.session_state.chat_history = []  # reset history
        except Exception as e:
            st.sidebar.error(str(e))
    else:
        st.sidebar.warning("Please enter a URL")

if st.sidebar.button("Clear Chat History"):
    st.session_state.chat_history = []
    st.sidebar.success("Chat history cleared")

# ---------------- Chat UI ----------------
st.header("Ask a Question")

with st.form("question_form"):
    query = st.text_input("Type your question and press Enter")
    submitted = st.form_submit_button("Ask")

if submitted:
    if not os.path.exists("data/INGESTED.flag"):
        st.warning("Please ingest a website first.")
    else:
        with st.spinner("Generating answer..."):
            answer = get_rag_answer(query, st.session_state.chat_history)

        # store history
        st.session_state.chat_history.append((query, answer))

# ---------------- Display Chat ----------------
st.subheader("Chat History")

for i, (q, a) in enumerate(st.session_state.chat_history):
    st.markdown(f"**User:** {q}")
    st.markdown(f"**Assistant:** {a}")
    st.markdown("---")
