#  Codebase AI Assistant

An intelligent AI-powered codebase assistant that allows users to upload a repository and ask questions about the code.  
Built using **RAG (Retrieval-Augmented Generation)** with **Qdrant + LLM + FastAPI + React**.

---

##  Live Demo

- 🔗 Frontend: https://codebase-ai-assistant-frontend.vercel.app/
- 🔗 Backend API: https://kirankumar29-codebase-assitant.hf.space

---

##  Features

-  Upload GitHub repository or local codebase
-  Semantic search using vector embeddings
-  Ask questions about your code
-  Get file-based explanations
-  Supports multiple programming languages
- ⚡ Fast retrieval using Qdrant vector database

---

##  Architecture
```
User Question
↓
Frontend (React / Vercel)
↓
FastAPI Backend (Hugging Face)
↓
Qdrant Vector DB
↓
Relevant Code Context
↓
LLM (Groq)
↓
Answer

```

##  Tech Stack

### 🔹 Backend
- FastAPI
- LangChain
- Qdrant Vector Database
- Groq LLM (LLaMA 3)
- HuggingFace Embeddings

### 🔹 Frontend
- React / Next.js
- Tailwind CSS
- Vercel Deployment

---

## ⚙️ How It Works

1.  Upload a repository
2.  Files are filtered and processed
3.  Converted into embeddings
4.  Stored in Qdrant
5.  User asks a question
6.  Relevant code is retrieved
7.  LLM generates answer based on context

---

##  Installation (Backend)

```bash
git clone https://github.com/kumar-kiran-24/Codebase-AI-Assistant.git
cd Codebase-AI-Assistant

pip install -r requirements.txt

```
