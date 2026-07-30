# Product Review Analyzer AI

An AI-powered product review analyzer that extracts sentiment, key topics, and concise summaries from customer reviews for business intelligence.

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
- [Input CSV Format](#input-csv-format)
- [Sample Output](#sample-output)
- [Dashboard Visualizations](#dashboard-visualizations)
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

This application analyzes customer product reviews to extract actionable insights for businesses. It classifies sentiment, identifies key topics, and generates concise summaries to help marketing, customer support, and logistics teams make data-driven decisions.

The application runs entirely locally, ensuring data privacy and eliminating API costs. It uses Ollama to host the Mistral model, FastAPI for the backend API, Pandas for data processing, and Streamlit for the user interface.

---

## Features

- **Sentiment Classification** — Identifies Positive, Neutral, or Negative sentiment
- **Topic Detection** — Extracts key issues (delivery, quality, pricing, etc.)
- **Concise Summaries** — Generates one-line summaries per review
- **Batch Processing** — Upload CSV files with multiple reviews
- **Interactive Dashboard** — Visual charts and metrics
- **Downloadable Insights** — Export results as CSV
- **Privacy-Focused** — All processing happens locally
- **No API Costs** — Free to use with no usage limits

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **Mistral** | Large Language Model for analysis |
| **Ollama** | Local LLM hosting and inference |
| **FastAPI** | Backend API framework |
| **Streamlit** | Frontend user interface |
| **Pandas** | Data processing and CSV handling |
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
cd School_Of_AI_Internship/"Project-6 Product Review Analyzer"
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

Create `data/sample_reviews.csv` with the following format:

```csv
product_id,product_name,review_text
101,Bluetooth Speaker,"The sound quality is great but delivery was slow."
102,Yoga Mat,"Arrived early. Good quality material!"
103,Wireless Headphones,"Battery life is terrible. Lasts only 2 hours."
104,Coffee Maker,"Makes perfect coffee every morning. Love it!"
105,Running Shoes,"Very comfortable but size runs small. Had to return."
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
2. Upload a CSV file with product reviews (see sample format above)
3. Click the **Analyze Reviews** button
4. View the interactive dashboard with results

---

## Input CSV Format

| Column | Description |
|---|---|
| `product_id` | Unique product identifier |
| `product_name` | Name of the product |
| `review_text` | Customer review text |

---

## Sample Output

| product_name | review_text | sentiment | topic | summary |
|---|---|---|---|---|
| Bluetooth Speaker | The sound quality is great but delivery was slow. | Positive | Delivery | Great sound, but slow delivery |
| Yoga Mat | Arrived early. Good quality material! | Positive | Product Quality | Early arrival and good quality |
| Wireless Headphones | Battery life is terrible. Lasts only 2 hours. | Negative | Battery Life | Poor battery performance |

---

## Dashboard Visualizations

- **Sentiment Distribution** — Bar chart of Positive/Neutral/Negative counts
- **Top Topics** — Bar chart of most common issues
- **Metrics** — Total reviews, positive count, negative count

---

## API Endpoints

### `POST /analyze/`

**Request:**

```json
{
  "text": "Your review text..."
}
```

**Response:**

```json
{
  "sentiment": "Positive",
  "topic": "Product Quality",
  "summary": "Concise one-line summary..."
}
```

---

## Project Structure

```
Project-6 Product Review Analyzer/
├── backend/
│   └── main.py          # FastAPI implementation
├── frontend/
│   └── app.py           # Streamlit UI
├── data/
│   └── sample_reviews.csv
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
| CSV format error | Check columns: `product_id`, `product_name`, `review_text` |
| Port already in use | Use `--port` flag to specify a different port |
| Module not found | Run `pip install -r requirements.txt` |
| Slow inference | Switch to a smaller model like `phi3` or `gemma:2b` |

---

## Roadmap

- [ ] Add support for direct integration with review platforms (Amazon, Shopify exports)
- [ ] Add trend charts to track sentiment over time
- [ ] Add automatic alerting for spikes in negative sentiment

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Acknowledgments

- [Ollama](https://ollama.com/) - Local LLM runtime
- Mistral AI - Mistral model
- FastAPI - Web framework
- Streamlit - UI framework
- Pandas - Data processing

---

## Contact

- **GitHub:** [Esha-Mirza](https://github.com/Esha-Mirza)
- **Email:** esha101374@gmail.com
