"""
Quiz Agent - Generates questions to test understanding
"""

from agents.base import call_llm, log_agent_response

def run(topic: str, concept: str) -> str:
    """Generate quiz questions based on the concept"""
    
    prompt = f"""
You are a Quiz Agent. Generate 5 quiz questions to test understanding of the following concept.

Concept: {concept}

For each question:
1. Question
2. 4 options (A, B, C, D)
3. Correct answer
4. Brief explanation of why the answer is correct

Format as:
Q1: [Question]
A) [Option]
B) [Option]
C) [Option]
D) [Option]
Answer: [Letter] - [Explanation]

Quiz Questions:
"""
    
    questions = call_llm(prompt)
    log_agent_response(topic, "Quiz Agent", f"Quiz on: {concept}\n\n{questions}")
    return questions

def run_by_level(topic: str, concept: str, level: str = "medium") -> str:
    """Generate quiz questions at specific difficulty level"""
    
    prompt = f"""
You are a Quiz Agent. Generate {level} difficulty quiz questions to test understanding of the following concept.

Concept: {concept}
Difficulty: {level} (easy, medium, or hard)

Generate 5 questions at {level} difficulty level.

Quiz Questions ({level}):
"""
    
    questions = call_llm(prompt)
    log_agent_response(topic, "Quiz Agent", f"Quiz ({level}) on: {concept}\n\n{questions}")
    return questions