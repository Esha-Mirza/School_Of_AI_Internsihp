
from agents.itinerary_agent import run as itinerary
from agents.cost_estimator_agent import run as cost_estimator
from agents.culture_agent import run as culture
from agents.base import log_agent_response, get_topic_log

def plan_trip(topic: str, destination: str, duration: int, interests: str, budget: str) -> dict:
    """
    Run all travel agents to plan a complete trip
    
    Returns:
        Dictionary with all agent responses
    """
    results = {}
    
    # Step 1: Build Itinerary
    itinerary_plan = itinerary(topic, destination, duration, interests, budget)
    results["itinerary"] = itinerary_plan
    
    # Step 2: Estimate Costs
    cost_estimate = cost_estimator(topic, destination, duration, budget, interests)
    results["cost"] = cost_estimate
    
    # Step 3: Cultural Guide
    culture_guide = culture(topic, destination, interests)
    results["culture"] = culture_guide
    
    return results

def get_trip_history(topic: str):
    """Get trip planning history"""
    return get_topic_log(topic)