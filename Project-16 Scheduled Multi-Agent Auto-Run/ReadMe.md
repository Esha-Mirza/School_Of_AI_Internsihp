# Scheduled Multi-Agent Auto-Run

An automated agent workflow engine that schedules and runs multi-agent research tasks at specified intervals for Athena Research Group.

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
- [Creating a Workflow](#creating-a-workflow)
- [Sample Workflow Output](#sample-workflow-output)
- [Project Structure](#project-structure)
- [How the Scheduler Works](#how-the-scheduler-works)
- [Scheduling Options](#scheduling-options)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Overview

This application extends the AthenaCore multi-agent system by adding automated scheduling capabilities. Users can define workflows that run specific agents on a schedule — daily, hourly, or at custom intervals. Each run is stored with timestamps, allowing users to track research progress over time.

The application runs entirely locally, ensuring data privacy and eliminating API costs. It uses Ollama to host the LLaMA 2 model, APScheduler for task scheduling, TinyDB for persistent storage, and Streamlit for the user interface.

---

## Features

- **Automated Scheduling** — Run agents at specified times (daily, hourly, custom intervals)
- **Workflow Management** — Create, edit, and delete scheduled workflows
- **Agent Selection** — Choose which agents to run in each workflow
- **Run History** — Track all automated runs with timestamps and results
- **Dashboard Notifications** — View run status and results
- **Export Ready** — Download run history
- **Privacy-Focused** — All processing happens locally
- **No API Costs** — Free to use with no usage limits

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **APScheduler** | Task scheduling and automation |
| **LLaMA 2** | Large Language Model for agent reasoning |
| **Ollama** | Local LLM hosting and inference |
| **TinyDB** | Lightweight JSON database for storage |
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
cd School_Of_AI_Internship/"Project-16 Scheduled Multi-Agent Auto-Run"
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
2. Create a new workflow or select an existing one
3. Configure the schedule (daily at specific time or interval-based)
4. Select which agents to run
5. Enable the workflow to start automated runs

---

## Creating a Workflow

**Step 1: Enter Workflow Name**

```text
Morning Research Brief
```

**Step 2: Select Topic**

```text
AI Regulation
```

**Step 3: Select Agents**

```text
☑ Research Agent
☑ Summarizer Agent
☑ Insight Agent
```

**Step 4: Set Schedule**

```text
Daily at 8:00 AM
```

**Step 5: Save and Schedule**

```text
✅ Workflow 'Morning Research Brief' created!
✅ Scheduled! Next run: 2024-01-16 08:00:00
```

---

## Sample Workflow Output

**Run History:**

```text
🕐 2024-01-15 08:00:00
✅ Research Agent: EU AI Act categorizes AI systems by risk level...
✅ Summarizer Agent: • EU AI Act categorizes AI by risk...
✅ Insight Agent: Companies need compliance strategies by 2025...

🕐 2024-01-16 08:00:00
✅ Research Agent: Latest developments in AI regulation...
✅ Summarizer Agent: • New AI regulations proposed in US...
✅ Insight Agent: Global regulatory divergence emerging...
```

---

## Project Structure

```
Project-16 Scheduled Multi-Agent Auto-Run/
├── agents/
│   ├── __init__.py
│   ├── base.py
│   ├── research_agent.py
│   ├── summarizer_agent.py
│   ├── devil_agent.py
│   └── insight_agent.py
├── memory/
│   ├── .gitkeep
│   ├── memory_store.json
│   └── scheduler_store.json   # NEW: Scheduler data
├── scheduler.py                # NEW: Task scheduler
├── orchestrator.py
├── frontend.py                 # Updated with scheduler UI
├── requirements.txt
└── README.md
```

---

## How the Scheduler Works

### Workflow Lifecycle

```text
User Creates Workflow
    │
    ▼
Workflow Saved to Database
    │
    ▼
User Schedules Workflow
    │
    ▼
APScheduler Activates Job
    │
    ▼
Workflow Runs at Specified Time
    │
    ▼
Results Stored in Run History
    │
    ▼
User Views Results in Dashboard
```

---

## Scheduling Options

| Type | Description | Example |
|---|---|---|
| Daily (Cron) | Runs at a specific time each day | 8:00 AM daily |
| Interval | Runs after a set number of hours | Every 24 hours |

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
| Scheduler not starting | Ensure APScheduler is installed (`pip install apscheduler`) |
| Workflow not running | Check that the workflow is enabled and scheduled |
| Port already in use | Use `--server.port` flag to specify a different port |
| Module not found | Run `pip install -r requirements.txt` |
| Slow inference | Switch to a smaller model like `phi3` or `gemma:2b` |

---

## Roadmap

- [ ] Add email/Slack notifications when a scheduled run completes
- [ ] Add retry logic for failed scheduled runs
- [ ] Add a calendar view of upcoming and past scheduled runs

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Acknowledgments

- APScheduler - Task scheduling
- [Ollama](https://ollama.com/) - Local LLM runtime
- TinyDB - Lightweight database
- Streamlit - UI framework

---

## Contact

- **GitHub:** [Esha-Mirza](https://github.com/Esha-Mirza)
- **Email:** esha101374@gmail.com
