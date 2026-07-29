

from agents.base import call_llm, log_agent_response, get_topic_log

def run(topic: str, proposal_text: str, agency: str) -> str:
    """Simulate reviewer feedback"""
    
    prompt = f"""
You are a Grant Reviewer Simulator. Review this proposal as if you work for the funding agency.

Funding Agency: {agency}

Proposal:
{proposal_text}

Provide feedback on:
1. Strengths
2. Weaknesses
3. Clarity of goals
4. Feasibility
5. Budget justification
6. Overall score (1-10)
7. Recommendations for improvement

Reviewer Feedback:
"""
    
    feedback = call_llm(prompt)
    log_agent_response(topic, "Reviewer Simulator", feedback)
    return feedback

def simulate_scoring(topic: str, proposal_text: str) -> str:
    """Generate simulated review scores"""
    
    prompt = f"""
You are a Grant Reviewer Simulator. Score this proposal based on typical reviewer criteria.

Proposal:
{proposal_text}

Provide scores (0-10) for:
1. Significance
2. Innovation
3. Approach
4. Investigator Qualifications
5. Environment
6. Budget Justification

Also provide a total score and brief justification.

Review Scores:
"""
    
    scores = call_llm(prompt)
    log_agent_response(topic, "Reviewer Simulator (Scores)", scores)
    return scores