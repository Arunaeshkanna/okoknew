# new-project-using-groq (CLAYSYS PROJECT)

This project is a Retrieval-Augmented Generation (RAG) chatbot that allows users to chat with the content of any website.
First, the user provides a website URL. The system scrapes and cleans the website content, splits it into meaningful chunks, and converts those chunks into vector embeddings using a sentence transformer model. These embeddings are stored in a FAISS vector database.
When the user asks a question, the chatbot retrieves the most relevant content from the vector database, combines it with previous chat history, and sends it to a large language model (LLM) to generate a context-aware and detailed answer.
The application is built using Streamlit and supports chat memory, making the conversation feel natural and continuous


| Technology                         | One-Line Definition                                               |
| ---------------------------------- | ----------------------------------------------------------------- |
| **Python**                         | Core programming language used to build the entire system         |
| **Streamlit**                      | Frontend framework to create an interactive web-based chatbot UI  |
| **Requests**                       | Used to fetch website HTML content                                |
| **BeautifulSoup**                  | Parses and cleans scraped website data                            |
| **LangChain**                      | Framework for building RAG pipelines and LLM workflows            |
| **RecursiveCharacterTextSplitter** | Splits large text into overlapping chunks for better retrieval    |
| **HuggingFace Embeddings**         | Converts text into numerical vectors for semantic search          |
| **Sentence-Transformers (MiniLM)** | Lightweight embedding model for fast and accurate vector creation |
| **FAISS**                          | Vector database for efficient similarity search                   |
| **Groq LLM (LLaMA 3.1)**           | Large Language Model used to generate final answers               |
| **dotenv**                         | Manages environment variables securely                            |
| **Session State (Streamlit)**      | Maintains chat history for conversational memory                  |



#FLOW CHART:-
User enters Website URL
        ↓
Website Scraper (Requests + BeautifulSoup)
        ↓
Text Cleaning (remove scripts, styles, noise)
        ↓
Text Splitter (chunking with overlap)
        ↓
Text Embeddings (HuggingFace Sentence Transformer)
        ↓
FAISS Vector Store (saved locally)
        ↓
INGESTED.flag created
        ↓
User asks a question
        ↓
Retrieve relevant chunks from FAISS
        ↓
Combine:
   - Retrieved context
   - Previous chat history
        ↓
Send prompt to Groq LLM (LLaMA 3.1)
        ↓
LLM generates contextual answer
        ↓
Answer displayed in Streamlit UI
        ↓
Chat history stored in session state


<img width="451" height="835" alt="image" src="https://github.com/user-attachments/assets/b0c8fcc8-6c26-4361-a9cf-197cc47c26ec" />
