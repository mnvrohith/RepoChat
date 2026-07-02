<div align="center">

# RepoChat

**AI-powered GitHub Repository Chat using Retrieval-Augmented Generation (RAG)**

Understand any codebase by asking questions in natural language.

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?logo=mongodb)
![Gemini](https://img.shields.io/badge/Gemini-2.5%20Flash-4285F4)
![RAG](https://img.shields.io/badge/RAG-Enabled-orange)

</div>

---

## Overview

RepoChat is an AI-powered Retrieval-Augmented Generation (RAG) application that enables developers to interact with GitHub repositories using natural language. Instead of manually exploring hundreds of source files, users can ask questions about a repository and receive context-aware answers generated directly from the repository's code.

The application clones a GitHub repository, parses and chunks its source code, generates vector embeddings, stores them in MongoDB Atlas Vector Search, and retrieves the most relevant code snippets to generate grounded responses using Gemini 2.5 Flash.

---

## Why RepoChat?

Understanding an unfamiliar codebase is often one of the biggest challenges for developers. Large repositories require navigating multiple folders, reading documentation, and searching through numerous files before understanding how a feature is implemented.

RepoChat simplifies this process by combining semantic search with Retrieval-Augmented Generation (RAG). Instead of relying solely on an LLM's knowledge, it retrieves relevant code from the repository and uses that context to generate accurate, repository-specific answers.

---

## Technology Stack

| Category | Technology | Purpose |
|:---------|:-----------|:--------|
| **Frontend** | Streamlit | Interactive web application |
| **Backend** | FastAPI | REST API development |
| **Database** | MongoDB Atlas | Store users, repositories, conversations and code chunks |
| **Vector Search** | MongoDB Atlas Vector Search | Semantic retrieval |
| **LLM** | Gemini 2.5 Flash | Repository-aware answer generation |
| **Embedding Model** | BAAI/bge-small-en-v1.5 | Generate vector embeddings |
| **Repository Processing** | GitIngest | Clone and preprocess GitHub repositories |
| **Code Parsing** | Tree-sitter | Parse source code into meaningful chunks |
| **Authentication** | JWT | Secure user authentication |
| **Password Security** | bcrypt | Password hashing |
| **AI SDK** | google-generativeai | Gemini integration |
| **Embeddings** | sentence-transformers | Embedding generation |
| **Validation** | Pydantic | Request and response validation |
| **Database Driver** | PyMongo | MongoDB operations |
| **Server** | Uvicorn | FastAPI ASGI server |

---

## Features

- AI-powered repository chat using Retrieval-Augmented Generation (RAG)
- Index any public GitHub repository
- Automatic repository cloning and preprocessing
- Language-aware code parsing using Tree-sitter
- Semantic code chunking for efficient retrieval
- Vector embedding generation using BAAI/bge-small-en-v1.5
- Fast semantic search with MongoDB Atlas Vector Search
- Repository-grounded answers generated using Gemini 2.5 Flash
- Secure user authentication using JWT
- Multiple project management
- Persistent conversation history
- Source-aware responses based only on retrieved repository context

---

## Repository Ingestion Pipeline

```text
GitHub Repository
        │
        ▼
Clone Repository (GitIngest)
        │
        ▼
Parse Source Code (Tree-sitter)
        │
        ▼
Semantic Code Chunking
        │
        ▼
Embedding Generation
        │
        ▼
Store Chunks + Metadata + Embeddings
        │
        ▼
MongoDB Atlas Vector Search
```

The repository is cloned, parsed into semantic code chunks, embedded using the BAAI embedding model, and stored in MongoDB Atlas Vector Search for efficient semantic retrieval.

---

## Question Answering Pipeline

```text
User Question
      │
      ▼
Generate Question Embedding
      │
      ▼
Vector Similarity Search
      │
      ▼
Retrieve Relevant Code Chunks
      │
      ▼
Build Prompt
      │
      ▼
Gemini 2.5 Flash
      │
      ▼
Repository-Aware Answer
      │
      ▼
Store Conversation History
```

For each question, RepoChat generates an embedding for the query, retrieves the most relevant code chunks through vector search, constructs a context-rich prompt, and generates an answer grounded in the repository. The conversation is then stored for future reference.

AI-powered GitHub Repository RAG Assistant built using FastAPI, Streamlit, MongoDB Atlas, Tree-sitter, gitingest, and Gemini.