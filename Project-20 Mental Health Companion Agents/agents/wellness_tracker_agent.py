
from agents.base import call_llm, log_agent_response, get_topic_log
import json
from datetime import datetime

def extract_mood_entries(log: list) -> list:
    """Extract mood entries from logs"""
    moods = []
    
    for entry in log:
        if "Reflection Agent" in entry.get("agent", ""):
            content = entry.get("content", "")
            # Extract mood from reflection content
            if "Mood:" in content:
                mood_line = content.split("Mood:")[1].split("\n")[0].strip()
                moods.append({
                    "timestamp": entry.get("timestamp", ""),
                    "mood": mood_line,
                    "entry": content
                })
    
    return moods

def run(topic: str) -> str:
    """Track wellness trends over time"""
    
    log = get_topic_log(topic)
    
    if not log:
        return "No journal entries yet. Start writing to track your wellness! 💫"
    
    moods = extract_mood_entries(log)
    
    if not moods:
        return "No mood data found. Try journaling with mood tracking! 📝"
    
    # Analyze mood patterns
    mood_summary = f"""
Total Entries: {len(moods)}
Recent Moods: {', '.join([m['mood'] for m in moods[-5:]])}
"""
    
    prompt = f"""
You are a Wellness Tracker Agent. Analyze the following mood data and provide insights.

Mood Data:
{mood_summary}

Provide:
1. **Mood Trends** - What patterns do you see?
2. **Weekly Summary** - How has the week been?
3. **Insights** - Any correlations or observations?
4. **Gentle Recommendations** - Suggestions for maintaining well-being

Wellness Tracking Report:
"""
    
    report = call_llm(prompt)
    log_agent_response(topic, "Wellness Tracker Agent", report)
    return report

def get_mood_data(topic: str) -> dict:
    """Get mood data for visualization"""
    log = get_topic_log(topic)
    moods = extract_mood_entries(log)
    
    mood_values = {
        "😊 Excellent": 5,
        "😌 Good": 4,
        "😐 Okay": 3,
        "😔 Low": 2,
        "😢 Struggling": 1
    }
    
    mood_data = []
    for entry in moods:
        mood = entry.get("mood", "😐 Okay")
        value = mood_values.get(mood, 3)
        mood_data.append({
            "date": entry.get("timestamp", "").split()[0] if entry.get("timestamp") else "",
            "mood": mood,
            "value": value
        })
    
    return {
        "count": len(mood_data),
        "trend": mood_data,
        "mood_counts": {m: sum(1 for e in moods if e["mood"] == m) for m in mood_values.keys()}
    }