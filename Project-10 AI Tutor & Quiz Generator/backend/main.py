from fastapi import FastAPI, Form
import requests

app = FastAPI()

def query_model(prompt: str):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",  # or "llama2"
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"].strip()

@app.post("/generate/")
def generate_learning_aids(text: str = Form(...)):
    prompts = {
        "explanation": (
            "Explain the following content in simple, student-friendly language:\n\n"
            f"{text}"
        ),
        "quiz": (
            "Generate 5 quiz questions with answers based on this educational content:\n\n"
            f"{text}"
        ),
        "concepts": (
            "List the key terms or concepts mentioned in this content:\n\n"
            f"{text}"
        )
    }

    return {key: query_model(prompt) for key, prompt in prompts.items()}
