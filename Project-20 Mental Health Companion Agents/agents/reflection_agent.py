
from agents.base import call_llm, log_agent_response

def run(topic: str, mood: str, journal: str) -> str:
    """Reflect on mood and journal entry"""
    
    prompt = f"""
You are a Reflection Agent. Help the user reflect on their daily journal entry.

Mood: {mood}

Journal Entry:
{journal}

Provide:
1. **Emotional Summary** - What emotions are present?
2. **Key Themes** - What are the main topics or concerns?
3. **Pattern Recognition** - Any recurring thoughts or feelings?
4. **Validation** - Acknowledge and validate their experience

Reflection:
"""
    
    reflection = call_llm(prompt)
    log_agent_response(topic, "Reflection Agent", f"Mood: {mood}\n\nReflection: {reflection}")
    return reflection