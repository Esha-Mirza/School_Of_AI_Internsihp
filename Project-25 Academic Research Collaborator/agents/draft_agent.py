
from agents.base import call_llm, log_agent_response, get_topic_log

def run(topic: str, draft: str, feedback: str = "") -> str:
    """Polish and improve draft"""
    
    if feedback:
        prompt = f"""
You are a Draft Polisher Agent. Revise this academic paper draft based on feedback.

Current Draft:
{draft}

Feedback:
{feedback}

Provide:
1. **Improved Draft** - With revisions incorporated
2. **Summary of Changes** - What was changed and why
3. **Next Steps** - What still needs work

Revised Draft:
"""
    else:
        prompt = f"""
You are a Draft Polisher Agent. Improve this academic paper draft.

Current Draft:
{draft}

Provide:
1. **Improved Draft** - With enhancements
2. **Suggestions** - For further improvement
3. **Areas for Expansion** - Where to add more detail

Polished Draft:
"""
    
    polished = call_llm(prompt)
    log_agent_response(topic, "Draft Polisher", polished)
    return polished

def get_writing_tips(topic: str) -> str:
    """Get academic writing tips"""
    
    prompt = f"""
You are a Draft Polisher Agent. Provide academic writing tips for the current draft.

Draft Topic: {topic}

Writing Tips:
"""
    
    tips = call_llm(prompt)
    log_agent_response(topic, "Draft Polisher (Tips)", tips)
    return tips