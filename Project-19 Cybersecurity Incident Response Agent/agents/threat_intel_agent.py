

from agents.base import call_llm, log_agent_response, get_topic_log

def run(topic: str, incident_summary: str) -> str:
    """Provide threat intelligence context"""
    
    prompt = f"""
You are a Threat Intelligence Agent. Based on the incident summary provided, give:
1. **Threat Actor Profile** - Who might be behind this?
2. **Known TTPs** - Tactics, Techniques, and Procedures
3. **Industry Impact** - How does this affect the sector?
4. **Recent Similar Incidents** - Any known related attacks?

Incident Summary:
{incident_summary}

Threat Intelligence Report:
"""
    
    intelligence = call_llm(prompt)
    log_agent_response(topic, "Threat Intelligence Agent", intelligence)
    return intelligence