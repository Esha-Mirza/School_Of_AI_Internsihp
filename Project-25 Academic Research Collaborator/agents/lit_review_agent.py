
from agents.base import call_llm, log_agent_response

def run(topic: str, research_question: str, citations: str) -> str:
    """Conduct literature review"""
    
    prompt = f"""
You are a Literature Review Agent. Analyze the provided citations and literature.

Research Question: {research_question}

Citations/Literature:
{citations}

Provide:
1. **Key Themes** - What are the main themes in the literature?
2. **Gaps** - What gaps exist in the current research?
3. **Methodologies** - What methods are commonly used?
4. **Key Findings** - What are the main conclusions?
5. **Relevance** - How does this relate to the research question?

Literature Review:
"""
    
    review = call_llm(prompt)
    log_agent_response(topic, "Literature Review Agent", review)
    return review

def identify_gaps(topic: str, review: str) -> str:
    """Identify research gaps"""
    
    prompt = f"""
You are a Literature Review Agent. Based on the review, identify specific research gaps.

Literature Review:
{review}

Research Gaps:
1.
2.
3.
4.
5.
"""
    
    gaps = call_llm(prompt)
    log_agent_response(topic, "Literature Review Agent (Gaps)", gaps)
    return gaps