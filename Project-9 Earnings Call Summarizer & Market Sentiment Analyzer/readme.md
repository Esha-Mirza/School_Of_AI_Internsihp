# Earnings Call Analyzer

An AI-powered earnings call analyzer that extracts summaries, sentiment, and key financial insights from quarterly earnings call transcripts for FinScope Capital.

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
- [Sample Data](#sample-data)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Sample Input](#sample-input-short)
- [Sample Output](#sample-output)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [License](#license)
- [Disclaimer](#disclaimer)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Overview

This application helps investment research firms and financial analysts quickly analyze earnings call transcripts. It automatically generates concise summaries, classifies overall sentiment, and extracts key financial insights including revenue trends, growth signals, risk warnings, and forward guidance.

The application runs entirely locally, ensuring data privacy and eliminating API costs. It uses Ollama to host the Mistral model, FastAPI for the backend API, and Streamlit for the user interface.

---

## Features

- **Earnings Call Summary** — Generates concise 3-sentence summaries of calls
- **Sentiment Classification** — Overall Positive / Neutral / Negative sentiment
- **Financial Insights** — Extracts revenue trends, growth signals, risks, and guidance
- **Analyst Q&A Support** — Handles CEO/CFO commentary and analyst questions
- **Export Ready** — Download analysis results for research reports
- **Privacy-Focused** — All processing happens locally, no data is sent to external servers
- **No API Costs** — Free to use with no usage limits

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **Mistral** | Large Language Model for financial text analysis |
| **Ollama** | Local LLM hosting and inference |
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
cd School_Of_AI_Internship/"Project-9 Earnings Call Summarizer"
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

## Sample Data

The project includes a sample transcript in `data/tesla_q4_2024.txt`:

```text
TESLA Q4 2024 EARNINGS CALL TRANSCRIPT
Date: January 29, 2025

[CEO - Elon Musk]: Good afternoon everyone. I'm pleased to report that we had a strong quarter with a 12% increase in vehicle deliveries compared to Q4 2023. We delivered a record 495,000 vehicles globally.

[CFO - Vaibhav Taneja]: Total revenue reached $25.7 billion, representing a 7% year-over-year growth. Operating income remained stable at $2.1 billion. We are investing heavily in AI-driven logistics.

[Analyst - John Smith]: Could you clarify how inflation is affecting your capital expenditures?

[CEO - Elon Musk]: We're maintaining our capital expenditure guidance of $9-10 billion for 2025. We expect vehicle deliveries to grow by 20-25% in 2025.
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
2. Paste an earnings call transcript in the text area or load the sample
3. Click the **Analyze** button
4. View the results:
   - **Summary** — 3-sentence call overview
   - **Sentiment** — Positive / Neutral / Negative with color coding
   - **Key Insights** — Revenue trends, growth signals, risks, guidance

---

## Sample Input (Short)

```text
[CEO]: We had a strong quarter with a 12% increase in revenue.
[Analyst]: Any concerns about the future?
[CEO]: We are optimistic about 2025 and expect continued growth.
```

---

## Sample Output

**Summary:**

```text
The company reported a strong quarter with 12% revenue growth. Management expressed optimism about 2025 and expects continued growth. The tone was positive throughout the call.
```

**Sentiment:** Positive (Green)

**Key Insights:**

```text
Revenue and Growth: 12% revenue increase
Forward Guidance: Optimistic about 2025 with expected continued growth
Risks: No significant risks mentioned
Strategic Initiatives: Focus on sustained growth
```

---

## API Endpoints

### `POST /analyze/`

**Request:**

```json
{
  "text": "Your earnings call transcript..."
}
```

**Response:**

```json
{
  "summary": "3-sentence summary...",
  "sentiment": "Positive",
  "insights": "Key financial insights..."
}
```

---

## Project Structure

```
Project-9 Earnings Call Summarizer/
├── backend/
│   └── main.py          # FastAPI implementation
├── frontend/
│   └── app.py           # Streamlit UI
├── data/
│   └── tesla_q4_2024.txt
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## Configuration

### Changing the Model

To use a different model, modify `backend/main.py`:

```python
MODEL = "phi3"        # Change from "mistral" to your preferred model
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

- [ ] Add multi-quarter trend comparison (QoQ / YoY insight tracking)
- [ ] Add speaker-level breakdown (separate CEO vs CFO vs analyst sentiment)
- [ ] Add PDF transcript upload support instead of pasted text only

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Disclaimer

**Educational/Prototype Use Only** — This tool is for research and demonstration purposes. It does not constitute financial advice, and its output should not be used as the sole basis for investment decisions. Always consult a qualified financial professional.

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
