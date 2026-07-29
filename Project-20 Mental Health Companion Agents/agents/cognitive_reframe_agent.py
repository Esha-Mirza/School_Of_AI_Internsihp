
from agents.base import call_llm, log_agent_response

def run(topic: str, mood: str, reflection: str) -> str:
    """Offer cognitive reframing and perspective"""
    
    prompt = f"""
You are a Cognitive Reframe Agent. Help the user gain a new perspective on their thoughts.

Mood: {mood}
User's Reflection: {reflection}

Provide:
1. **Alternative Perspectives** - How else could this be viewed?
2. **Cognitive Reframing** - Gentle reframing of any negative patterns
3. **Balanced View** - Acknowledge both challenges and strengths
4. **Actionable Perspective** - A new way to think about this

Cognitive Reframe:
"""
    
    reframe = call_llm(prompt)
    log_agent_response(topic, "Cognitive Reframe Agent", reframe)
    return reframe