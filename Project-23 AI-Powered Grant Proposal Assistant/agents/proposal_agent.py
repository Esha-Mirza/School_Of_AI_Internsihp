
from agents.outline_agent import run as outline, refine_outline
from agents.budget_agent import run as budget
from agents.reviewer_agent import run as reviewer, simulate_scoring
from agents.base import log_agent_response, get_topic_log

def create_proposal(topic: str, goals: str, agency: str, duration: int, team_size: int) -> dict:
    """
    Create a complete grant proposal
    
    Returns:
        Dictionary with all agent responses
    """
    results = {}
    
    # Step 1: Create Outline
    outline_result = outline(topic, goals, agency)
    results["outline"] = outline_result
    
    # Step 2: Estimate Budget
    budget_result = budget(topic, goals, duration, team_size)
    results["budget"] = budget_result
    
    # Combine for review
    combined_text = f"Outline:\n{outline_result}\n\nBudget:\n{budget_result}"
    
    # Step 3: Simulate Reviewer
    review_result = reviewer(topic, combined_text, agency)
    results["review"] = review_result
    
    # Step 4: Simulate Scores
    scores_result = simulate_scoring(topic, combined_text)
    results["scores"] = scores_result
    
    return results

def get_proposal_history(topic: str):
    """Get proposal history"""
    return get_topic_log(topic)

def refine_proposal(topic: str, outline: str, feedback: str) -> str:
    """Refine proposal based on feedback"""
    return refine_outline(topic, outline, feedback)