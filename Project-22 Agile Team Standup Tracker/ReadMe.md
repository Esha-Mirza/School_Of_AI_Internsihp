# Agile Team Standup Tracker

An AI-powered asynchronous standup system that helps software teams track daily updates, identify blockers, and monitor sprint progress.

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
- [Sample Standup Update](#sample-standup-update)
- [Sample Output](#sample-output)
- [Project Structure](#project-structure)
- [Sprint Dashboard](#sprint-dashboard)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Overview

This application enables software teams to run asynchronous standup meetings. Team members submit daily updates on what they did yesterday, what they'll do today, and any blockers. Three specialized AI agents — Summary Agent, Blocker Detector, and Sprint Progress Estimator — analyze these updates to provide team insights and identify issues.

The application runs entirely locally, ensuring data privacy and eliminating API costs. It uses Ollama to host the LLaMA 2 model, TinyDB for persistent sprint data, and Streamlit for the user interface.

---

## Features

- **Asynchronous Standups** — Team members submit updates at their convenience
- **Summary Agent** — Summarizes team updates and highlights key points
- **Blocker Detector** — Identifies blockers, impediments, and dependencies
- **Sprint Progress Estimator** — Tracks sprint health and velocity
- **Persistent Logs** — Per-sprint tracking with full history
- **Export Ready** — Download daily and weekly digests
- **Privacy-Focused** — All processing happens locally
- **No API Costs** — Free to use with no usage limits

---

## The Agents

| Agent | Role | Responsibility |
|---|---|---|
| **Summary Agent** | Team Summarizer | Summarizes team updates and highlights progress |
| **Blocker Detector** | Risk Identifier | Identifies blockers, impediments, and dependencies |
| **Sprint Progress Estimator** | Progress Tracker | Assesses sprint health and velocity |

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **LLaMA 2** | Large Language Model for standup analysis |
| **Ollama** | Local LLM hosting and inference |
| **TinyDB** | Lightweight JSON database for sprint data |
| **Plotly** | Interactive visualizations |
| **Pandas** | Data processing for sprint metrics |
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
cd School_Of_AI_Internship/"Project-22 Agile Team Standup Tracker"
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
2. Create a new sprint or select an existing one
3. Team members submit daily standup updates
4. View the summaries, blocker reports, and sprint progress

---

## Sample Standup Update

```text
Team Member: Sarah
Date: 2024-01-15

Yesterday: Completed the authentication module and fixed 3 bugs in the payment gateway.
Today: Will start working on the notification service and review PRs.
Blockers: Waiting for API documentation from the backend team.
```

---

## Sample Output

**Team Summary:**

```text
📝 Daily Standup Summary

Team Overview:
- Sarah completed authentication module and bug fixes
- Mark is reviewing the payment integration
- Emily has finalized the UI designs

Key Highlights:
- Authentication module is complete ✅
- Payment gateway bugs resolved ✅
- UI designs finalized ✅

Focus Areas:
- Notification service implementation
- API documentation delivery
- PR reviews
```

**Blocker Report:**

```text
🚨 Blocker Report

Active Blockers:
- Sarah is waiting for API documentation from backend team

Dependencies:
- Notification service needs backend API docs
- Payment integration blocked by external vendor

Recommendations:
- Escalate API documentation request
- Consider writing mock APIs as fallback
```

**Sprint Progress:**

```text
📊 Sprint Progress Report

Sprint Health: 🟢 On Track

Team Velocity:
- Committed: 12 story points
- Completed: 8 story points
- Remaining: 4 story points

Completion Forecast:
- On track to complete all committed work by sprint end

Recommendations:
- Monitor API documentation blocker
- Consider backlog refinement session
```

---

## Project Structure

```
Project-22 Agile Team Standup Tracker/
├── agents/
│   ├── __init__.py
│   ├── base.py
│   ├── summary_agent.py
│   ├── blocker_agent.py
│   └── sprint_agent.py
├── memory/
│   ├── .gitkeep
│   └── memory_store.json
├── orchestrator.py
├── frontend.py
├── requirements.txt
└── README.md
```

---

## Sprint Dashboard

**Team Activity Chart:**

```text
📈 Team Activity

Updates by Team Member:
Sarah: 5 updates
Mark: 4 updates
Emily: 4 updates
John: 3 updates
```

**Sprint Health Metrics:**

```text
📊 Sprint Statistics

Total Updates: 16
Active Days: 5
Teammates: 4
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
| No updates submitted | Ensure team members submit daily updates |
| Port already in use | Use `--server.port` flag to specify a different port |
| Module not found | Run `pip install -r requirements.txt` |
| Slow inference | Switch to a smaller model like `phi3` or `gemma:2b` |

---

## Roadmap

- [ ] Add Slack/Discord integration for update submission and digest delivery
- [ ] Add historical velocity trend charts across multiple sprints
- [ ] Add automated blocker escalation reminders after N days unresolved

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Acknowledgments

- [Ollama](https://ollama.com/) - Local LLM runtime
- TinyDB - Lightweight database
- Plotly - Interactive visualizations
- Streamlit - UI framework

---

## Contact

- **GitHub:** [Esha-Mirza](https://github.com/Esha-Mirza)
- **Email:** esha101374@gmail.com
