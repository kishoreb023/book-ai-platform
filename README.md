📚 Book AI Platform (Document Intelligence System)
🚀 Overview

This is a full-stack AI-powered Document Intelligence Platform that allows users to browse books, ask intelligent questions, and get AI-generated insights using a Retrieval-Augmented Generation (RAG) pipeline.

The system collects book data using web automation, stores it in a backend database, generates embeddings for semantic search, and uses an LLM to provide contextual answers with source-based responses.

🧠 Key Features
📖 Book listing with title, author, rating, and description
🔍 Intelligent Q&A system using RAG pipeline
🤖 AI-generated insights (summary, recommendations, classification)
📊 Vector-based similarity search using embeddings
🌐 Full-stack web interface (React + Tailwind CSS)
⚡ REST APIs for all backend operations
🕷️ Automated book data scraping
🏗️ Tech Stack
Backend
Django REST Framework
Python
MySQL (metadata storage)
AI / ML
OpenAI / LM Studio (LLM integration)
Sentence Transformers (embeddings)
ChromaDB / FAISS (vector search)
Frontend
ReactJS
Tailwind CSS
Automation
Selenium (web scraping)
🧩 System Architecture
Scraper Module → Collects book data from web
Backend API → Stores and serves book data
Embedding Engine → Converts text into vectors
Vector Database → Stores embeddings for similarity search
RAG Pipeline → Retrieves relevant chunks + LLM generates answer
Frontend UI → Displays results and user interaction
🔥 AI Features
1. Book Summary

Generates short and meaningful summaries of books.

2. Genre Classification

Predicts book category based on description.

3. Recommendation System

Suggests similar books (“If you like X, you may like Y”).

4. RAG Question Answering
Converts user question into embeddings
Performs similarity search
Retrieves relevant context
Generates final answer using LLM with citations
📡 API Endpoints
GET
/api/books/ → List all books
/api/books/<id>/ → Book details
/api/recommend/ → Recommended books
POST
/api/upload/ → Upload/scrape books
/api/ask/ → Ask AI questions (RAG endpoint)
⚙️ Setup Instructions
1. Clone Repository
git clone https://github.com/kishoreb023/book-ai-platform.git
cd book-ai-platform
2. Backend Setup
cd backend
pip install -r requirements.txt
python manage.py runserver
3. Frontend Setup
cd frontend
npm install
npm start
🧪 Sample Questions
“Summarize Sapiens”
“Recommend books like Sharp Objects”
“What is the genre of this book?”
“Explain the main theme of Sapiens”

Dashboard Page
Book Details Page
Q&A Interface
📌 Future Improvements
Async scraping pipeline (Celery)
Advanced caching for AI responses
Multi-source book ingestion
Chat history saving
Improved ranking system for recommendations
👨‍💻 Author

Kishore B
3rd Year AI & Data Science Student
