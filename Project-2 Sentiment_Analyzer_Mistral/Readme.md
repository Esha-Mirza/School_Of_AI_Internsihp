# Sentiment Analyzer AI

An AI-powered sentiment analysis application that uses a locally hosted Mistral model to classify text as Positive, Negative, or Neutral.

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

This application leverages Large Language Models (LLMs) to automatically analyze the sentiment of customer reviews, social media posts, survey responses, and other text data. It is designed for businesses, researchers, and individuals who need to understand public opinion and customer feedback at scale.

The application runs entirely locally, ensuring data privacy and eliminating API costs. It uses Ollama to host the Mistral model, FastAPI for the backend API, and Streamlit for the user interface.

---

## Features

- **Sentiment Classification** — Classifies text as Positive, Negative, or Neutral
- **Local LLM Inference** — Runs the Mistral model locally using Ollama, ensuring complete data privacy
- **FastAPI Backend** — Provides a RESTful API for sentiment analysis
- **Streamlit Frontend** — Clean, intuitive user interface with color-coded results
- **Color-Coded Results** — Visual feedback with Green (Positive), Red (Negative), and Yellow (Neutral)
- **Privacy-Focused** — All processing happens locally, no data is sent to external servers
- **No API Costs** — Free to use with no usage limits

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **Ollama** | Local LLM hosting and inference |
| **Mistral** | Large Language Model for sentiment analysis |
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
| **Mistral Model** | Downloaded via Ollama |
| **RAM** | 8GB+ recommended |
| **Storage** | 5GB+ free space for model |

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Esha-Mirza/School_Of_AI_Internship.git
cd School_Of_AI_Internship/"Project-2 Sentiment_Anayzer_Mistral"
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

### 4. Pull Mistral Model via Ollama

```bash
ollama pull mistral
```

This downloads the Mistral model (~4.1 GB). Alternatively, you can use a smaller model:

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
2. Paste the text you want to analyze in the input area
3. Click the **Analyze** button
4. View the predicted sentiment with color coding

### Sample Input (Positive)

```text
I absolutely love this product! It has completely changed my life for the better. The quality is outstanding and the customer service was amazing. I would definitely recommend it to everyone!
```

**Expected Output:** ✅ Positive (Green)

### Sample Input (Negative)

```text
The service was terrible. The staff was rude and unhelpful. I waited over an hour for my order. Never coming back here again!
```

**Expected Output:** ❌ Negative (Red)

### Sample Input (Neutral)

```text
The movie started at 7 PM and lasted for two hours. The theater was about half full.
```

**Expected Output:** ⚖️ Neutral (Yellow)

---

## API Endpoints

### `POST /analyze/`

**Request:**

```json
{
  "text": "Your text to analyze..."
}
```

**Response:**

```json
{
  "sentiment": "Positive"
}
```

---

## Project Structure

```
Project-2 Sentiment_Anayzer_Mistral/
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
"model": "phi3",        # Change from "mistral" to your preferred model
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
| Model not found | Run `ollama pull mistral` to download the model |
| Connection refused | Ensure Ollama is running (`ollama serve`) |
| Port already in use | Use `--port` flag to specify a different port |
| Module not found | Run `pip install -r requirements.txt` |
| Slow inference | Switch to a smaller model like `phi3` or `gemma:2b` |

---

## Roadmap

- [ ] Add confidence scores alongside the sentiment label
- [ ] Support batch analysis via CSV upload
- [ ] Add sentiment trend visualization over time (using Plotly)

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Acknowledgments

- [Ollama](https://ollama.com/) - Local LLM runtime
- Mistral AI - Mistral model
- FastAPI - Web framework
- Streamlit - UI framework

---

## Contact

- **GitHub:** [Esha-Mirza](https://github.com/Esha-Mirza)
- **Email:** esha101374@gmail.com
