
from agents.base import call_llm, log_agent_response

def run(topic: str, concept: str) -> str:
    """Explain a concept in simple, student-friendly language"""
    
    prompt = f"""
You are an Explainer Agent. Your job is to make complex concepts easy to understand for students.

Concept: {concept}

Provide a clear, simple explanation using:
1. Everyday language (no jargon)
2. Real-world examples
3. Simple analogies
4. Step-by-step breakdown if needed

Student-Friendly Explanation:
"""
    
    explanation = call_llm(prompt)
    log_agent_response(topic, "Explainer Agent", f"Explained: {concept}\n\n{explanation}")
    return explanation