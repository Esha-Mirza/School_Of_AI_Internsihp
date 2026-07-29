
from agents.base import call_llm, log_agent_response

def run(topic: str, goals: str, duration: int, team_size: int) -> str:
    """Estimate budget"""
    
    prompt = f"""
You are a Grant Budget Estimator. Create a detailed budget estimate.

Topic: {topic}
Goals: {goals}
Project Duration: {duration} months
Team Size: {team_size}

Include:
1. Personnel Costs (salaries, benefits)
2. Equipment / Materials
3. Travel / Fieldwork
4. Participant Costs (if applicable)
5. Administrative Overhead
6. Total Budget

Provide a detailed breakdown with justifications.

Budget Estimate:
"""
    
    budget = call_llm(prompt)
    log_agent_response(topic, "Budget Estimator", budget)
    return budget