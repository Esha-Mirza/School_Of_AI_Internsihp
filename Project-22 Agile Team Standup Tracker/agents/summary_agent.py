

from agents.base import call_llm, log_agent_response

def run(topic: str, updates: str) -> str:
    """Summarize team updates"""
    
    prompt = f"""
You are a Standup Summary Agent. Summarize the following team updates.

Team Updates:
{updates}

Provide:
1. **Overall Summary** - What's happening across the team?
2. **Key Highlights** - Major wins or progress
3. **Team Velocity** - How is the team progressing?
4. **Focus Areas** - What should the team focus on?

Team Summary:
"""
    
    summary = call_llm(prompt)
    log_agent_response(topic, "Summary Agent", summary)
    return summary