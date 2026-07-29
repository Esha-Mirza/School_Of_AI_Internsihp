
from agents.base import call_llm, log_agent_response

def run(topic: str, destination: str, interests: str) -> str:
    """Provide cultural insights and local tips"""
    
    prompt = f"""
You are a Local Culture Coach Agent. Provide cultural insights for travelers.

Destination: {destination}
Traveler Interests: {interests}

Include:
1. **Local Customs** - Important cultural norms to know
2. **Language Tips** - Key phrases to learn
3. **Cultural Etiquette** - Do's and Don'ts
4. **Local Experiences** - Authentic activities to try
5. **Cultural Sensitivity** - How to be a respectful traveler

Cultural Guide:
"""
    
    culture = call_llm(prompt)
    log_agent_response(topic, "Local Culture Coach", f"{destination}\n\n{culture}")
    return culture

def get_phrase_guide(destination: str) -> str:
    """Get key phrases for the destination"""
    
    prompt = f"""
Provide 10 essential phrases for travelers visiting {destination}.

Include:
- Greetings
- Thank you / Please
- Where is...?
- How much?
- Help / Emergency

Format as English → Local Language.

Essential Phrases:
"""
    
    return call_llm(prompt)