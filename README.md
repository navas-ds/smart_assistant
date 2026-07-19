Architecture

Upload

↓

Loader

↓

Chunker

↓

Embeddings

↓

ChromaDB

↓

Retriever

↓

Agent

↓

LLM

↓

Answer

Installation

git clone

cd project

pip install -r requirements.txt

cp .env.example .env

uvicorn app.main:app --reload

Run Streamlit

streamlit run ui/streamlit_app.py

Docker
docker compose up --build

API
POST /documents/upload

GET /documents

POST /chat

GET /chat/{session_id}/history

<!-- Design Decisions -->

<!-- Explain:

RecursiveCharacterTextSplitter
Why Chroma
Why BGE embeddings
Why Top-K=5
Why LangChain
Future Improvements

Mention:

Redis Memory
PostgreSQL
LangGraph
Authentication
Hybrid Search
Reranker
Async Upload -->