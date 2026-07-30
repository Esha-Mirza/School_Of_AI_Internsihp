# Visual Timeline of Agent Collaboration

An interactive visualization tool that displays the sequence of agent outputs over time, showing how AI agents collaborate on research topics.

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
- [Sample Timeline Output](#sample-timeline-output)
- [Project Structure](#project-structure)
- [How the Timeline Works](#how-the-timeline-works)
- [Visualization Options](#visualization-options)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Overview

This application extends the AthenaCore multi-agent system by adding a visual timeline that displays agent contributions in chronological order. It helps users understand how research evolves through the collaboration of specialized AI agents — Research, Summarizer, Devil's Advocate, and Insight — over time.

The application runs entirely locally, ensuring data privacy and eliminating API costs. It uses Ollama to host the LLaMA 2 model, TinyDB for persistent memory, Plotly for interactive visualizations, and Streamlit for the user interface.

---

## Features

- **Visual Timeline** — Chronological display of all agent contributions
- **Agent Grouping** — Color-coded cards for each agent type
- **Interactive Charts** — Plotly-based timeline visualization
- **Contribution Summary** — Statistics by agent
- **Timestamp Tracking** — Every agent response is time-stamped
- **Export Ready** — Download timeline as CSV or text
- **Privacy-Focused** — All processing happens locally
- **No API Costs** — Free to use with no usage limits

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **LLaMA 2** | Large Language Model for agent reasoning |
| **Ollama** | Local LLM hosting and inference |
| **TinyDB** | Lightweight JSON database for memory storage |
| **Plotly** | Interactive visualizations |
| **Pandas** | Data processing for timeline data |
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
cd School_Of_AI_Internship/"Project-14 Visual Timeline of Agent Collaboration"
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
3. Run agents to generate contributions
4. Switch to the **Timeline View** tab
5. Explore the visual timeline in three views:
   - **Card View** — Chronological cards with agent names and timestamps
   - **Chart View** — Interactive Plotly timeline chart
   - **Summary View** — Agent contribution statistics

---

## Sample Timeline Output

**Card View:**

```text
🕐 2024-01-15 10:30:00 | 🔵 Research Agent
Research findings on EU AI regulations...

🕐 2024-01-15 10:32:00 | 🟢 Summarizer Agent
Key points: EU AI Act categorizes AI by risk...

🕐 2024-01-15 10:34:00 | 🔴 Devil's Advocate
Counterarguments: Enforcement challenges...

🕐 2024-01-15 10:36:00 | 🟣 Insight Agent
Strategic implications: Compliance by 2025...
```

**Chart View:**

- Interactive Plotly chart showing agent contributions over time
- Hover for details on each contribution
- Zoom and pan functionality

**Summary View:**

```text
📈 Agent Contribution Summary

Total Contributions: 12
Number of Agents: 4
Most Active Agent: Research Agent (5 contributions)

Agent Activity Breakdown:
- Research Agent: 5 contributions (41.7%)
- Summarizer Agent: 3 contributions (25.0%)
- Devil's Advocate: 2 contributions (16.7%)
- Insight Agent: 2 contributions (16.7%)
```

---

## Project Structure

```
Project-14 Visual Timeline of Agent Collaboration/
├── agents/
│   ├── __init__.py
│   ├── base.py              ← Updated with timestamps
│   ├── research_agent.py
│   ├── summarizer_agent.py
│   ├── devil_agent.py
│   └── insight_agent.py
├── memory/
│   ├── .gitkeep
│   └── memory_store.json
├── timeline.py               ← NEW: Timeline visualization
├── orchestrator.py
├── frontend.py               ← Updated with timeline tab
├── requirements.txt
└── README.md
```

---

## How the Timeline Works

### Timestamp Addition

Every agent response is automatically time-stamped:

```python
def log_agent_response(topic: str, agent: str, content: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Store agent response with timestamp
```

### Timeline Data Structure

```json
{
    "agent": "Research Agent",
    "content": "Research findings...",
    "timestamp": "2024-01-15 10:30:00"
}
```

---

## Visualization Options

| View | Description |
|---|---|
| Card View | Chronological cards with agent names and timestamps |
| Chart View | Interactive Plotly chart |
| Summary View | Agent contribution statistics |

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
| Timeline not showing | Run at least one agent to generate contributions |
| Plotly not rendering | Ensure plotly is installed (`pip install plotly`) |
| Port already in use | Use `--server.port` flag to specify a different port |
| Module not found | Run `pip install -r requirements.txt` |
| Slow inference | Switch to a smaller model like `phi3` or `gemma:2b` |

---

## Roadmap

- [ ] Add filtering by agent type or date range on the timeline
- [ ] Add a "compare topics" view to see multiple timelines side by side
- [ ] Add animated playback of the timeline (step through contributions in order)

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Acknowledgments

- [Ollama](https://ollama.com/) - Local LLM runtime
- Plotly - Interactive visualizations
- TinyDB - Lightweight database
- Streamlit - UI framework

---

## Contact

- **GitHub:** [Esha-Mirza](https://github.com/Esha-Mirza)
- **Email:** esha101374@gmail.com
