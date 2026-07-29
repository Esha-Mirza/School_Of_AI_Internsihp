
from agents.base import call_llm, log_agent_response
import random

def run(topic: str, progress: str = "Just starting") -> str:
    """Provide motivation and encouragement based on progress"""
    
    random_encouragement = random.choice([
        "Every expert was once a beginner. Keep going! 🌟",
        "The beautiful thing about learning is that no one can take it away from you. 📚",
        "Don't worry about being perfect. Just focus on getting better every day. 💪",
        "Success is the sum of small efforts repeated day in and day out. 🎯",
        "Your potential is endless. Keep pushing forward! 🚀"
    ])
    
    prompt = f"""
You are a Motivation Agent. Provide encouragement and practical learning advice to a student.

Student's Progress: {progress}

Include:
1. Encouragement based on their progress
2. Practical study tips
3. Mindset advice
4. One short, inspiring quote

Motivational Message:
"""
    
    motivation = call_llm(prompt)
    log_agent_response(topic, "Motivation Agent", motivation)
    
    return f"{random_encouragement}\n\n{motivation}"