
from agents.summary_agent import run as summary
from agents.blocker_agent import run as blocker
from agents.sprint_agent import run as sprint
from agents.base import log_agent_response, get_topic_log

def process_standup(topic: str, updates: str) -> dict:
    """
    Process standup updates through all agents
    
    Returns:
        Dictionary with all agent responses
    """
    results = {}
    
    # Step 1: Generate Summary
    summary_result = summary(topic, updates)
    results["summary"] = summary_result
    
    # Step 2: Detect Blockers
    blocker_result = blocker(topic, updates)
    results["blockers"] = blocker_result
    
    # Step 3: Sprint Progress
    sprint_result = sprint(topic, updates)
    results["sprint"] = sprint_result
    
    return results

def get_standup_history(topic: str):
    """Get standup history"""
    return get_topic_log(topic)

def get_sprint_stats(topic: str):
    """Get sprint statistics"""
    logs = get_topic_log(topic)
    
    days = {}
    for entry in logs:
        date = entry.get("timestamp", "").split()[0]
        if date:
            days[date] = days.get(date, 0) + 1
    
    return {
        "total_entries": len(logs),
        "active_days": len(days),
        "teammates": list(set([e.get("agent", "") for e in logs]))
    }