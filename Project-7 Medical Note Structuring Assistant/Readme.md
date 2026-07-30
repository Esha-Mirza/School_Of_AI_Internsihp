# Medical Note Structuring Assistant

An AI-powered medical note structuring assistant that converts unstructured clinical notes into structured medical data for EMR integration and analytics.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Ollama](https://img.shields.io/badge/LLM-Ollama-black)

---

## Table of Contents

- [Overview](#overview)
- [Disclaimer](#disclaimer)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Sample Data](#sample-data)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Input CSV Format](#input-csv-format)
- [Sample Input](#sample-input)
- [Sample Output](#sample-output)
- [JSON Output Format](#json-output-format)
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

This application helps healthcare providers convert free-form clinical notes into structured, machine-readable data. It extracts key medical information — symptoms, diagnosis, medications, and follow-up instructions — from unstructured text, making it easier to integrate with Electronic Medical Record (EMR) systems and analytics platforms.

The application runs entirely locally, ensuring patient data privacy and eliminating API costs. It uses Ollama to host the LLaMA 2 model, FastAPI for the backend API, Pandas for data processing, and Streamlit for the user interface.

---

## Disclaimer

This project is an educational/portfolio demonstration and is **not a certified medical device or clinical tool**. It is not intended for use in real diagnosis, treatment decisions, or production EMR pipelines without proper validation, clinical oversight, and compliance review (e.g. HIPAA, GDPR, or other applicable healthcare data regulations). Always use synthetic or de-identified data when testing.

---

## Features

- **Symptoms Extraction** — Identifies patient-reported symptoms
- **Diagnosis Detection** — Extracts diagnosis or suspected diagnosis
- **Medication Extraction** — Lists all prescribed medications
- **Follow-up Instructions** — Extracts follow-up plans and timelines
- **Batch Processing** — Upload CSV files with multiple patient notes
- **Export Ready** — Download structured data as CSV or JSON
- **Consistent Schema** — Standardized output for EMR integration
- **Privacy-Focused** — All processing happens locally
- **No API Costs** — Free to use with no usage limits

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **LLaMA 2** | Large Language Model for medical text extraction |
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
| **LLaMA 2 Model** | Downloaded via Ollama |
| **RAM** | 8GB+ recommended |
| **Storage** | 4GB+ free space for model |

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Esha-Mirza/School_Of_AI_Internship.git
cd School_Of_AI_Internship/"Project-7 Medical Note Structuring"
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

## Sample Data

Create `data/example_notes.csv` with the following format:

```csv
patient_id,doctor_notes
001,"Patient complains of fatigue and joint pain. Diagnosed with rheumatoid arthritis. Prescribed methotrexate. Follow-up in 4 weeks."
002,"Severe cough and shortness of breath. Possible pneumonia. Started azithromycin. Chest X-ray recommended."
003,"Patient has type 2 diabetes. Blood sugar levels are high. Prescribed metformin. Diet and exercise advised. Follow-up in 2 weeks."
004,"Headaches and blurred vision for the past week. Suspected migraines. Prescribed sumatriptan. Keep a headache diary."
005,"Patient with hypertension. Blood pressure 150/95. Lisinopril 10mg prescribed. Check BP daily. Follow-up in 1 month."
```

> **Note:** This sample data is entirely fictional. Never use real patient information in demos, screenshots, or repos.

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
2. Upload a CSV file with clinical notes (see sample format above)
3. Click the **Extract Structured Data** button
4. View the structured medical data output

---

## Input CSV Format

| Column | Description |
|---|---|
| `patient_id` | Unique patient identifier |
| `doctor_notes` | Unstructured clinical notes |

---

## Sample Input

```csv
patient_id,doctor_notes
001,"Patient complains of fatigue and joint pain. Diagnosed with rheumatoid arthritis. Prescribed methotrexate. Follow-up in 4 weeks."
```

---

## Sample Output

| patient_id | symptoms | diagnosis | medications | follow_up |
|---|---|---|---|---|
| 001 | fatigue and joint pain | rheumatoid arthritis | methotrexate | Follow-up in 4 weeks |
| 002 | severe cough and shortness of breath | pneumonia | azithromycin | Chest X-ray recommended |

---

## JSON Output Format

```json
{
  "patient_id": "001",
  "symptoms": "fatigue and joint pain",
  "diagnosis": "rheumatoid arthritis",
  "medications": "methotrexate",
  "follow_up": "Follow-up in 4 weeks"
}
```

---

## API Endpoints

### `POST /extract/`

**Request:**

```json
{
  "note": "Your clinical note..."
}
```

**Response:**

```json
{
  "structured": {
    "symptoms": "fatigue and joint pain",
    "diagnosis": "rheumatoid arthritis",
    "medications": "methotrexate",
    "follow_up": "Follow-up in 4 weeks"
  }
}
```

---

## Project Structure

```
Project-7 Medical Note Structuring/
├── backend/
│   └── main.py          # FastAPI implementation
├── frontend/
│   └── app.py           # Streamlit UI
├── data/
│   └── example_notes.csv
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

### Changing the Prompt

To customize the extraction, modify the prompt in `backend/main.py`:

```python
prompt = (
    "Extract the following from the doctor's note:\n"
    "- Symptoms\n"
    "- Diagnosis\n"
    "- Medications\n"
    "- Follow-up Instructions\n\n"
    "Return the output in valid JSON format.\n\n"
    f"Doctor's Note:\n{note}"
)
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
| CSV format error | Check columns: `patient_id`, `doctor_notes` |
| JSON parsing error | Ensure the prompt returns valid JSON |
| Port already in use | Use `--port` flag to specify a different port |
| Module not found | Run `pip install -r requirements.txt` |
| Slow inference | Switch to a smaller model like `phi3` or `gemma:2b` |

---

## Roadmap

- [ ] Add ICD-10 code mapping for extracted diagnoses
- [ ] Add validation/confidence scoring per extracted field
- [ ] Add FHIR-compatible export format for real EMR interoperability

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Acknowledgments

- [Ollama](https://ollama.com/) - Local LLM runtime
- Meta - LLaMA 2 model
- FastAPI - Web framework
- Streamlit - UI framework
- Pandas - Data processing

---

## Contact

- **GitHub:** [Esha-Mirza](https://github.com/Esha-Mirza)
- **Email:** esha101374@gmail.com
