# AI-Powered Grant Proposal Assistant

An AI-powered grant proposal assistant that helps researchers and nonprofits draft winning proposals with specialized agents for outlining, budgeting, and review simulation.

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
- [Sample Proposal Input](#sample-proposal-input)
- [Sample Output](#sample-output)
- [Project Structure](#project-structure)
- [Funding Agencies Supported](#funding-agencies-supported)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Overview

This application assists researchers and nonprofits in drafting comprehensive grant proposals. It uses three specialized AI agents — Outline Designer, Budget Estimator, and Reviewer Simulator — to structure proposals, estimate costs, and provide mock review feedback to strengthen submissions.

The application runs entirely locally, ensuring data privacy and eliminating API costs. It uses Ollama to host the LLaMA 2 model, TinyDB for persistent proposal memory, and Streamlit for the user interface.

---

## Features

- **Proposal Outline** — Creates structured proposal outlines
- **Budget Estimation** — Generates detailed budget breakdowns
- **Reviewer Simulation** — Provides mock review feedback and scores
- **Version Tracking** — Track proposal versions and rationale
- **Multiple Funding Agencies** — Support for NSF, NIH, EU Horizon, and more
- **Export Ready** — Download complete proposal packages
- **Privacy-Focused** — All processing happens locally
- **No API Costs** — Free to use with no usage limits

---

## The Agents

| Agent | Role | Responsibility |
|---|---|---|
| **Outline Designer** | Proposal Structurer | Creates comprehensive proposal outlines |
| **Budget Estimator** | Financial Planner | Generates detailed budget estimates |
| **Reviewer Simulator** | Feedback Provider | Simulates reviewer feedback and scores |

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **LLaMA 2** | Large Language Model for proposal drafting |
| **Ollama** | Local LLM hosting and inference |
| **TinyDB** | Lightweight JSON database for proposal memory |
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
cd School_Of_AI_Internship/"Project-23 Grant Proposal Assistant"
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
2. Create a new proposal or select an existing one
3. Enter project goals, funding agency, duration, and team size
4. Click **Generate Proposal** to create the complete proposal
5. Review the outline, budget, and reviewer feedback

---

## Sample Proposal Input

| Field | Value |
|---|---|
| Topic | AI-Enhanced Personalized Learning for STEM Education |
| Goals | Develop an adaptive learning platform using AI to personalize STEM education for high school students |
| Funding Agency | NSF |
| Duration | 24 months |
| Team Size | 5 |

---

## Sample Output

**Outline Designer:**

```text
📋 Proposal Outline

1. Executive Summary
   - Brief overview of the project
   - Key objectives and expected outcomes
   - Total budget requested

2. Introduction / Background
   - Problem statement: STEM education gap
   - Current challenges in personalized learning
   - Opportunity for AI-based solutions

3. Problem Statement
   - Students struggle with one-size-fits-all STEM education
   - Teachers lack tools for personalized instruction
   - Need for adaptive learning technologies

4. Proposed Solution / Methodology
   - AI-powered adaptive learning platform
   - Machine learning algorithms for student modeling
   - Personalized content delivery system
   - Pilot testing in 5 high schools

5. Timeline
   - Months 1-3: Requirements gathering and design
   - Months 4-12: Platform development
   - Months 13-18: Pilot testing
   - Months 19-24: Refinement and evaluation

6. Budget Overview
   - Personnel: 5 team members
   - Equipment and software
   - Travel for pilot testing
   - Total budget: $750,000

7. Evaluation Plan
   - Student learning outcomes assessment
   - Teacher satisfaction surveys
   - Usage analytics and engagement metrics

8. Conclusion
   - Potential impact on STEM education
   - Scalability and sustainability
```

**Budget Estimator:**

```text
💰 Budget Estimate

Personnel Costs:
- Principal Investigator: $120,000/year × 2 years = $240,000
- Co-PI (1): $100,000/year × 2 years = $200,000
- Postdoc (1): $70,000/year × 2 years = $140,000
- Graduate Students (2): $40,000/year × 2 years = $160,000
- Total Personnel: $740,000

Equipment / Materials:
- Cloud computing resources: $30,000
- Software licenses: $15,000
- Student devices for pilot: $25,000
- Total Equipment: $70,000

Travel / Fieldwork:
- Pilot testing in 5 schools: $20,000
- Conference presentations: $15,000
- Total Travel: $35,000

Participant Costs:
- Teacher stipends: $10,000
- Student incentives: $5,000
- Total Participants: $15,000

Administrative Overhead:
- Indirect costs (25%): $215,000

Total Budget: $1,075,000
```

**Reviewer Simulator:**

```text
🎯 Reviewer Feedback

Strengths:
- Well-defined problem statement
- Innovative AI approach
- Strong team composition
- Clear evaluation plan

Weaknesses:
- Limited discussion of privacy concerns
- Need more details on technology integration
- Unclear data management plan

Clarity of Goals:
- Goals are clear and measurable
- Objectives align with agency priorities

Feasibility:
- Timeline appears realistic
- Team has relevant expertise

Budget Justification:
- Personnel costs are reasonable
- Equipment costs are justified

Overall Score: 8.5/10

Recommendations for Improvement:
1. Add a data privacy and security section
2. Include more detail on technology integration
3. Develop a comprehensive data management plan
4. Address potential challenges and mitigation strategies
```

---

## Project Structure

```
Project-23 Grant Proposal Assistant/
├── agents/
│   ├── __init__.py
│   ├── base.py
│   ├── outline_agent.py
│   ├── budget_agent.py
│   └── reviewer_agent.py
├── memory/
│   ├── .gitkeep
│   └── memory_store.json
├── orchestrator.py
├── frontend.py
├── requirements.txt
└── README.md
```

---

## Funding Agencies Supported

| Agency | Description |
|---|---|
| NSF | National Science Foundation |
| NIH | National Institutes of Health |
| EU Horizon | European Union research program |
| Wellcome Trust | Global charitable foundation |
| Gates Foundation | Global health and development |

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
| No proposal generated | Ensure goals and funding agency are provided |
| Port already in use | Use `--server.port` flag to specify a different port |
| Module not found | Run `pip install -r requirements.txt` |
| Slow inference | Switch to a smaller model like `phi3` or `gemma:2b` |

---

## Roadmap

- [ ] Add agency-specific formatting templates (NSF vs NIH page/section requirements differ)
- [ ] Add collaborative multi-author editing support
- [ ] Add exportable proposal document (Word/PDF) matching agency submission formats

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
