
from agents.reflection_agent import run as reflection
from agents.cognitive_reframe_agent import run as reframe
from agents.wellness_tracker_agent import run as tracker
from agents.base import log_agent_response

def process_journal_entry(topic: str, mood: str, journal: str) -> dict:
    """
    Process a journal entry through all wellness agents
    
    Returns:
        Dictionary with all agent responses
    """
    results = {}
    
    # Step 1: Reflection
    reflection_result = reflection(topic, mood, journal)
    results["reflection"] = reflection_result
    
    # Step 2: Cognitive Reframe
    reframe_result = reframe(topic, mood, reflection_result)
    results["reframe"] = reframe_result
    
    return results

def get_wellness_report(topic: str) -> str:
    """Get wellness tracking report"""
    return tracker(topic)