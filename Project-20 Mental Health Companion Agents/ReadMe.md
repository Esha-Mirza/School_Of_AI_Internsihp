# Mental Health Companion Agents

A compassionate AI-powered journaling and wellness companion that helps users reflect on their emotions, gain perspective, and track their mental well-being over time.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Ollama](https://img.shields.io/badge/LLM-Ollama-black)

---

## Table of Contents

- [Overview](#overview)
- [Disclaimer](#disclaimer)
- [Features](#features)
- [The Agents](#the-agents)
- [Technology Stack](#technology-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Sample Journal Entry](#sample-journal-entry)
- [Sample Output](#sample-output)
- [Mood Tracking Visualization](#mood-tracking-visualization)
- [Project Structure](#project-structure)
- [Mood Levels](#mood-levels)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Overview

This application provides a safe, private space for users to journal their thoughts and emotions. It uses three specialized AI agents — Reflection, Cognitive Reframe, and Wellness Tracker — to help users process their feelings, gain new perspectives, and track their emotional well-being over time.

The application runs entirely locally, ensuring complete privacy and data security. It uses Ollama to host the LLaMA 2 model, TinyDB for persistent journal storage, Plotly for wellness visualization, and Streamlit for the user interface.

---

## Disclaimer

**Educational/Prototype Use Only** — This is NOT a medical device and is not a substitute for professional mental health care. Always consult qualified mental health professionals for clinical support. This tool is not equipped to handle mental health emergencies or crisis situations. If you or someone you know is in crisis, please contact a local emergency service or a crisis helpline in your country immediately.

---

## Features

- **Daily Journaling** — Record your thoughts and feelings
- **Mood Tracking** — Select your mood from 5 levels
- **Emotional Reflection** — AI summarizes emotions and themes
- **Cognitive Reframing** — Offers gentle perspective shifts
- **Wellness Tracking** — Visualize mood trends over time
- **Export Ready** — Download journal and mood data
- **Privacy-Focused** — All processing happens locally, no data is sent to external servers
- **No API Costs** — Free to use with no usage limits

---

## The Agents

| Agent | Role | Responsibility |
|---|---|---|
| **Reflection Agent** | Emotional Summarizer | Summarizes emotions and identifies themes |
| **Cognitive Reframe Agent** | Perspective Shifter | Offers gentle cognitive reframing |
| **Wellness Tracker Agent** | Trend Analyzer | Tracks well-being over time |

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **LLaMA 2** | Large Language Model for emotional support |
| **Ollama** | Local LLM hosting and inference |
| **TinyDB** | Lightweight JSON database for journal storage |
| **Plotly** | Interactive visualizations |
| **Pandas** | Data processing for mood trends |
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
cd School_Of_AI_Internship/"Project-20 Mental Health Companion"
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
2. Create a new journal or select an existing one
3. Select your mood from 5 levels
4. Write your journal entry
5. Click **Process Journal Entry** to get reflection and reframing
6. Track your mood trends in the Wellness Tracking tab

---

## Sample Journal Entry

**Mood:** 😊 Good

**Journal Text:**

```text
I had a productive day at work today. I completed a big project that I've been working on for weeks. My manager praised my work, which felt really good. However, I'm feeling a bit anxious about the upcoming presentation next week.
```

---

## Sample Output

**Reflection Agent:**

```text
🪞 Emotional Reflection

Mood: Good

Emotional Summary:
You're feeling proud and accomplished about completing your project. There's also some anxiety about the upcoming presentation. It's common to experience mixed emotions after a success.

Key Themes:
- Achievement and recognition
- Work-related stress
- Anticipation anxiety

Validation:
It's completely normal to feel both proud and anxious. You've worked hard and deserve the recognition. The anxiety shows that you care about doing well.
```

**Cognitive Reframe Agent:**

```text
🔄 Cognitive Reframe

Alternative Perspective:
While the presentation is coming up, remember that you've already proven your capability by completing the project successfully. Your manager's praise is evidence of your skills.

Gentle Reframe:
The anxiety you're feeling is energy that can be channeled into preparation. Instead of worrying about the outcome, focus on what you can control—preparing well and doing your best.

Balanced View:
- Strength: You've demonstrated success already
- Challenge: Presentation anxiety is common
- Opportunity: This is a chance to showcase your work

Actionable Perspective:
Break the presentation preparation into small steps. Your past success shows you're capable of succeeding again.
```

---

## Mood Tracking Visualization

```text
📊 Wellness Tracking

Mood Trends Over Time:
[Interactive Plotly chart showing mood progression]

Mood Distribution:
😊 Excellent: 3 days
😌 Good: 2 days
😐 Okay: 2 days
😔 Low: 0 days
😢 Struggling: 1 day
```

---

## Project Structure

```
Project-20 Mental Health Companion/
├── agents/
│   ├── __init__.py
│   ├── base.py
│   ├── reflection_agent.py
│   ├── cognitive_reframe_agent.py
│   └── wellness_tracker_agent.py
├── memory/
│   ├── .gitkeep
│   └── memory_store.json
├── orchestrator.py
├── frontend.py
├── requirements.txt
└── README.md
```

---

## Mood Levels

| Mood | Emoji | Value |
|---|---|---|
| Excellent | 😊 | 5 |
| Good | 😌 | 4 |
| Okay | 😐 | 3 |
| Low | 😔 | 2 |
| Struggling | 😢 | 1 |

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
| No mood data | Write journal entries with mood selected |
| Port already in use | Use `--server.port` flag to specify a different port |
| Module not found | Run `pip install -r requirements.txt` |
| Slow inference | Switch to a smaller model like `phi3` or `gemma:2b` |

---

## Roadmap

- [ ] Add gentle in-app prompts to seek professional support when low-mood patterns persist
- [ ] Add guided journaling prompts for days when users don't know what to write
- [ ] Add exportable wellness summary for sharing with a therapist (optional, user-initiated)

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
