
from agents.base import call_llm, log_agent_response
from datetime import datetime

def run(topic: str, destination: str, duration: int, interests: str, budget: str) -> str:
    """Build a daily itinerary for the trip"""
    
    prompt = f"""
You are an Itinerary Builder Agent. Create a detailed day-by-day travel itinerary.

Destination: {destination}
Trip Duration: {duration} days
Traveler Interests: {interests}
Budget Level: {budget}

For each day, include:
- Morning activities
- Afternoon activities
- Evening activities
- Meal suggestions
- Transportation notes

Format with clear day headings.

Day-by-Day Itinerary:
"""
    
    itinerary = call_llm(prompt)
    log_agent_response(topic, "Itinerary Builder", f"{destination}\n\n{itinerary}")
    return itinerary

def get_trip_summary(destination: str, duration: int) -> str:
    """Get a quick trip summary"""
    
    prompt = f"""
Provide a brief summary for a {duration}-day trip to {destination}.

Include:
- Best time to visit
- Must-see attractions
- Local cuisine to try
- Cultural tips

Quick Trip Summary:
"""
    
    return call_llm(prompt)