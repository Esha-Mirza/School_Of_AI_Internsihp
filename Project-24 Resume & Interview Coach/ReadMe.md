# Resume & Interview Coach

An AI-powered career coach that helps job seekers optimize their resumes, practice behavioral interviews, and analyze role fit.

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
- [Sample Resume Input](#sample-resume-input)
- [Sample Output](#sample-output)
- [Project Structure](#project-structure)
- [STAR Method Guide](#star-method-guide)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Overview

This application assists job seekers in preparing for their job search. It uses three specialized AI agents — Resume Optimizer, Behavioral Interview Agent, and Role-Fit Analyzer — to provide comprehensive career preparation support.

The application runs entirely locally, ensuring data privacy and eliminating API costs. It uses Ollama to host the LLaMA 2 model, TinyDB for persistent career history, and Streamlit for the user interface.

---

## Features

- **Resume Optimization** — Analyzes resumes and provides improvement suggestions
- **Behavioral Interview Practice** — Generates questions and provides STAR method feedback
- **Role-Fit Analysis** — Analyzes fit between resume and job descriptions
- **Persistent History** — Tracks improvements and progress over time
- **Export Ready** — Download analysis and feedback
- **Privacy-Focused** — All processing happens locally
- **No API Costs** — Free to use with no usage limits

---

## The Agents

| Agent | Role | Responsibility |
|---|---|---|
| **Resume Optimizer** | Resume Analyzer | Analyzes resumes, identifies strengths, and suggests improvements |
| **Behavioral Interview Agent** | Interview Coach | Generates questions and provides STAR method feedback |
| **Role-Fit Analyzer** | Fit Analyst | Analyzes resume-job fit and provides recommendations |

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **LLaMA 2** | Large Language Model for career coaching |
| **Ollama** | Local LLM hosting and inference |
| **TinyDB** | Lightweight JSON database for career history |
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
cd School_Of_AI_Internship/"Project-24 Resume & Interview Coach"
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
2. Create a new career profile or select an existing one
3. Paste your resume and target role
4. Use the three tabs for different coaching functions

---

## Sample Resume Input

```text
Sarah Johnson
123 Main Street, San Francisco, CA 94105
sarah.johnson@email.com | (555) 123-4567

SUMMARY
Experienced software engineer with 5+ years of experience in full-stack development. Passionate about building scalable applications and mentoring junior developers.

EXPERIENCE
Senior Software Engineer | TechCorp Inc. | 2020–Present
- Developed RESTful APIs serving 1M+ daily requests
- Led a team of 5 engineers on a successful product launch
- Reduced API response time by 40%
- Mentored 3 junior developers

Software Engineer | Innovate Labs | 2018–2020
- Built full-stack web applications using React and Node.js
- Collaborated with product team on feature development
- Participated in daily standups and sprint planning

EDUCATION
B.S. Computer Science | Stanford University | 2018

SKILLS
Languages: Python, JavaScript, Java, SQL
Frameworks: React, Node.js, Django
Cloud: AWS, Docker, Kubernetes
```

---

## Sample Output

**Resume Optimizer:**

```text
📝 Resume Analysis

Strengths:
- Clear career progression with 2+ years at each role
- Quantifiable achievements (1M+ requests, 40% improvement)
- Leadership experience with mentoring and team leading
- Good technical skill coverage

Weaknesses:
- No bullet points for education
- Missing relevant certifications
- Lacks keywords for ATS (Applicant Tracking Systems)
- No mention of agile methodologies

Keyword Optimization:
- Add: "Agile", "Scrum", "CI/CD", "Test-driven development"
- Add: "Cloud architecture", "Microservices", "API design"

Bullet Point Improvements:
Current: "Developed RESTful APIs serving 1M+ daily requests"
Improved: "Architected and deployed RESTful APIs handling 1M+ daily requests with 99.9% uptime"

Formatting Tips:
- Use consistent bullet points
- Add measurable outcomes for all roles
- Include relevant certifications section

Overall Score: 7.5/10
```

**Behavioral Interview Agent:**

```text
🎯 Interview Questions

1. Tell me about a time you led a team through a challenging project.
2. Describe a situation where you had to handle a difficult stakeholder.
3. Give an example of a time you failed and what you learned from it.
4. How do you handle conflicting priorities and deadlines?
5. Tell me about a time you had to adapt to a significant change.

💬 Practice Answer (STAR Method)

Question: Tell me about a time you led a team through a challenging project.
Your Answer: [Paste your answer here]

Feedback:
- Situation: Clear context provided
- Task: Well-defined objective
- Action: Good description of leadership actions
- Result: Includes measurable outcomes
- Strengths: Team leadership, problem-solving
- Suggestions: Add more detail on specific challenges overcome
- STAR Compliance: 4/5
- Overall Score: 8/10
```

**Role-Fit Analyzer:**

```text
📊 Role-Fit Analysis

Skills Match:
✅ Python - Strong match
✅ JavaScript - Strong match
✅ React - Strong match
✅ AWS - Strong match
✅ Leadership - Strong match
❌ Docker - Not mentioned
❌ Kubernetes - Not mentioned

Skills Gap:
- Docker (mentioned in job description, not in resume)
- Kubernetes (mentioned in job description, not in resume)

Experience Match:
- 5+ years of experience: ✅ Matches
- Full-stack development: ✅ Matches
- Team leadership: ✅ Matches

Cultural Fit Indicators:
- Strong focus on collaboration and mentoring
- Experience in agile environments
- Continuous learning mindset

Recommendations:
1. Add Docker and Kubernetes to skills section
2. Highlight cloud architecture experience
3. Include a certification section

Overall Fit Score: 8/10
```

---

## Project Structure

```
Project-24 Resume & Interview Coach/
├── agents/
│   ├── __init__.py
│   ├── base.py
│   ├── resume_agent.py
│   ├── interview_agent.py
│   └── fit_agent.py
├── memory/
│   ├── .gitkeep
│   └── memory_store.json
├── orchestrator.py
├── frontend.py
├── requirements.txt
└── README.md
```

---

## STAR Method Guide

| Component | Description |
|---|---|
| Situation | Set the context and background |
| Task | Describe what needed to be done |
| Action | Explain what you did specifically |
| Result | Share measurable outcomes |

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
| No analysis generated | Ensure resume text and job description are provided |
| Port already in use | Use `--server.port` flag to specify a different port |
| Module not found | Run `pip install -r requirements.txt` |
| Slow inference | Switch to a smaller model like `phi3` or `gemma:2b` |

---

## Roadmap

- [ ] Add resume-to-PDF export with the optimized suggestions applied
- [ ] Add mock interview mode with voice input/output for realistic practice
- [ ] Add tracking across multiple job applications with fit scores compared side by side

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
