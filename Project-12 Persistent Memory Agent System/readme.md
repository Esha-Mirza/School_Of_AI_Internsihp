# Persistent Memory Agent System

An AI assistant with long-term memory that maintains context across topics and sessions, allowing users to resume research where they left off.

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
- [Sample Workflow](#sample-workflow)
- [Memory Log Display](#memory-log-display)
- [Project Structure](#project-structure)
- [How Memory Works](#how-memory-works)
- [Memory Storage Format (TinyDB)](#memory-storage-format-tinydb)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Overview

This application introduces persistent memory to AI conversations. Unlike traditional chatbots that lose context between sessions, this system remembers everything you discuss, organized by topic. It is designed for researchers, students, and professionals who need to maintain continuity in their work.

The application runs entirely locally, ensuring data privacy and eliminating API costs. It uses Ollama to host the LLaMA 2 model, TinyDB for lightweight persistent storage, and Streamlit for the user interface.

---

## Features

- **Persistent Memory** — Remembers everything you discuss across sessions
- **Topic-Based Organization** — Separate memory for each research topic
- **Conversation History** — Full chat history per topic
- **Context-Aware Responses** — AI uses past conversations for better responses
- **Resume Anywhere** — Pick up where you left off anytime
- **Export Ready** — Download memory logs
- **Privacy-Focused** — All processing happens locally, no data is sent to external servers
- **No API Costs** — Free to use with no usage limits

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **LLaMA 2** | Large Language Model for conversation |
| **Ollama** | Local LLM hosting and inference |
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
cd School_Of_AI_Internship/"Project-12 Persistent Memory Agent System"
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
2. Create a new topic or select an existing one
3. Ask a question or add a research note
4. AI responds with context from previous conversations
5. Come back anytime — the AI remembers everything!

---

## Sample Workflow

**Session 1:**

```text
User: What are the latest trends in AI?
AI: The latest trends include generative AI, large language models, and multimodal systems...
```

**Session 2 (Next Day):**

```text
User: Tell me more about multimodal systems.
AI: As we discussed yesterday, multimodal systems combine text, image, and audio processing. Building on our conversation about generative AI...
```

---

## Memory Log Display

The application shows a chronological history of all interactions:

```text
📜 Topic Memory Log
You: What are the latest trends in AI?
AI: The latest trends include generative AI, large language models...
You: Tell me more about multimodal systems.
AI: As we discussed yesterday, multimodal systems combine...
```

---

## Project Structure

```
Project-12 Persistent Memory Agent System/
├── agents/
│   └── memory_agent.py   # Core memory agent
├── memory/
│   ├── .gitkeep
│   └── memory_store.json # Persistent memory storage
├── orchestrator.py        # Orchestration layer
├── frontend.py            # Streamlit UI
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## How Memory Works

```text
User Input
    │
    ▼
[Memory Agent] ──┬── Retrieve Topic History
                  │
                  ├── Build Context Prompt
                  │
                  ├── Generate AI Response
                  │
                  └── Store New Memory
    │
    ▼
Context-Aware Response
```

---

## Memory Storage Format (TinyDB)

```json
[
    {
        "name": "AI Research",
        "messages": [
            {
                "user": "What are the latest AI trends?",
                "ai": "The latest AI trends include generative AI..."
            },
            {
                "user": "Tell me more about transformers",
                "ai": "Transformers are neural network architectures..."
            }
        ]
    }
]
```

---

## Configuration

### Changing the Model

To use a different model, modify `agents/memory_agent.py`:

```python
MODEL = "phi3"        # Change from "llama2" to your preferred model
```

### Changing Memory Context Size

To control how much history is included in the context, modify `agents/memory_agent.py`:

```python
def get_memory_context(topic: str, max_messages: int = 10):
    # max_messages controls how many recent messages are included
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
| Memory not persisting | Check `memory/memory_store.json` exists |
| Port already in use | Use `--server.port` flag to specify a different port |
| Module not found | Run `pip install -r requirements.txt` |
| Slow inference | Switch to a smaller model like `phi3` or `gemma:2b` |

---

## Roadmap

- [ ] Add semantic search across memory (retrieve relevant past messages, not just recent ones)
- [ ] Add topic merging/renaming and memory cleanup tools
- [ ] Add memory summarization for long topics to reduce prompt size over time

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
