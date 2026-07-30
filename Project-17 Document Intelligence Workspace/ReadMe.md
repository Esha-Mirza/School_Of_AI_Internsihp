# Document Intelligence Workspace

A collaborative document analysis system where multiple AI agents analyze uploaded documents to extract insights, identify red flags, and summarize key information.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Ollama](https://img.shields.io/badge/LLM-Ollama-black)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [The Agents](#the-agents)
- [Technology Stack](#technology-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Supported Document Formats](#supported-document-formats)
- [Sample Document (TXT)](#sample-document-txt)
- [Sample Output](#sample-output)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Overview

This application enables users to upload documents (PDF, DOCX, TXT) and have them analyzed by a team of specialized AI agents. The agents work together to extract text, generate summaries, detect red flags, and extract key decisions from the document content.

The application runs entirely locally, ensuring document privacy and eliminating API costs. It uses Ollama to host the LLaMA 2 model, PyPDF2 and python-docx for document parsing, TinyDB for persistent storage, and Streamlit for the user interface.

---

## Features

- **Document Upload** — Supports PDF, DOCX, and TXT files
- **Text Extraction** — Automatically extracts text from uploaded documents
- **Multi-Agent Analysis** — Three specialized agents analyze the document
- **Summary Agent** — Generates concise document summaries
- **Red Flag Detector** — Identifies risks, concerns, and issues
- **Decision Extractor** — Extracts decisions, action items, and commitments
- **Export Ready** — Download analysis results
- **Privacy-Focused** — All processing happens locally, no data is sent to external servers
- **No API Costs** — Free to use with no usage limits

---

## The Agents

| Agent | Role | Responsibility |
|---|---|---|
| **Summary Agent** | Document Summarizer | Generates concise document summaries |
| **Red Flag Detector** | Risk Identifier | Detects risks, concerns, and red flags |
| **Decision Extractor** | Action Item Extractor | Extracts decisions, action items, and commitments |

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **LLaMA 2** | Large Language Model for document analysis |
| **Ollama** | Local LLM hosting and inference |
| **PyPDF2** | PDF text extraction |
| **python-docx** | DOCX text extraction |
| **TinyDB** | Lightweight JSON database for memory storage |
| **Streamlit** | Frontend user interface |
| **Requests** | HTTP client for API communication |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Python** | Version 3.8 or higher |
| **Ollama** | Installed and running |
| **LLaMA 2 Model** | Downloaded via Ollama |
| **RAM** | 8GB+ recommended |
| **Storage** | 4GB+ free space for model |

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Esha-Mirza/School_Of_AI_Internship.git
cd School_Of_AI_Internship/"Project-17 Document Intelligence Workspace"
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Pull LLaMA 2 Model via Ollama

```bash
ollama pull llama2
```

This downloads the LLaMA 2 model (~3.8 GB). Alternatively, you can use a smaller model:

```bash
ollama pull phi3        # 2.2 GB, faster inference
ollama pull gemma:2b    # 1.4 GB, lightest option
```

---

## Running the Application

**Terminal 1: Start Ollama Service**

```bash
ollama serve
```

**Terminal 2: Start Backend (FastAPI)**

```bash
uvicorn backend.main:app --reload
```

The backend will be available at: `http://localhost:8000`

**Terminal 3: Start Frontend (Streamlit)**

```bash
streamlit run frontend/app.py
```

The frontend will open at: `http://localhost:8501`

---

## Usage

1. Open your browser and navigate to `http://localhost:8501`
2. Create a new topic or select an existing one
3. Upload a document (PDF, DOCX, or TXT)
4. Click the **Analyze Document** button
5. View the results from all three agents

---

## Supported Document Formats

| Format | Extension | Library Used |
|---|---|---|
| PDF | `.pdf` | PyPDF2 |
| Word | `.docx` | python-docx |
| Text | `.txt` | Built-in |

---

## Sample Document (TXT)

```text
PROJECT STATUS REPORT

Project: AI Implementation
Date: January 15, 2024

Summary:
The AI project is currently in Phase 2. We have completed the data collection phase and are now in model development.

Risks:
- Budget overruns expected
- Delays in data processing

Decisions:
- Hire two additional data scientists
- Extend project timeline by 2 weeks
```

---

## Sample Output

**Summary Agent:**

```text
The AI project is in Phase 2 with data collection complete and model development underway. Budget overruns and data processing delays are the main risks. Two additional data scientists will be hired, and the project timeline will be extended by 2 weeks.
```

**Red Flag Detector:**

```text
Risk: Budget overruns expected
Risk: Delays in data processing

Recommendations:
- Review budget allocation
- Optimize data processing pipeline
- Consider additional resources
```

**Decision Extractor:**

```text
Decisions/Action Items:
1. Hire two additional data scientists (Immediate)
2. Extend project timeline by 2 weeks
3. Review budget allocation
```

---

## API Endpoints

### `POST /analyze/`

**Request:**

```json
{
  "text": "Document text content..."
}
```

**Response:**

```json
{
  "summary": "Document summary...",
  "red_flags": "Identified risks...",
  "decisions": "Extracted decisions..."
}
```

---

## Project Structure

```
Project-17 Document Intelligence Workspace/
├── backend/
│   └── main.py          # FastAPI implementation
├── frontend/
│   └── app.py           # Streamlit UI
├── agents/
│   ├── __init__.py
│   ├── base.py
│   ├── document_agent.py
│   ├── research_agent.py
│   ├── summarizer_agent.py
│   ├── devil_agent.py
│   └── insight_agent.py
├── memory/
│   ├── .gitkeep
│   └── memory_store.json
├── requirements.txt
└── README.md
```

---

## Configuration

### Changing the Model

To use a different model, modify `agents/base.py`:

```python
MODEL = "phi3"        # Change from "llama2" to your preferred model
```

### Changing the Port

**Backend Port** (default: 8000):

```bash
uvicorn backend.main:app --reload --port 8001
```

**Frontend Port** (default: 8501):

```bash
streamlit run frontend/app.py --server.port 8502
```

---

## Troubleshooting

| Issue | Solution |
|---|---|
| Model not found | Run `ollama pull llama2` to download the model |
| Connection refused | Ensure Ollama is running (`ollama serve`) |
| PDF parsing error | Ensure the PDF is not password-protected |
| DOCX parsing error | Ensure the DOCX file is not corrupted |
| File size limit | Try with smaller files (< 5MB) |
| Port already in use | Use `--port` flag to specify a different port |
| Module not found | Run `pip install -r requirements.txt` |
| Slow inference | Switch to a smaller model like `phi3` or `gemma:2b` |

---

## Roadmap

- [ ] Add support for scanned/image-based PDFs via OCR
- [ ] Add cross-document comparison (analyze multiple related documents together)
- [ ] Add exportable analysis report (PDF/DOCX)

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Acknowledgments

- [Ollama](https://ollama.com/) - Local LLM runtime
- PyPDF2 - PDF parsing
- python-docx - DOCX parsing
- FastAPI - Web framework
- Streamlit - UI framework

---

## Contact

- **GitHub:** [Esha-Mirza](https://github.com/Esha-Mirza)
- **Email:** esha101374@gmail.com
