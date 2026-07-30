# Text Summarizer AI

An AI-powered text summarization application that uses a locally hosted LLaMA model to generate concise summaries from long-form text.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Ollama](https://img.shields.io/badge/LLM-Ollama-black)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)
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

This application leverages Large Language Models (LLMs) to automatically condense lengthy documents, articles, or transcripts into clear, concise summaries. It is designed for researchers, students, and professionals who need to quickly extract key information from large volumes of text.

The application runs entirely locally, ensuring data privacy and eliminating API costs. It uses Ollama to host the LLaMA model, FastAPI for the backend API, and Streamlit for the user interface.

---

## Features

- **Local LLM Inference** — Runs the LLaMA model locally using Ollama, ensuring complete data privacy
- **FastAPI Backend** — Provides a RESTful API for text summarization
- **Streamlit Frontend** — Clean, intuitive user interface
- **Real-time Processing** — Instant summarization with progress feedback
- **Privacy-Focused** — All processing happens locally, no data is sent to external servers
- **No API Costs** — Free to use with no usage limits

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **Ollama** | Local LLM hosting and inference |
| **LLaMA 2** | Large Language Model for text summarization |
| **FastAPI** | Backend API framework |
| **Streamlit** | Frontend user interface |
| **Requests** | HTTP client for API communication |
| **Uvicorn** | ASGI server for FastAPI |

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
cd School_Of_AI_Internship/"Project-1 Text Summarizer"
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

### 4. Pull LLaMA Model via Ollama

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
2. Paste the text you want to summarize in the input area
3. Click the **Summarize** button
4. Wait a few seconds for the AI to generate the summary
5. Review the generated summary

### Sample Input

```text
Artificial intelligence (AI) is rapidly transforming the healthcare industry in remarkable ways. AI-powered systems can now analyze medical images like X-rays and MRIs with accuracy that sometimes exceeds human experts, helping doctors detect diseases such as cancer at much earlier stages. Machine learning algorithms are being used to predict patient outcomes, identify individuals at high risk for certain diseases, and suggest personalized treatment plans based on a patient's unique genetic makeup and medical history. Despite these incredible advances, significant challenges remain, including concerns about patient data privacy, potential algorithmic bias, and the high costs of implementing these technologies in healthcare systems worldwide.
```

### Expected Output

```text
AI is transforming healthcare by enabling faster and more accurate diagnoses through medical image analysis and predictive algorithms. While AI helps doctors detect diseases early and personalize treatments, challenges such as data privacy, bias, and high implementation costs persist.
```

---

## API Endpoints

### `POST /summarize/`

**Request:**

```json
{
  "text": "Your text to summarize..."
}
```

**Response:**

```json
{
  "summary": "Generated summary text..."
}
```

---

## Project Structure

```
Project-1 Text Summarizer/
├── backend/
│   └── main.py          # FastAPI implementation
├── frontend/
│   └── app.py           # Streamlit UI
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## Configuration

### Changing the Model

To use a different model, modify `backend/main.py`:

```python
"model": "phi3",        # Change from "llama2" to your preferred model
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
| Port already in use | Use `--port` flag to specify a different port |
| Module not found | Run `pip install -r requirements.txt` |
| Slow inference | Switch to a smaller model like `phi3` or `gemma:2b` |

---

## Roadmap

- [ ] Add support for file uploads (PDF, DOCX) instead of pasted text only
- [ ] Add adjustable summary length (short/medium/long)
- [ ] Add multi-language summarization support

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Acknowledgments

- [Ollama](https://ollama.com/) - Local LLM runtime
- Meta - LLaMA 2
- FastAPI - Web framework
- Streamlit - UI framework

---

## Contact

- **GitHub:** [Esha-Mirza](https://github.com/Esha-Mirza)
- **Email:** esha101374@gmail.com
