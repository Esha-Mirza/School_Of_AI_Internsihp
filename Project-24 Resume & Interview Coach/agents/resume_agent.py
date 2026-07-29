
from agents.base import call_llm, log_agent_response

def run(topic: str, resume_text: str, role: str) -> str:
    """Analyze and optimize resume"""
    
    prompt = f"""
You are a Resume Optimizer Agent. Analyze and improve this resume.

Target Role: {role}

Resume:
{resume_text}

Provide:
1. **Strengths** - What's working well?
2. **Weaknesses** - What needs improvement?
3. **Keyword Optimization** - What keywords are missing?
4. **Bullet Point Improvements** - Rewrite weak bullet points
5. **Formatting Tips** - Layout and structure suggestions
6. **Overall Score** (1-10)

Resume Optimization Report:
"""
    
    analysis = call_llm(prompt)
    log_agent_response(topic, "Resume Optimizer", f"{role}\n\n{analysis}")
    return analysis

def optimize_bullet_points(topic: str, bullet_points: str, role: str) -> str:
    """Optimize bullet points"""
    
    prompt = f"""
You are a Resume Optimizer Agent. Rewrite these bullet points for maximum impact.

Target Role: {role}
Current Bullet Points:
{bullet_points}

Provide improved versions using:
- Action verbs
- Quantifiable results
- Impact-focused language

Optimized Bullet Points:
"""
    
    optimized = call_llm(prompt)
    log_agent_response(topic, "Resume Optimizer (Bullet Points)", optimized)
    return optimized