
from agents.base import call_llm, log_agent_response

def run(topic: str, updates: str) -> str:
    """Detect blockers and impediments"""
    
    prompt = f"""
You are a Blocker Detector Agent. Review the following team updates and identify blockers.

Team Updates:
{updates}

Identify:
1. **Active Blockers** - What is blocking progress?
2. **Potential Risks** - What might become blockers?
3. **Dependencies** - What does the team depend on?
4. **Recommendations** - How to resolve blockers?

Blocker Report:
"""
    
    blockers = call_llm(prompt)
    log_agent_response(topic, "Blocker Detector", blockers)
    return blockers