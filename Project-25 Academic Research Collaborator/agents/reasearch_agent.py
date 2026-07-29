
from agents.lit_review_agent import run as lit_review, identify_gaps
from agents.hypothesis_agent import run as validate_hypothesis, generate_hypotheses
from agents.draft_agent import run as polish_draft, get_writing_tips
from agents.base import log_agent_response, get_topic_log

def process_research(topic: str, research_question: str, citations: str, draft: str = "") -> dict:
    """
    Process research through all agents
    
    Returns:
        Dictionary with all agent responses
    """
    results = {}
    
    # Step 1: Literature Review
    review = lit_review(topic, research_question, citations)
    results["review"] = review
    
    # Step 2: Identify Gaps
    gaps = identify_gaps(topic, review)
    results["gaps"] = gaps
    
    # Step 3: Generate Hypotheses
    hypotheses = generate_hypotheses(topic, research_question)
    results["hypotheses"] = hypotheses
    
    # Step 4: Polish Draft (if provided)
    if draft:
        polished = polish_draft(topic, draft)
        results["polished_draft"] = polished
    
    return results

def validate_hypothesis(topic: str, hypothesis: str, evidence: str) -> str:
    """Validate a specific hypothesis"""
    return validate_hypothesis(topic, hypothesis, evidence)

def polish_draft_with_feedback(topic: str, draft: str, feedback: str) -> str:
    """Polish draft with feedback"""
    return polish_draft(topic, draft, feedback)

def get_research_history(topic: str):
    """Get research history"""
    return get_topic_log(topic)