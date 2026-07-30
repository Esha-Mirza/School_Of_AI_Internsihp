# AI Tutor & Quiz Generator

An AI-powered tutor and quiz generator that simplifies educational content, generates quiz questions, and extracts key concepts for LearnSphere Academy.

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
- [Sample Lesson Content](#sample-lesson-content)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Sample Input](#sample-input)
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

This application helps educators and students by automating learning support. It simplifies complex material, generates quiz questions, and extracts key concepts for revision. It is designed for online courses, textbook content, and lecture notes.

The application runs entirely locally, ensuring data privacy and eliminating API costs. It uses Ollama to host the Mistral model, FastAPI for the backend API, and Streamlit for the user interface.

---

## Features

- **Student-Friendly Explanations** — Simplifies complex concepts with plain language
- **Quiz Generation** — Creates 5-question quizzes with answers
- **Key Concept Extraction** — Identifies 5-10 important terms with definitions
- **Multiple Difficulty Levels** — Easy, Medium, and Hard quiz options
- **Export Ready** — Download learning aids for study
- **Privacy-Focused** — All processing happens locally, no data is sent to external servers
- **No API Costs** — Free to use with no usage limits

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **Mistral** | Large Language Model for educational content processing |
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
cd School_Of_AI_Internship/"Project-10 AI Tutor & Quiz Generator"
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

## Sample Lesson Content

The project includes a sample lesson in `data/sample_lesson.txt`:

```text
PHOTOSYNTHESIS: THE PROCESS OF LIFE

Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize foods from carbon dioxide and water. This process generally involves the green pigment chlorophyll and generates oxygen as a by-product.

The photosynthesis equation is:
6CO₂ + 6H₂O + Light Energy → C₆H₁₂O₆ + 6O₂

Factors affecting photosynthesis include:
- Light intensity: Higher light intensity generally increases the rate of photosynthesis.
- Carbon dioxide concentration: Higher CO₂ levels lead to faster photosynthesis.
- Temperature: Photosynthesis works best at optimal temperatures (around 25°C to 30°C).
- Water availability: Water is essential for the process.

Photosynthesis is crucial for life on Earth because:
- It produces oxygen for animals to breathe.
- It provides food (glucose) for plants and the animals that eat them.
- It reduces carbon dioxide in the atmosphere, helping to regulate climate.
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
2. Paste educational content in the text area
3. Click the **Generate Learning Aids** button
4. View the results in three tabs:
   - **Simplified Explanation** — Student-friendly explanation
   - **Quiz** — 5 questions with answers
   - **Key Concepts** — 5-10 important terms with definitions

---

## Sample Input

```text
Photosynthesis is the process by which green plants use sunlight to synthesize foods from carbon dioxide and water. It involves chlorophyll and generates oxygen as a by-product.
```

---

## Sample Output

**Simplified Explanation:**

```text
Photosynthesis is how plants make their own food. They use sunlight, water, and carbon dioxide to create glucose (sugar) and oxygen. Think of it like a kitchen where plants cook their own meals using energy from the sun!
```

**Quiz:**

```text
Q1: What is photosynthesis?
A) The process of plants making food
B) The process of animals breathing
C) The process of water evaporating
D) The process of rocks forming
Answer: A - Plants use sunlight to make food.

Q2: What gas do plants release during photosynthesis?
A) Carbon dioxide
B) Oxygen
C) Nitrogen
D) Hydrogen
Answer: B - Plants release oxygen as a by-product.
```

**Key Concepts:**

```text
1. Photosynthesis: The process by which plants make food using sunlight.
2. Chlorophyll: The green pigment in plants that captures sunlight.
3. Glucose: The sugar that plants produce as food.
4. Oxygen: The gas released by plants during photosynthesis.
5. Carbon Dioxide: The gas plants absorb from the air.
```

---

## API Endpoints

### `POST /generate/`

**Request:**

```json
{
  "text": "Your educational content..."
}
```

**Response:**

```json
{
  "explanation": "Simplified explanation...",
  "quiz": "Generated quiz with answers...",
  "concepts": "Key concepts with definitions..."
}
```

---

## Project Structure

```
Project-10 AI Tutor & Quiz Generator/
├── backend/
│   └── main.py          # FastAPI implementation
├── frontend/
│   └── app.py           # Streamlit UI
├── data/
│   └── sample_lesson.txt
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

### Changing the Quiz Difficulty

To adjust quiz difficulty, modify the prompt in `backend/main.py`:

```python
quiz_prompt = (
    "Generate 5 quiz questions at MEDIUM difficulty level with answers..."
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
| Model not found | Run `ollama pull mistral` to download the model |
| Connection refused | Ensure Ollama is running (`ollama serve`) |
| Port already in use | Use `--port` flag to specify a different port |
| Module not found | Run `pip install -r requirements.txt` |
| Slow inference | Switch to a smaller model like `phi3` or `gemma:2b` |
| No quiz generated | Ensure the content is educational and has sufficient detail |

---

## Roadmap

- [ ] Add adjustable number of quiz questions (not fixed at 5)
- [ ] Add spaced-repetition flashcard export for key concepts
- [ ] Add support for PDF/lecture-slide input instead of pasted text only

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
