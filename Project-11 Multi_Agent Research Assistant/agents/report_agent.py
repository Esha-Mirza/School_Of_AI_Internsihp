"""
Report Generator Agent - Produces a polished final research brief
"""

import requests

# Choose your model
MODEL = "llama2"  # or "mistral" or "phi3"

def generate_report(summary: str, corrections: str) -> str:
    """
    Generate a polished executive-style research report
    """
    
    prompt = f"""
You are a professional report writer. Using the summary and fact-checker feedback below, produce a polished, executive-style research report.

Include:
- Executive summary
- Key findings
- Supporting details
- Recommendations
- Conclusion

Format professionally with clear sections.

SUMMARY:
{summary}

FACT-CHECKER FEEDBACK:
{corrections}

EXECUTIVE RESEARCH REPORT:
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
        return f"Error in report generation: {str(e)}"