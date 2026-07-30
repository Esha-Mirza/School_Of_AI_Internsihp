# Meeting Notes Generator AI

An AI-powered meeting notes generator that transcribes audio files and automatically generates summaries, action items, and full transcripts using Whisper and LLaMA 2.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Ollama](https://img.shields.io/badge/LLM-Ollama-black)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Prerequisites](#prerequisites)
- [FFmpeg Installation](#ffmpeg-installation)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Supported Audio Formats](#supported-audio-formats)
- [Sample Output](#sample-output)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Overview

This application automates the process of converting meeting recordings into actionable insights. It uses Whisper for accurate speech-to-text transcription and LLaMA 2 for intelligent summarization and action item extraction.

The application runs entirely locally, ensuring data privacy and eliminating API costs. It uses Ollama to host the LLaMA 2 model, Whisper for transcription, FastAPI for the backend API, and Streamlit for the user interface.

---

## Features

- **Audio Transcription** — Converts speech to text using OpenAI's Whisper
- **Meeting Summary** — Generates concise, AI-powered summaries
- **Action Item Extraction** — Identifies key tasks and responsibilities
- **Full Transcript** — Provides complete meeting transcript
- **Local Processing** — All processing happens locally, no data leaves your machine
- **Multiple Audio Formats** — Supports MP3, WAV, and M4A files
- **No API Costs** — Free to use with no usage limits

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **Whisper** | Speech-to-text transcription |
| **LLaMA 2** | Summarization and action item extraction |
| **Ollama** | Local LLM hosting and inference |
| **FFmpeg** | Audio processing and conversion |
| **FastAPI** | Backend API framework |
| **Streamlit** | Frontend user interface |
| **Requests** | HTTP client for API communication |
| **Uvicorn** | ASGI server for FastAPI |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Python** | Version 3.8 or higher |
| **Ollama** | Installed and running |
| **LLaMA 2 Model** | Downloaded via Ollama |
| **FFmpeg** | Installed and added to PATH |
| **RAM** | 8GB+ recommended |
| **Storage** | 5GB+ free space for models |

---

## FFmpeg Installation

### Windows

1. Download FFmpeg from: [gyan.dev/ffmpeg/builds](https://www.gyan.dev/ffmpeg/builds/)
2. Download the **"ffmpeg-release-full.7z"** file
3. Extract it to `C:\ffmpeg`
4. Add `C:\ffmpeg\bin` to your system PATH

**Verify installation:**

```bash
ffmpeg -version
```

### Mac

```bash
brew install ffmpeg
```

### Ubuntu

```bash
sudo apt install ffmpeg
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Esha-Mirza/School_Of_AI_Internship.git
cd School_Of_AI_Internship/"Project-5 Meeting Notes AI"
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

This downloads the LLaMA 2 model (~3.8 GB).

### 5. Verify FFmpeg is Installed

```bash
ffmpeg -version
```

---

## Running the Application

**Terminal 1: Start Ollama Service**

```bash
ollama serve
```

**Terminal 2: Start Backend (FastAPI)**

```bash
uvicorn backend.main:app --reload
```

The backend will be available at: `http://localhost:8000`

**Terminal 3: Start Frontend (Streamlit)**

```bash
streamlit run frontend/app.py
```

The frontend will open at: `http://localhost:8501`

---

## Usage

1. Open your browser and navigate to `http://localhost:8501`
2. Upload a meeting audio file (MP3, WAV, or M4A)
3. Click the **Generate Meeting Notes** button
4. Wait for processing (1-3 minutes depending on length)
5. View the generated summary, action items, and full transcript

---

## Supported Audio Formats

| Format | Extension |
|---|---|
| MP3 | `.mp3` |
| WAV | `.wav` |
| M4A | `.m4a` |

---

## Sample Output

**Summary:**

```text
The team discussed the Q4 marketing strategy, focusing on social media campaigns and budget allocation. Key decisions included increasing Instagram ad spend and launching a new product teaser campaign. Action items were assigned to team members with specific deadlines.
```

**Action Items:**

```text
1. Sarah: Prepare Instagram ad creative by Friday.
2. Mark: Finalize budget allocation for Q4 by Wednesday.
3. Emily: Draft product teaser campaign copy by Thursday.
4. John: Coordinate with external vendors for social media promotions.
```

---

## API Endpoints

### `POST /process/`

**Request:**

```python
files = {"file": audio_file_bytes}
```

**Response:**

```json
{
  "transcript": "Full meeting transcript...",
  "summary": "Concise meeting summary...",
  "action_items": "List of action items..."
}
```

---

## Project Structure

```
Project-5 Meeting Notes AI/
├── backend/
│   └── main.py          # FastAPI implementation
├── frontend/
│   └── app.py           # Streamlit UI
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## Configuration

### Changing Whisper Model

To use a different Whisper model, modify `backend/main.py`:

```python
model = whisper.load_model("base")    # Options: tiny, base, small, medium, large
```

### Changing the Port

**Backend Port** (default: 8000):

```bash
uvicorn backend.main:app --reload --port 8001
```

**Frontend Port** (default: 8501):

```bash
streamlit run frontend/app.py --server.port 8502
```

---

## Troubleshooting

| Issue | Solution |
|---|---|
| FFmpeg not found | Install FFmpeg and add to PATH |
| Model not found | Run `ollama pull llama2` to download the model |
| Connection refused | Ensure Ollama is running (`ollama serve`) |
| Port already in use | Use `--port` flag to specify a different port |
| Module not found | Run `pip install -r requirements.txt` |
| Slow processing | Use shorter audio files or switch to `tiny` Whisper model |
| Whisper model download | First run will download the Whisper model (~1 GB) |

---

## Roadmap

- [ ] Add speaker diarization (identify who said what)
- [ ] Export notes directly to PDF/DOCX
- [ ] Add calendar/email integration to auto-send meeting summaries

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Acknowledgments

- OpenAI Whisper - Speech recognition
- [Ollama](https://ollama.com/) - Local LLM runtime
- Meta - LLaMA 2 model
- FFmpeg - Audio processing
- FastAPI - Web framework
- Streamlit - UI framework

---

## Contact

- **GitHub:** [Esha-Mirza](https://github.com/Esha-Mirza)
- **Email:** esha101374@gmail.com
