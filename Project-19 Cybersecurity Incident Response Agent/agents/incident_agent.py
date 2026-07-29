
from agents.log_parser_agent import run as log_parser
from agents.threat_intel_agent import run as threat_intel
from agents.containment_agent import run as containment
from agents.base import log_agent_response, get_topic_log

def run_incident_response(topic: str, log_data: str) -> dict:
    """
    Run all incident response agents in sequence
    
    Returns:
        Dictionary with all agent responses
    """
    results = {}
    
    # Step 1: Parse logs
    log_analysis = log_parser(topic, log_data)
    results["log_analysis"] = log_analysis
    
    # Step 2: Threat intelligence
    threat_report = threat_intel(topic, log_analysis)
    results["threat_report"] = threat_report
    
    # Step 3: Containment recommendations
    combined_data = f"Log Analysis:\n{log_analysis}\n\nThreat Report:\n{threat_report}"
    containment_plan = containment(topic, combined_data)
    results["containment_plan"] = containment_plan
    
    return results

def get_incident_history(topic: str):
    """Get incident history"""
    return get_topic_log(topic)