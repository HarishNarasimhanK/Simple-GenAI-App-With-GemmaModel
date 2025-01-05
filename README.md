# Simple-GenAI-App-With-GemmaModel
# Document Question-Answering System

## Overview
This project implements a question-answering system that can process various document formats (PDF, TXT) and answer questions based on their content. It utilizes LangChain, vector stores (FAISS and Chroma), and language models for document processing and question answering.

## Project Structure
```
.
├── DataIngestion.ipynb          # Notebook for data ingestion processes
├── QnA_Bot_ForWebpageBasedDocuments.ipynb  # Web-based Q&A implementation
├── alien.pdf                    # Sample PDF document
├── alien.txt                    # Sample text document
├── app.py                       # Main application file
├── chroma.ipynb                # Implementation using Chroma vector store
├── faiss.ipynb                 # Implementation using FAISS vector store
└── requirements.txt            # Project dependencies
```

## Features
- Document processing support for multiple formats (PDF, TXT)
- Web-based document Q&A capabilities
- Multiple vector store implementations (FAISS and Chroma)
- Flexible document ingestion pipeline
- Interactive question-answering interface

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Jupyter Notebooks
- `DataIngestion.ipynb`: Demonstrates the document ingestion process
- `QnA_Bot_ForWebpageBasedDocuments.ipynb`: Shows implementation for web-based documents
- `chroma.ipynb`: Examples using Chroma vector store
- `faiss.ipynb`: Examples using FAISS vector store

### Running the Application
```bash
python app.py
```

## Dependencies
The project requires several key libraries:
- LangChain
- FAISS
- Chroma
- PDF processing libraries
- Language model dependencies

See `requirements.txt` for a complete list of dependencies.

## Vector Store Implementations

### FAISS
- Efficient similarity search
- Scalable to large document collections
- Optimized for dense vectors

### Chroma
- Persistent storage capabilities
- Metadata filtering
- Easy integration with LangChain

## Model Configuration
The project currently uses the Gemma 2B model through Ollama. Configuration example:

```python
from langchain_community.chat_models import ChatOllama
llm = ChatOllama(model="gemma2:2b")
```

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
