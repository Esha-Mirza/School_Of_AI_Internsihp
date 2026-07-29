
from agents.base import call_llm, log_agent_response

def run(topic: str, log_data: str) -> str:
    """Parse and analyze system logs/alerts"""
    
    prompt = f"""
You are a Log Parser Agent. Analyze the following system logs or security alerts and provide:

1. **Summary of Events** - What happened?
2. **Severity Assessment** - Critical/High/Medium/Low
3. **Key Indicators** - Suspicious IPs, users, timestamps, patterns
4. **Potential Attack Vectors** - What type of attack is this?

Log Data:
{log_data[:3000]}

Security Incident Analysis:
"""
    
    analysis = call_llm(prompt)
    log_agent_response(topic, "Log Parser Agent", analysis)
    return analysis