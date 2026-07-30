# School of AI Internship - Complete Project Portfolio

A comprehensive collection of 25 AI/ML projects completed during my AI internship. Each project demonstrates practical applications of Large Language Models (LLMs), multi-agent systems, and modern AI development tools.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Ollama](https://img.shields.io/badge/LLM-Ollama-black)

---

## Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Project Categories](#project-categories)
- [Technology Stack](#technology-stack)
- [Project Overview](#project-overview)
- [Model Requirements](#model-requirements)
- [Installation Guide](#installation-guide)
- [Project Structure](#project-structure)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Overview

This repository showcases 25 AI-powered applications built during my School of AI Internship. Each project addresses a specific real-world problem across diverse domains including healthcare, finance, education, security, and legal tech.

All projects are designed to run locally using Ollama for LLM inference, with FastAPI backends and Streamlit frontends.

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/Esha-Mirza/School_Of_AI_Internship.git
cd School_Of_AI_Internship

# Navigate to any project directory
cd "Project-1 Text Summarizer"

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Pull the required Ollama model
ollama pull llama2

# Start the application
streamlit run frontend/app.py
```

Each project directory contains its own README with specific setup instructions.

---

## Project Categories

### Natural Language Processing & Text Analysis
- **Text Summarizer** — Summarize long documents and articles
- **Sentiment Analyzer** — Classify text as Positive, Neutral, or Negative
- **Meeting Notes Generator** — Transcribe and summarize meeting audio
- **Product Review Analyzer** — Analyze customer reviews with sentiment and topic extraction

### Healthcare & Medical Applications
- **Medical Note Structuring** — Convert unstructured clinical notes into structured EMR-ready data
- **Mental Health Companion** — Journaling and emotional well-being support

### Legal & Compliance
- **Legal Document Analyzer** — Extract clauses, entities, and summaries from legal documents
- **Grant Proposal Assistant** — Draft and refine grant proposals

### Business & Finance
- **Earnings Call Analyzer** — Extract insights from financial transcripts
- **Agile Standup Tracker** — Asynchronous team standup management

### Multi-Agent Systems
- **Multi-Agent Research Assistant** — Collaborative research with specialized agents
- **AthenaCore** — Multi-agent system with shared persistent memory
- **Visual Timeline** — Agent collaboration visualization
- **Voice-Controlled Agent** — Voice-enabled multi-agent interaction
- **Scheduled Workflow** — Automated agent runs with scheduling
- **Document Intelligence** — Collaborative document analysis

### Education & Learning
- **AI Tutor & Quiz Generator** — Educational content simplification and assessment
- **Agent-Guided Learning Coach** — Personalized tutoring system
- **Academic Research Collaborator** — Research assistance for scholars

### Developer Tools
- **Code Review Assistant** — Code analysis, bug detection, and optimization
- **Resume & Interview Coach** — Career preparation and job application support

### Other Domains
- **Image Caption Generator** — Vision-language model for image description
- **Travel Planning Assistant** — AI-powered trip planning
- **Cybersecurity Incident Agent** — Security operations and incident response

---

## Technology Stack

### Core Technologies

| Technology | Purpose |
|---|---|
| Ollama | Local LLM hosting and inference |
| FastAPI | Backend API development |
| Streamlit | Frontend UI development |
| TinyDB | Lightweight JSON database |
| Pandas | Data processing and analysis |
| Plotly | Interactive visualizations |

### LLM Models

| Model | Projects | Size | RAM Required |
|---|---|---|---|
| LLaMA 2 | 1, 5, 7, 8, 11-25 | 3.8 GB | 8+ GB |
| Mistral | 2, 6, 9, 10 | 4.1 GB | 8+ GB |
| LLaVA | 3 | 4.5 GB | 8+ GB |
| DeepSeek-Coder | 4 | 3.8 GB | 8+ GB |
| Gemma:2b | 1 (alternative) | 1.4 GB | 4+ GB |
| Phi-3 | 2, 4, 5 (alternatives) | 2.2 GB | 4+ GB |
| Whisper | 5, 15 | ~1 GB | 4+ GB |

### Specialized Libraries

| Library | Purpose | Projects |
|---|---|---|
| PyPDF2 | PDF text extraction | 17 |
| python-docx | DOCX text extraction | 17 |
| openai-whisper | Speech-to-text transcription | 5, 15 |
| pyttsx3 | Text-to-speech synthesis | 15 |
| sounddevice | Audio recording | 15 |
| pydub | Audio processing and conversion | 5, 15 |
| APScheduler | Task scheduling | 16 |

---

## Project Overview

| # | Project Name | Category | Key Technologies |
|---|---|---|---|
| 1 | Text Summarizer | NLP | LLaMA 2, FastAPI, Streamlit |
| 2 | Sentiment Analyzer | NLP | Mistral, FastAPI, Streamlit |
| 3 | Image Caption Generator | Vision | LLaVA, FastAPI, Streamlit, Pillow |
| 4 | Code Review Assistant | Developer Tools | DeepSeek-Coder, FastAPI, Streamlit |
| 5 | Meeting Notes Generator | Audio | Whisper, LLaMA 2, FastAPI, FFmpeg |
| 6 | Product Review Analyzer | Business Intelligence | Mistral, FastAPI, Streamlit, Pandas |
| 7 | Medical Note Structuring | Healthcare | LLaMA 2, FastAPI, Streamlit |
| 8 | Legal Document Analyzer | Legal Tech | LLaMA 2, FastAPI, Streamlit |
| 9 | Earnings Call Analyzer | Finance | Mistral, FastAPI, Streamlit |
| 10 | AI Tutor & Quiz Generator | Education | Mistral, FastAPI, Streamlit |
| 11 | Multi-Agent Research Assistant | Multi-Agent | LLaMA 2, Streamlit |
| 12 | Persistent Memory Agent | Memory Systems | LLaMA 2, TinyDB, Streamlit |
| 13 | AthenaCore | Multi-Agent | LLaMA 2, TinyDB, Streamlit |
| 14 | Visual Timeline | Visualization | LLaMA 2, Plotly, Streamlit |
| 15 | Voice-Controlled Agent | Voice AI | Whisper, pyttsx3, Streamlit |
| 16 | Scheduled Agent Workflow | Automation | APScheduler, Streamlit |
| 17 | Document Intelligence | Document Processing | PyPDF2, python-docx, Streamlit |
| 18 | Agent-Guided Learning Coach | Education | LLaMA 2, Streamlit |
| 19 | Cybersecurity Incident Agent | Security | LLaMA 2, Streamlit |
| 20 | Mental Health Companion | Health Tech | LLaMA 2, Streamlit |
| 21 | Travel Planning Assistant | Travel | LLaMA 2, Streamlit |
| 22 | Agile Standup Tracker | Project Management | LLaMA 2, Streamlit |
| 23 | Grant Proposal Assistant | Research | LLaMA 2, Streamlit |
| 24 | Resume & Interview Coach | Career | LLaMA 2, Streamlit |
| 25 | Academic Research Collaborator | Academia | LLaMA 2, Streamlit |

---

## Model Requirements

### Essential Models

Pull these models to run the majority of projects:

```bash
# Core models
ollama pull llama2
ollama pull mistral
ollama pull phi3

# Vision model
ollama pull llava

# Code model
ollama pull deepseek-coder
```

### Project-Specific Requirements

| Model | Required For |
|---|---|
| llama2 | Projects 1, 5, 7, 8, 11-25 |
| mistral | Projects 2, 6, 9, 10 |
| phi3 | Faster alternative for projects 2, 4, 5 |
| llava | Project 3 |
| deepseek-coder | Project 4 |
| whisper | Projects 5, 15 |

---

## Installation Guide

### Prerequisites

- Python 3.8 or higher
- Ollama installed and running
- Git installed
- 8GB+ RAM recommended
- 20GB+ free disk space for all models

### General Project Setup

```bash
# Navigate to any project
cd "Project-XX_ProjectName"

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Pull required Ollama model
ollama pull llama2

# Start the application
streamlit run frontend/app.py
```

---

## Project Structure

Each project follows a consistent structure:

```
Project-XX_ProjectName/
├── backend/
│   └── main.py
├── frontend/
│   └── app.py
├── agents/
├── memory/
├── requirements.txt
└── README.md
```

---

## License

This repository is open source and available under the [MIT License](LICENSE).

---

## Acknowledgments

- [Ollama](https://ollama.com/) - Local LLM runtime
- Meta - LLaMA 2
- Mistral AI - Mistral model
- OpenAI - Whisper
- FastAPI - Web framework
- Streamlit - UI framework

---

## Contact

- **GitHub:** [Esha-Mirza](https://github.com/Esha-Mirza)
- **Email:** esha101374@gmail.com
