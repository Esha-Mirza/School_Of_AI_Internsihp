
from agents.base import call_llm, log_agent_response

def run(topic: str, destination: str, duration: int, budget: str, interests: str) -> str:
    """Estimate costs for the trip"""
    
    prompt = f"""
You are a Cost Estimator Agent. Estimate the costs for a trip.

Destination: {destination}
Trip Duration: {duration} days
Budget Level: {budget}
Traveler Interests: {interests}

Provide cost estimates for:
1. **Accommodation** - Per night and total
2. **Food** - Per day and total
3. **Transportation** - Local + flights
4. **Activities** - Per day and total
5. **Total Estimated Cost**

Also include:
- Money-saving tips
- Hidden costs to watch for
- Where to splurge vs save

Cost Breakdown:
"""
    
    estimate = call_llm(prompt)
    log_agent_response(topic, "Cost Estimator", f"{destination}\n\n{estimate}")
    return estimate

def get_budget_tips(budget: str) -> str:
    """Get budget-specific travel tips"""
    
    prompt = f"""
Provide travel money-saving tips for a {budget} budget traveler.

Include:
- Daily budget targets
- Money-saving hacks
- Free activities
- Best value options

Budget Travel Tips:
"""
    
    return call_llm(prompt)