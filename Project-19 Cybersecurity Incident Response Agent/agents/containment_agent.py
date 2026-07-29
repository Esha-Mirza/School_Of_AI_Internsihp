
from agents.base import call_llm, log_agent_response, get_topic_log

def run(topic: str, incident_data: str) -> str:
    """Recommend containment and response actions"""
    
    prompt = f"""
You are a Containment Advisor Agent. Based on the incident data, provide:

1. **Immediate Actions** - What to do right now (5-10 min)
2. **Containment Steps** - How to prevent further damage
3. **Eradication Recommendations** - How to remove the threat
4. **Recovery Plan** - How to restore systems
5. **Prevention Measures** - How to prevent recurrence

Incident Data:
{incident_data}

Incident Response Plan:
"""
    
    recommendations = call_llm(prompt)
    log_agent_response(topic, "Containment Advisor Agent", recommendations)
    return recommendations