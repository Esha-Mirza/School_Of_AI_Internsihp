
from agents.base import call_llm, log_agent_response, get_topic_log

def run(topic: str, role: str, question: str = None) -> str:
    """Conduct mock interview"""
    
    if question:
        # Answer specific question
        prompt = f"""
You are a Behavioral Interview Agent. Answer this interview question for a {role} position.

Question: {question}

Provide a structured answer using STAR method:
- Situation
- Task
- Action
- Result

Your Answer:
"""
        answer = call_llm(prompt)
        return answer
    else:
        # Generate questions
        prompt = f"""
You are a Behavioral Interview Agent. Generate 5 common behavioral interview questions for a {role} position.

Include questions about:
1. Leadership
2. Problem-solving
3. Teamwork
4. Conflict resolution
5. Adaptability

Interview Questions:
"""
        
        questions = call_llm(prompt)
        log_agent_response(topic, "Interview Agent", f"{role}\n\n{questions}")
        return questions

def generate_feedback(topic: str, role: str, question: str, answer: str) -> str:
    """Generate feedback on interview answer"""
    
    prompt = f"""
You are a Behavioral Interview Agent. Provide feedback on this interview answer.

Position: {role}
Question: {question}
Candidate's Answer: {answer}

Provide:
1. **Strengths** - What was effective?
2. **Areas for Improvement** - What could be better?
3. **STAR Method Compliance** - How well did they use STAR?
4. **Key Takeaway** - One main improvement
5. **Score** (1-10)

Interview Feedback:
"""
    
    feedback = call_llm(prompt)
    log_agent_response(topic, "Interview Agent (Feedback)", feedback)
    return feedback

def get_interview_history(topic: str):
    """Get interview history"""
    return get_topic_log(topic)