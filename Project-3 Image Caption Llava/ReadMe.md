# Image Caption Generator AI

An AI-powered image captioning application that uses a locally hosted LLaVA vision-language model to generate natural-language descriptions for uploaded images.

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
- [Supported Image Formats](#supported-image-formats)
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

This application leverages a vision-language model (LLaVA) to automatically generate descriptive captions for images. It is designed for content creators, accessibility tools, researchers, and anyone who needs to automatically describe visual content.

The application runs entirely locally, ensuring data privacy and eliminating API costs. It uses Ollama to host the LLaVA model, FastAPI for the backend API, and Streamlit for the user interface.

---

## Features

- **Vision-Language Model** — Uses LLaVA to understand both images and text
- **Local Inference** — Runs entirely locally using Ollama, ensuring complete data privacy
- **Multiple Format Support** — Upload PNG, JPG, JPEG, and WEBP images
- **FastAPI Backend** — Provides a RESTful API for image captioning
- **Streamlit Frontend** — Clean, intuitive user interface
- **Privacy-Focused** — All processing happens locally, no data is sent to external servers
- **No API Costs** — Free to use with no usage limits

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **Ollama** | Local LLM hosting and inference |
| **LLaVA** | Vision-language model for image understanding |
| **FastAPI** | Backend API framework |
| **Streamlit** | Frontend user interface |
| **Pillow** | Image processing and handling |
| **Requests** | HTTP client for API communication |
| **Uvicorn** | ASGI server for FastAPI |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Python** | Version 3.8 or higher |
| **Ollama** | Installed and running |
| **LLaVA Model** | Downloaded via Ollama |
| **RAM** | 8GB+ recommended (16GB for optimal performance) |
| **Storage** | 5GB+ free space for model |

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Esha-Mirza/School_Of_AI_Internship.git
cd School_Of_AI_Internship/"Project-3 Image Caption Llava"
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

### 4. Pull LLaVA Model via Ollama

```bash
ollama pull llava
```

This downloads the LLaVA model (~4.5 GB).

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
2. Click the **Choose an image** button
3. Select an image (PNG, JPG, JPEG, or WEBP)
4. Click the **Generate Caption** button
5. Wait for the AI to generate the caption

---

## Supported Image Formats

| Format | Extension |
|---|---|
| PNG | `.png` |
| JPEG | `.jpg`, `.jpeg` |
| WEBP | `.webp` |

---

## Sample Output

**Input Image:** A photo of a dog running in a park

**Generated Caption:**

```text
A brown dog running through a green grassy field with trees in the background.
```

---

## API Endpoints

### `POST /caption/`

**Request:**

```python
files = {"file": image_bytes}
```

**Response:**

```json
{
  "caption": "Generated caption text..."
}
```

---

## Project Structure

```
Project-3 Image Caption Llava/
├── backend/
│   └── main.py          # FastAPI implementation
├── frontend/
│   └── app.py           # Streamlit UI
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## Configuration

### Changing the Model

To use a different vision model, modify `backend/main.py`:

```python
"model": "bakllava",    # Change from "llava" to your preferred model
```

### Changing the Prompt

To customize the caption style, modify `backend/main.py`:

```python
"prompt": "Describe this image in detail in one sentence.",  # Customize your prompt
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
| Model not found | Run `ollama pull llava` to download the model |
| Connection refused | Ensure Ollama is running (`ollama serve`) |
| Image upload error | Ensure file is under 5MB and in supported format |
| Port already in use | Use `--port` flag to specify a different port |
| Module not found | Run `pip install -r requirements.txt` |
| Slow inference | LLaVA is a large model — be patient; it may take 15-30 seconds per image |

---

## Roadmap

- [ ] Add batch captioning for multiple images at once
- [ ] Add alt-text export mode for accessibility/web use cases
- [ ] Support custom caption tone (formal, casual, descriptive, SEO-style)

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Acknowledgments

- [Ollama](https://ollama.com/) - Local LLM runtime
- LLaVA - Vision-language model
- FastAPI - Web framework
- Streamlit - UI framework

---

## Contact

- **GitHub:** [Esha-Mirza](https://github.com/Esha-Mirza)
- **Email:** esha101374@gmail.com
