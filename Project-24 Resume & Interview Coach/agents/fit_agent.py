
from agents.base import call_llm, log_agent_response, get_topic_log

def run(topic: str, resume_text: str, job_description: str) -> str:
    """Analyze role fit"""
    
    prompt = f"""
You are a Role-Fit Analyzer Agent. Analyze how well the candidate fits this role.

Resume:
{resume_text}

Job Description:
{job_description}

Provide:
1. **Skills Match** - What skills match perfectly?
2. **Skills Gap** - What skills are missing?
3. **Experience Match** - How well does experience align?
4. **Cultural Fit Indicators** - What suggests cultural fit?
5. **Recommendations** - How to bridge gaps?
6. **Overall Fit Score** (1-10)

Role-Fit Analysis:
"""
    
    analysis = call_llm(prompt)
    log_agent_response(topic, "Role-Fit Analyzer", analysis)
    return analysis

def get_fit_summary(topic: str) -> str:
    """Get fit summary over time"""
    log = get_topic_log(topic)
    
    if not log:
        return "No analysis yet"
    
    fit_entries = [e for e in log if "Role-Fit" in e.get("agent", "")]
    
    if not fit_entries:
        return "No fit analysis available"
    
    summary = f"""
Total Fit Analyses: {len(fit_entries)}
Latest Analysis: {fit_entries[-1].get('timestamp', 'Unknown')}
"""
    
    return summary