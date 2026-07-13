from agents import (
    reasearch_agent,
    summarize_agent,
    devil_agent,
    insight_agent
)
from agents.base import get_topic_log, get_all_topics, delete_topic, get_topic_by_name

def run_agent(agent: str, topic: str, query: str = ""):
    if agent == "Research":
        return reasearch_agent.run(topic, query)
    elif agent == "Summarizer":
        return summarize_agent.run(topic)
    elif agent == "Devil":
        return devil_agent.run(topic)
    elif agent == "Insight":
        return insight_agent.run(topic)
    return "Unknown agent."

def get_topic_memory(topic: str) -> list:
    """Get full memory log for a topic"""
    return get_topic_log(topic)

def get_topic_list() -> list:
    """Get all topics with message counts"""
    all_topics = get_all_topics()
    topic_info = []
    
    for topic in all_topics:
        log = get_topic_log(topic)
        topic_info.append({
            "name": topic,
            "message_count": len(log)
        })
    
    return topic_info

def delete_topic_memory(topic: str) -> None:
    """Delete a topic and its memory"""
    delete_topic(topic)

def get_topic_data(topic: str):
    """Get full topic data including log"""
    return get_topic_by_name(topic)