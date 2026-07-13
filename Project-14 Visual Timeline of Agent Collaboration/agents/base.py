import requests
from tinydb import TinyDB, Query
from datetime import datetime

# Initialize database
db = TinyDB("memory/memory_store.json")
Topic = Query()

# Model configuration
MODEL = "llama2"  # or "mistral" or "phi3"

def call_llm(prompt: str) -> str:
    """Send prompt to Ollama and return response"""
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            }
        )
        return response.json()["response"].strip()
    except Exception as e:
        return f"Error: {str(e)}"

def log_agent_response(topic: str, agent: str, content: str):
    """Log agent response to shared memory with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if db.contains(Topic.name == topic):
        db.update(
            lambda t: t["log"].append({
                "agent": agent, 
                "content": content,
                "timestamp": timestamp
            }),
            Topic.name == topic
        )
    else:
        db.insert({
            "name": topic,
            "log": [{
                "agent": agent, 
                "content": content,
                "timestamp": timestamp
            }]
        })

def get_topic_log(topic: str):
    """Retrieve all agent responses for a topic"""
    result = db.search(Topic.name == topic)
    return result[0]["log"] if result else []

def get_all_topics() -> list:
    """Get all topic names"""
    return [item["name"] for item in db.all()]

def delete_topic(topic: str):
    """Delete a topic and its memory"""
    db.remove(Topic.name == topic)

def get_topic_by_name(topic: str):
    """Get full topic data including log"""
    result = db.search(Topic.name == topic)
    return result[0] if result else None