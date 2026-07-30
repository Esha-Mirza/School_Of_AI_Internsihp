# Cybersecurity Incident Response Agent

An AI-powered security incident response system that helps security teams triage incidents using multi-agent reasoning and provides actionable response recommendations.

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
- [Sample Log Data](#sample-log-data)
- [Sample Output](#sample-output)
- [Project Structure](#project-structure)
- [Incident Response Flow](#incident-response-flow)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [License](#license)
- [Disclaimer](#disclaimer)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Overview

This application assists security operations teams in analyzing and responding to cybersecurity incidents. It uses three specialized agents — Log Parser, Threat Intelligence, and Containment Advisor — to analyze system logs, provide threat context, and recommend response actions. The agents collaborate to deliver a comprehensive incident response plan.

The application runs entirely locally, ensuring data privacy and eliminating API costs. It uses Ollama to host the LLaMA 2 model, TinyDB for persistent incident memory, and Streamlit for the user interface.

---

## Features

- **Log Analysis** — Parses and analyzes system logs and security alerts
- **Threat Intelligence** — Provides threat context and actor profiling
- **Containment Planning** — Recommends response and containment actions
- **Incident Memory** — Persistent tracking of incident response history
- **Export Ready** — Download incident reports
- **Privacy-Focused** — All processing happens locally, no data is sent to external servers
- **No API Costs** — Free to use with no usage limits

---

## The Agents

| Agent | Role | Responsibility |
|---|---|---|
| **Log Parser Agent** | Log Analyst | Analyzes logs and alerts, assesses severity |
| **Threat Intelligence Agent** | Threat Context Provider | Provides threat actor profiles and TTPs |
| **Containment Advisor Agent** | Response Planner | Recommends containment and response actions |

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **LLaMA 2** | Large Language Model for security analysis |
| **Ollama** | Local LLM hosting and inference |
| **TinyDB** | Lightweight JSON database for incident memory |
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
cd School_Of_AI_Internship/"Project-19 Cybersecurity Incident Agent"
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
2. Create a new incident or select an existing one
3. Upload logs or paste alert data
4. Click the **Analyze Incident** button
5. Review the incident response report

---

## Sample Log Data

```text
[2024-01-15 14:23:45] Failed login attempt from IP 10.0.0.25
[2024-01-15 14:24:12] Multiple failed logins detected (5 attempts)
[2024-01-15 14:25:01] Successful login from 10.0.0.25
[2024-01-15 14:25:30] Unusual outbound traffic detected
[2024-01-15 14:26:00] Suspicious file download from external source
```

---

## Sample Output

**Log Parser Agent:**

```text
📋 Log Parser Analysis

Summary of Events:
- Multiple failed login attempts from 10.0.0.25
- Successful login followed by unusual outbound traffic
- Suspicious file download detected

Severity Assessment: HIGH

Key Indicators:
- IP: 10.0.0.25 (Internal address - possible compromised credential)
- Timeline: 5 failed attempts → success → outbound traffic → download
- Pattern: Brute force followed by exfiltration attempt

Potential Attack Vectors:
- Account compromise
- Credential theft
- Data exfiltration
```

**Threat Intelligence Agent:**

```text
🔍 Threat Intelligence Report

Threat Actor Profile:
- Likely: Opportunistic cybercriminal
- Motive: Financial gain (data exfiltration)
- Capability: Moderate (using common tools)

Known TTPs:
- Tactic: Initial Access (Brute Force)
- Tactic: Discovery (Internal reconnaissance)
- Tactic: Exfiltration (Data transfer)

Recent Similar Incidents:
- Similar patterns reported in financial sector
- IP 10.0.0.25 seen in previous incidents
```

**Containment Advisor Agent:**

```text
🛡️ Incident Response Plan

Immediate Actions (5-10 min):
1. Disable compromised account
2. Isolate affected system from network
3. Capture memory and disk images

Containment Steps:
1. Block IP 10.0.0.25 at firewall
2. Reset all credentials for affected user
3. Implement additional MFA verification

Eradication Recommendations:
1. Scan system for malware
2. Remove any unauthorized software
3. Apply security patches

Recovery Plan:
1. Restore from clean backup
2. Test system functionality
3. Monitor for recurrence

Prevention Measures:
1. Implement account lockout policies
2. Deploy endpoint detection and response (EDR)
3. Conduct security awareness training
```

---

## Project Structure

```
Project-19 Cybersecurity Incident Agent/
├── agents/
│   ├── __init__.py
│   ├── base.py
│   ├── log_parser_agent.py
│   ├── threat_intel_agent.py
│   └── containment_agent.py
├── memory/
│   ├── .gitkeep
│   └── memory_store.json
├── orchestrator.py
├── frontend.py
├── requirements.txt
└── README.md
```

---

## Incident Response Flow

```text
User Input (Logs/Alerts)
    │
    ▼
[Log Parser Agent] → Analysis & Severity Assessment
    │
    ▼
[Threat Intelligence Agent] → Threat Context & Profiling
    │
    ▼
[Containment Advisor Agent] → Response & Containment Plan
    │
    ▼
Incident Response Report
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
| No analysis generated | Ensure log data is provided |
| Port already in use | Use `--server.port` flag to specify a different port |
| Module not found | Run `pip install -r requirements.txt` |
| Slow inference | Switch to a smaller model like `phi3` or `gemma:2b` |

---

## Roadmap

- [ ] Add MITRE ATT&CK technique ID tagging on identified TTPs
- [ ] Add automated log ingestion from common SIEM export formats
- [ ] Add severity trend tracking across multiple incidents over time

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Disclaimer

**Educational/Prototype Use Only** — This is NOT a certified security tool. Always consult qualified security professionals for critical security incidents.

---

## Acknowledgments

- [Ollama](https://ollama.com/) - Local LLM runtime
- TinyDB - Lightweight database
- Streamlit - UI framework
- MITRE ATT&CK - TTP reference

---

## Contact

- **GitHub:** [Esha-Mirza](https://github.com/Esha-Mirza)
- **Email:** esha101374@gmail.com
