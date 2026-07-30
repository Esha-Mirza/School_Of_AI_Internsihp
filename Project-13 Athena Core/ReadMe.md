# AthenaCore: Collaborative Multi-Agent Memory System

A collaborative AI system where multiple autonomous agents share and evolve topic-specific memory over time for Athena Research Group.

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
- [Shared Memory Log](#shared-memory-log)
- [Project Structure](#project-structure)
- [Agent Collaboration Flow](#agent-collaboration-flow)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Overview

AthenaCore is a think tank-style research system where specialized AI agents collaborate on long-term strategic topics. Instead of a single AI assistant, it uses a team of agents — Research, Summarizer, Devil's Advocate, and Insight — that read from and write to a shared, evolving memory.

The application runs entirely locally, ensuring data privacy and eliminating API costs. It uses Ollama to host the LLaMA 2 model, TinyDB for persistent shared memory, and Streamlit for the user interface.

---

## Features

- **Multi-Agent Collaboration** — Specialized agents work together on the same topic
- **Shared Persistent Memory** — All agents read from and write to the same memory
- **Specialized Roles** — Each agent has a unique function
- **Session Continuity** — Memory persists across sessions
- **Full Contribution Timeline** — Review all agent outputs
- **Export Ready** — Download memory logs
- **Privacy-Focused** — All processing happens locally
- **No API Costs** — Free to use with no usage limits

---

## The Agents

| Agent | Role | Responsibility |
|---|---|---|
| **Research Agent** | Information Collector | Answers factual questions and gathers context |
| **Summarizer Agent** | Insight Extractor | Condenses knowledge into bullet summaries |
| **Devil's Advocate Agent** | Critical Thinker | Challenges assumptions and raises risks |
| **Insight Agent** | Strategic Analyst | Extracts key takeaways and implications |

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **LLaMA 2** | Large Language Model for agent reasoning |
| **Ollama** | Local LLM hosting and inference |
| **TinyDB** | Lightweight JSON database for shared memory |
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
cd School_Of_AI_Internship/"Project-13 Athena Core"
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
3. Select an agent to run:
   - **Research** — Ask a factual question
   - **Summarizer** — Condense all knowledge on the topic
   - **Devil's Advocate** — Challenge assumptions and raise risks
   - **Insight** — Extract strategic takeaways
4. Each agent reads from and writes to the shared memory

---

## Sample Workflow

**Topic:** "AI Global Regulation"

**Step 1: Research Agent**

```text
User Query: What are the current EU AI regulations?
Research Agent: The EU AI Act categorizes AI systems by risk level...
```

**Step 2: Summarizer Agent**

```text
Summarizer Agent: • EU AI Act categorizes AI by risk
• High-risk systems face strict requirements
• Implementation timeline: 2024-2026
```

**Step 3: Devil's Advocate Agent**

```text
Devil's Advocate: • How will enforcement work?
• What about non-EU companies?
• Are there implementation gaps?
```

**Step 4: Insight Agent**

```text
Insight Agent: • Companies need compliance strategies by 2025
• Regulatory divergence with US and China
• Opportunity for AI governance frameworks
```

---

## Shared Memory Log

All agents contribute to a shared log:

```text
📜 Shared Topic Log
Research Agent: EU AI Act categorizes AI systems by risk level...
Summarizer Agent: • EU AI Act categorizes AI by risk...
Devil's Advocate: How will enforcement work?...
Insight Agent: Companies need compliance strategies by 2025...
```

---

## Project Structure

```
Project-13 Athena Core/
├── agents/
│   ├── __init__.py
│   ├── base.py
│   ├── research_agent.py
│   ├── summarizer_agent.py
│   ├── devil_agent.py
│   └── insight_agent.py
├── memory/
│   ├── .gitkeep
│   └── memory_store.json
├── orchestrator.py
├── frontend.py
├── requirements.txt
└── README.md
```

---

## Agent Collaboration Flow

```text
User Input (Topic)
    │
    ▼
[Research Agent] → Factual Answers
    │
    ▼
[Summarizer Agent] → Condensed Summary
    │
    ▼
[Devil's Advocate] → Challenges & Risks
    │
    ▼
[Insight Agent] → Strategic Takeaways
    │
    ▼
Shared Topic Memory
```

---

## Configuration

### Changing the Model

To use a different model, modify `agents/base.py`:

```python
MODEL = "phi3"        # Change from "llama2" to your preferred model
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

- [ ] Add an "auto-run all agents" mode to run the full pipeline in one click
- [ ] Add agent output voting/ranking to surface the most useful contributions
- [ ] Add multi-topic cross-referencing so agents can draw on related topics

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
