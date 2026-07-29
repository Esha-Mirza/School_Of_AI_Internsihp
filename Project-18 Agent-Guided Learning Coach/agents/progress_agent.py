
from agents.base import call_llm, log_agent_response, get_topic_log

def run(topic: str) -> str:
    """Track progress and provide feedback"""
    
    log = get_topic_log(topic)
    
    if not log:
        return "No progress to track yet. Start learning! 📚"
    
    # Count interactions by agent
    agent_counts = {}
    for entry in log:
        agent = entry["agent"]
        agent_counts[agent] = agent_counts.get(agent, 0) + 1
    
    # Calculate progress
    total = len(log)
    learning_metrics = f"""
Total Learning Interactions: {total}

Breakdown:
- Explainer Agent: {agent_counts.get('Explainer Agent', 0)} explanations
- Quiz Agent: {agent_counts.get('Quiz Agent', 0)} quizzes taken
- Motivation Agent: {agent_counts.get('Motivation Agent', 0)} motivation sessions

Conversations by Agent:
{', '.join([f'{agent}: {count}' for agent, count in agent_counts.items()])}
"""
    
    prompt = f"""
You are a Progress Agent. Analyze the following learning progress and provide feedback.

{learning_metrics}

Based on this progress, provide:
1. Summary of what the student has learned
2. Strengths shown
3. Areas for improvement
4. Recommendations for next steps

Learning Progress Feedback:
"""
    
    feedback = call_llm(prompt)
    log_agent_response(topic, "Progress Agent", feedback)
    return feedback