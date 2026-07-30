# Travel Planning Assistant

An AI-powered travel planning assistant that helps users collaboratively plan trips with specialized agents for itinerary building, cost estimation, and cultural guidance.

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
- [Sample Trip Input](#sample-trip-input)
- [Sample Output](#sample-output)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Overview

This application helps travelers plan their dream vacations with the help of three specialized AI agents. The Itinerary Builder creates daily trip plans, the Cost Estimator provides budget breakdowns, and the Local Culture Coach offers cultural insights and tips.

The application runs entirely locally, ensuring data privacy and eliminating API costs. It uses Ollama to host the LLaMA 2 model, TinyDB for persistent trip memory, and Streamlit for the user interface.

---

## Features

- **Trip Planning** — Enter destination, budget, and interests
- **Itinerary Builder** — Creates detailed day-by-day trip plans
- **Cost Estimator** — Provides comprehensive budget breakdowns
- **Local Culture Coach** — Offers cultural insights and etiquette tips
- **Trip Memory** — Persistent storage of trip plans and history
- **Export Ready** — Download complete trip plans
- **Privacy-Focused** — All processing happens locally
- **No API Costs** — Free to use with no usage limits

---

## The Agents

| Agent | Role | Responsibility |
|---|---|---|
| **Itinerary Builder** | Trip Planner | Creates daily itineraries with activities |
| **Cost Estimator** | Budget Planner | Estimates accommodation, food, and activity costs |
| **Local Culture Coach** | Cultural Guide | Provides cultural insights, etiquette, and language tips |

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **LLaMA 2** | Large Language Model for travel planning |
| **Ollama** | Local LLM hosting and inference |
| **TinyDB** | Lightweight JSON database for trip memory |
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
cd School_Of_AI_Internship/"Project-21 Travel Planning Assistant"
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
2. Create a new trip or select an existing one
3. Enter destination, duration, budget, and interests
4. Click **Generate Trip Plan**
5. View the itinerary, cost estimate, and cultural guide

---

## Sample Trip Input

| Field | Value |
|---|---|
| Destination | Paris, France |
| Duration | 5 days |
| Budget | Mid-range |
| Interests | Food, History, Art, Culture |

---

## Sample Output

**Itinerary Builder:**

```text
🗺️ Day-by-Day Itinerary

Day 1: Arrival and Orientation
- Morning: Arrive at CDG, check into hotel
- Afternoon: Walk along Champs-Élysées, visit Arc de Triomphe
- Evening: Dinner at a traditional French bistro

Day 2: Art and History
- Morning: Visit Louvre Museum (Mona Lisa, Venus de Milo)
- Afternoon: Explore Musée d'Orsay
- Evening: Seine River cruise

Day 3: Iconic Landmarks
- Morning: Eiffel Tower (morning visit)
- Afternoon: Notre-Dame Cathedral, Latin Quarter
- Evening: Montmartre and Sacré-Cœur Basilica

Day 4: Day Trip
- Optional: Versailles Palace or Disneyland Paris
- Evening: Dinner and shopping

Day 5: Departure
- Morning: Last-minute shopping or visit
- Afternoon: Depart from CDG
```

**Cost Estimator:**

```text
💰 Cost Breakdown (5 days, 2 travelers)

Accommodation:
- Hotel: €150/night × 5 = €750

Food:
- Meals: €60/day × 5 = €300

Transportation:
- Metro: €20/day × 5 = €100
- Airport transfers: €60

Activities:
- Museums: €50/day × 3 = €150
- Eiffel Tower: €30
- Seine Cruise: €40

Total Estimated Cost: €1,430

Money-Saving Tips:
- Consider a Paris Museum Pass
- Use public transport passes
- Book attractions online in advance
```

**Local Culture Coach:**

```text
🎭 Cultural Guide: Paris

Local Customs:
- Always say "Bonjour" when entering shops
- Keep voice low in public places
- Dress appropriately for restaurants

Language Tips:
- Bonjour = Hello
- Merci = Thank you
- S'il vous plaît = Please
- Où est...? = Where is...?
- Combien ça coûte? = How much?

Etiquette:
- Wait to be seated at restaurants
- Keep hands visible on the table
- Tipping: 5-10% is appreciated

Local Experiences:
- Try a croissant at a local bakery
- Visit a street market
- Take a cooking class
- Explore neighborhood cafes

Cultural Sensitivity:
- The French appreciate effort to speak French
- Avoid loud conversations in public
- Be patient with service, it's more relaxed
```

---

## Project Structure

```
Project-21 Travel Planning Assistant/
├── agents/
│   ├── __init__.py
│   ├── base.py
│   ├── itinerary_agent.py
│   ├── cost_estimator_agent.py
│   └── culture_agent.py
├── memory/
│   ├── .gitkeep
│   └── memory_store.json
├── orchestrator.py
├── frontend.py
├── requirements.txt
└── README.md
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
| No itinerary generated | Ensure destination and interests are provided |
| Port already in use | Use `--server.port` flag to specify a different port |
| Module not found | Run `pip install -r requirements.txt` |
| Slow inference | Switch to a smaller model like `phi3` or `gemma:2b` |

---

## Roadmap

- [ ] Add live weather integration for the travel dates
- [ ] Add map view of the itinerary using an interactive map widget
- [ ] Add multi-destination trip support (e.g. Paris → Rome → Barcelona)

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
