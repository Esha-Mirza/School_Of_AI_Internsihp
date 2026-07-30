# Academic Research Collaborator

An AI-powered research assistant that helps scholars write academic papers by providing literature review, hypothesis validation, and draft polishing services.

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
- [Sample Research Input](#sample-research-input)
- [Sample Output](#sample-output)
- [Project Structure](#project-structure)
- [Research Workflow](#research-workflow)
- [Academic Writing Tips](#academic-writing-tips)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Overview

This application assists researchers and academics in the writing process. It uses three specialized AI agents — Literature Review, Hypothesis Validator, and Draft Polisher — to help scholars conduct comprehensive literature reviews, validate hypotheses, and polish academic drafts.

The application runs entirely locally, ensuring data privacy and eliminating API costs. It uses Ollama to host the LLaMA 2 model, TinyDB for persistent research memory, and Streamlit for the user interface.

---

## Features

- **Literature Review** — Analyzes citations and identifies key themes and gaps
- **Hypothesis Validation** — Evaluates hypotheses against evidence
- **Draft Polishing** — Improves academic writing quality
- **Research Memory** — Tracks evolving drafts and research progress
- **Export Ready** — Download polished drafts and research notes
- **Privacy-Focused** — All processing happens locally
- **No API Costs** — Free to use with no usage limits

---

## The Agents

| Agent | Role | Responsibility |
|---|---|---|
| **Literature Review Agent** | Research Synthesizer | Analyzes literature, identifies themes and gaps |
| **Hypothesis Validator Agent** | Hypothesis Tester | Evaluates hypotheses against evidence |
| **Draft Polisher Agent** | Academic Editor | Improves academic writing and structure |

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **LLaMA 2** | Large Language Model for academic writing |
| **Ollama** | Local LLM hosting and inference |
| **TinyDB** | Lightweight JSON database for research memory |
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
cd School_Of_AI_Internship/"Project-25 Academic Research Collaborator"
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
2. Create a new research project or select an existing one
3. Enter research question, citations, and draft
4. Use the four tabs for different research functions

---

## Sample Research Input

**Research Question:**

```text
How does artificial intelligence impact student learning outcomes in higher education?
```

**Citations/Literature:**

```text
Smith, J. (2023). AI in Education: A Comprehensive Review. Journal of Educational Technology, 45(2), 123-145.
Johnson, M. (2022). Personalized Learning with AI. Educational Research Review, 34, 78-92.
Lee, S. (2024). Student Engagement and AI Tools. Computers & Education, 190, 104-118.
```

**Draft:**

```text
Artificial intelligence is becoming increasingly prevalent in higher education. Many institutions are adopting AI tools to enhance student learning. However, the impact of these technologies on student outcomes remains unclear. This study aims to investigate the relationship between AI implementation and student academic performance.
```

---

## Sample Output

**Literature Review Agent:**

```text
📚 Literature Review

Key Themes:
1. AI integration in education is rapidly growing
2. Personalized learning is a major application area
3. Student engagement is a key focus of research

Gaps:
1. Limited research on long-term impact of AI on learning
2. Few studies on AI efficacy in specific disciplines
3. Lack of standardized metrics for measuring AI impact

Methodologies:
- Quantitative studies (45%)
- Mixed methods (30%)
- Qualitative studies (25%)

Key Findings:
- AI tools improve engagement (Lee, 2024)
- Personalized learning shows positive outcomes (Johnson, 2022)
- Integration challenges remain significant (Smith, 2023)

Relevance:
These findings support the need for further investigation into how AI affects student learning outcomes in higher education settings.
```

**Hypothesis Validator Agent:**

```text
🔬 Hypothesis Validation

Generated Hypotheses:
1. H1: AI-powered learning tools increase student engagement in higher education.
2. H2: Personalized AI tutoring improves student academic performance.
3. H3: AI integration reduces student dropout rates.

Validation for H1:
Evidence: Lee (2024) found AI tools improve engagement by 35%.
Support: Strong empirical evidence supports this hypothesis.
Recommendation: Proceed with H1 as a primary hypothesis.

Validation for H2:
Evidence: Johnson (2022) reported improved performance with personalized AI.
Support: Moderate evidence supports this hypothesis.
Recommendation: Use as a secondary hypothesis.

Validation for H3:
Evidence: Limited research available on dropout rates.
Support: Weak evidence currently available.
Recommendation: Consider as a research question rather than a hypothesis.

Confidence Levels:
- H1: 9/10
- H2: 7/10
- H3: 4/10
```

**Draft Polisher Agent:**

```text
✍️ Polished Draft

Artificial intelligence is increasingly prevalent in higher education, with many institutions adopting AI tools to enhance student learning. Despite this growing adoption, the impact of these technologies on student outcomes remains unclear. This study aims to investigate the relationship between AI implementation and student academic performance, addressing a critical gap in the existing literature.

Feedback:
- Strengths: Clear problem statement, good topic framing
- Improvements: Added transition sentence, strengthened research gap statement
- Suggestions: Add specific research questions, consider methodology section

Areas for Expansion:
- Include theoretical framework
- Add preliminary literature review
- Discuss research methodology

Next Steps:
1. Develop specific research questions
2. Select appropriate methodology
3. Expand literature review
4. Begin data collection
```

---

## Project Structure

```
Project-25 Academic Research Collaborator/
├── agents/
│   ├── __init__.py
│   ├── base.py
│   ├── lit_review_agent.py
│   ├── hypothesis_agent.py
│   └── draft_agent.py
├── memory/
│   ├── .gitkeep
│   └── memory_store.json
├── orchestrator.py
├── frontend.py
├── requirements.txt
└── README.md
```

---

## Research Workflow

```text
User Input (Research Question)
    │
    ▼
[Literature Review Agent] → Key Themes & Gaps
    │
    ▼
[Hypothesis Validator Agent] → Validated Hypotheses
    │
    ▼
[Draft Polisher Agent] → Polished Draft
    │
    ▼
Research Progress (Memory)
```

---

## Academic Writing Tips

| Category | Tips |
|---|---|
| Introduction | Start broad, narrow to your research gap |
| Literature Review | Organize by theme, not author |
| Methodology | Be specific and reproducible |
| Results | Present findings objectively |
| Discussion | Interpret results, link to literature |
| Conclusion | Summarize and suggest future research |

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
| No literature review generated | Ensure citations are provided |
| Port already in use | Use `--server.port` flag to specify a different port |
| Module not found | Run `pip install -r requirements.txt` |
| Slow inference | Switch to a smaller model like `phi3` or `gemma:2b` |

---

## Roadmap

- [ ] Add citation format conversion (APA, MLA, Chicago)
- [ ] Add plagiarism/originality style similarity checking
- [ ] Add integration with reference managers (Zotero, Mendeley) for citation import

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
