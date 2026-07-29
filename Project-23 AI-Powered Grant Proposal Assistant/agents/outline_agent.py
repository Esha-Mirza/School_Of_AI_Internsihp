
from agents.base import call_llm, log_agent_response

def run(topic: str, goals: str, agency: str) -> str:
    """Design proposal outline"""
    
    prompt = f"""
You are a Grant Proposal Outline Designer. Create a comprehensive proposal outline.

Topic: {topic}
Goals: {goals}
Funding Agency: {agency}

Include sections:
1. Executive Summary
2. Introduction / Background
3. Problem Statement
4. Proposed Solution / Methodology
5. Timeline
6. Budget Overview
7. Evaluation Plan
8. Conclusion

Provide detailed prompts for each section.

Proposal Outline:
"""
    
    outline = call_llm(prompt)
    log_agent_response(topic, "Outline Designer", f"{topic}\n\n{outline}")
    return outline

def refine_outline(topic: str, outline: str, feedback: str) -> str:
    """Refine outline based on feedback"""
    
    prompt = f"""
You are a Grant Proposal Outline Designer. Refine this proposal outline based on feedback.

Current Outline:
{outline}

Feedback:
{feedback}

Provide the refined outline with improvements incorporated.

Refined Outline:
"""
    
    refined = call_llm(prompt)
    log_agent_response(topic, "Outline Designer (Refined)", refined)
    return refined