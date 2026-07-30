# Agent-Guided Learning Coach

An AI-powered tutor system with specialized agents that support different learning functions — explaining concepts, generating quizzes, providing motivation, and tracking progress.

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
- [Sample Workflow](#sample-workflow)
- [Project Structure](#project-structure)
- [Agent Details](#agent-details)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Overview

This application acts as a personal AI tutor for students and lifelong learners. It uses four specialized agents to provide a complete learning experience: the Explainer Agent simplifies concepts, the Quiz Agent tests understanding, the Motivation Agent provides encouragement, and the Progress Agent tracks learning over time.

The application runs entirely locally, ensuring data privacy and eliminating API costs. It uses Ollama to host the LLaMA 2 model, TinyDB for persistent storage, and Streamlit for the user interface.

---

## Features

- **Concept Learning** — Explainer Agent simplifies complex concepts
- **Quiz Generation** — Quiz Agent creates questions to test understanding
- **Motivation** — Motivation Agent provides encouragement and study advice
- **Progress Tracking** — Progress Agent tracks learning and gives feedback
- **Memory per Subject** — Persistent learning history for each subject
- **Export Ready** — Download learning aids and progress reports
- **Privacy-Focused** — All processing happens locally
- **No API Costs** — Free to use with no usage limits

---

## The Agents

| Agent | Role | Responsibility |
|---|---|---|
| **Explainer Agent** | Concept Simplifier | Explains complex topics in simple language |
| **Quiz Agent** | Assessment Generator | Creates quiz questions with answers |
| **Motivation Agent** | Encouragement Coach | Provides motivation and study tips |
| **Progress Agent** | Learning Tracker | Tracks learning and gives feedback |

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **LLaMA 2** | Large Language Model for learning assistance |
| **Ollama** | Local LLM hosting and inference |
| **TinyDB** | Lightweight JSON database for progress tracking |
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
cd School_Of_AI_Internship/"Project-18 Agent-Guided Learning Coach"
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

**Terminal 2: Start Streamlit Frontend**

```bash
streamlit run frontend.py
```

The frontend will open at: `http://localhost:8501`

---

## Usage

1. Open your browser and navigate to `http://localhost:8501`
2. Create a new subject or select an existing one
3. Choose a learning activity:
   - **Learn** — Get concepts explained in simple language
   - **Quiz** — Test your understanding with generated questions
   - **Motivation** — Get encouragement and study advice
   - **Progress** — Track your learning journey

---

## Sample Workflow

**Step 1: Learn a Concept**

```text
User: Explain photosynthesis
Explainer Agent: Photosynthesis is how plants make their own food. Think of it like a kitchen where plants cook their meals using sunlight, water, and carbon dioxide...
```

**Step 2: Take a Quiz**

```text
Quiz Agent:
Q1: What is photosynthesis?
A) Plants making food using sunlight
B) Animals breathing
C) Water evaporating
Answer: A - Plants use sunlight to make food.
```

**Step 3: Get Motivation**

```text
Motivation Agent: Every expert was once a beginner. Keep going! 🌟
You're making great progress. Remember that small steps lead to big results!
```

**Step 4: Track Progress**

```text
Progress Agent:
Total Learning Interactions: 12
- Explainer Agent: 5 explanations
- Quiz Agent: 3 quizzes taken
- Motivation Agent: 2 motivation sessions
- Progress Agent: 2 progress checks

Learning Summary:
You've made good progress on understanding photosynthesis. You've learned the basics and can answer quiz questions correctly. Consider exploring more about cellular respiration next!
```

---

## Project Structure

```
Project-18 Agent-Guided Learning Coach/
├── agents/
│   ├── __init__.py
│   ├── base.py
│   ├── explainer_agent.py    # Explains concepts
│   ├── quiz_agent.py         # Generates quizzes
│   ├── motivation_agent.py   # Provides motivation
│   └── progress_agent.py     # Tracks progress
├── memory/
│   ├── .gitkeep
│   └── memory_store.json
├── orchestrator.py
├── frontend.py
├── requirements.txt
└── README.md
```

---

## Agent Details

### Explainer Agent

```python
Prompt: "Explain this concept in simple, student-friendly language..."
```

- Uses real-world examples and analogies
- Breaks down complex topics step-by-step
- Avoids technical jargon

### Quiz Agent

```python
Prompt: "Generate 5 quiz questions with answers..."
```

- Multiple difficulty levels (Easy, Medium, Hard)
- Mix of multiple-choice and short-answer questions
- Includes answer explanations

### Motivation Agent

```python
Prompt: "Provide encouragement and practical learning advice..."
```

- Personalized based on student's progress
- Includes inspiring quotes
- Offers practical study tips

### Progress Agent

```python
Prompt: "Analyze learning progress and provide feedback..."
```

- Summarizes what has been learned
- Identifies strengths and areas for improvement
- Recommends next steps

---

## Configuration

### Changing the Model

To use a different model, modify `agents/base.py`:

```python
MODEL = "phi3"        # Change from "llama2" to your preferred model
```

### Changing Quiz Difficulty

To adjust quiz difficulty, modify the prompt in `agents/quiz_agent.py`:

```python
prompt = f"Generate {level} difficulty quiz questions..."
```

### Changing the Port

```bash
streamlit run frontend.py --server.port 8502
```

---

## Troubleshooting

| Issue | Solution |
|---|---|
| Model not found | Run `ollama pull llama2` to download the model |
| Connection refused | Ensure Ollama is running (`ollama serve`) |
| No progress data | Use the app to learn and take quizzes first |
| Port already in use | Use `--server.port` flag to specify a different port |
| Module not found | Run `pip install -r requirements.txt` |
| Slow inference | Switch to a smaller model like `phi3` or `gemma:2b` |

---

## Roadmap

- [ ] Add spaced-repetition scheduling to resurface weaker topics
- [ ] Add multi-subject dashboard comparing progress across subjects
- [ ] Add adaptive difficulty (auto-adjust quiz level based on performance)

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Acknowledgments

- [Ollama](https://ollama.com/) - Local LLM runtime
- TinyDB - Lightweight database
- Streamlit - UI framework

---

## Contact

- **GitHub:** [Esha-Mirza](https://github.com/Esha-Mirza)
- **Email:** esha101374@gmail.com
