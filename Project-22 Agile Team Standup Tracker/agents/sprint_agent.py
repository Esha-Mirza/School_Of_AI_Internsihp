
from agents.base import call_llm, log_agent_response, get_topic_log

def run(topic: str, updates: str) -> str:
    """Estimate sprint progress"""
    
    prompt = f"""
You are a Sprint Progress Estimator. Analyze the following team updates.

Team Updates:
{updates}

Provide:
1. **Sprint Health** - How is the sprint progressing?
2. **Velocity Assessment** - Are we on track?
3. **Completion Forecast** - Will we complete the sprint goals?
4. **Recommendations** - How to improve?

Sprint Progress Report:
"""
    
    progress = call_llm(prompt)
    log_agent_response(topic, "Sprint Progress Estimator", progress)
    return progress

def get_sprint_summary(logs: list) -> dict:
    """Get sprint statistics"""
    
    daily_updates = []
    for entry in logs:
        if "Summary Agent" in entry.get("agent", ""):
            daily_updates.append(entry)
    
    return {
        "total_updates": len(daily_updates),
        "days_active": len(set([d.get("timestamp", "").split()[0] for d in daily_updates])),
        "latest_update": daily_updates[-1].get("content", "") if daily_updates else None
    }