
from agents.resume_agent import run as resume, optimize_bullet_points
from agents.interview_agent import run as interview, generate_feedback
from agents.fit_agent import run as fit_analysis
from agents.base import log_agent_response, get_topic_log

def process_resume(topic: str, resume_text: str, role: str) -> dict:
    """Process resume through resume agent"""
    results = {}
    
    resume_result = resume(topic, resume_text, role)
    results["resume"] = resume_result
    
    return results

def conduct_interview(topic: str, role: str, question: str = None, answer: str = None) -> dict:
    """Conduct mock interview"""
    results = {}
    
    if question and answer:
        # Provide feedback
        feedback = generate_feedback(topic, role, question, answer)
        results["feedback"] = feedback
    else:
        # Generate questions
        questions = interview(topic, role)
        results["questions"] = questions
    
    return results

def analyze_fit(topic: str, resume_text: str, job_description: str) -> dict:
    """Analyze role fit"""
    results = {}
    
    fit_result = fit_analysis(topic, resume_text, job_description)
    results["fit"] = fit_result
    
    return results

def get_career_history(topic: str):
    """Get career history"""
    return get_topic_log(topic)