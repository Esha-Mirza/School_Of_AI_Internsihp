"""
Fact-Checker Agent - Reviews for hallucinations, bias, or gaps
"""

import requests

# Choose your model
MODEL = "llama2"  # or "mistral" or "phi3"

def fact_check(text: str) -> str:
    """
    Review the summary for accuracy, bias, and completeness
    """
    
    prompt = f"""
You are a fact-checker and quality assurance specialist. Review the following research summary and provide feedback on:

1. Accuracy: Are the facts correct?
2. Bias: Is there any bias or unbalanced perspective?
3. Completeness: Are there important gaps?
4. Clarity: Is the information clear and well-structured?

Provide specific suggestions for improvement.

Research summary:
{text}

Fact-checker feedback:
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
        return f"Error in fact-checking: {str(e)}"