"""
Summarizer Agent - Condenses findings into concise insights
"""

import requests

# Choose your model
MODEL = "llama2"  # or "mistral" or "phi3"

def summarize_text(text: str) -> str:
    """
    Summarize the provided text into key bullet points
    """
    
    prompt = f"""
You are a research summarizer. Review the following research findings and provide a concise summary in 3-5 bullet points.

Focus on:
- Key findings
- Important statistics
- Main trends
- Critical insights

Research findings:
{text}

Summary (3-5 bullet points):
"""
    
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            }
        )
        return response.json()["response"].strip()
    except Exception as e:
        return f"Error in summarization: {str(e)}"