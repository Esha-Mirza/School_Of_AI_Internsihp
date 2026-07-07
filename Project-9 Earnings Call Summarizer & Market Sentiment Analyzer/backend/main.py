from fastapi import FastAPI, Form
import requests

app = FastAPI()

def query_model(prompt: str):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"].strip()

@app.post("/analyze/")
def analyze_call(text: str = Form(...)):
    prompts = {
        "summary": (
            "Summarize the following earnings call transcript in 3 sentences:\n\n"
            f"{text}"
        ),
        "sentiment": (
            "What is the overall sentiment of this earnings call? "
            "Respond with Positive, Neutral, or Negative:\n\n"
            f"{text}"
        ),
        "insights": (
            "Extract key financial insights such as growth signals, risks, "
            "revenue trends, and forward guidance:\n\n"
            f"{text}"
        )
    }

    results = {key: query_model(prompt) for key, prompt in prompts.items()}
    return results