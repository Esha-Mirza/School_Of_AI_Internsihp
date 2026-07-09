"""
Orchestrator - Manages the multi-agent research pipeline
"""

from agents.search_agent import run_search
from agents.summarize_agent import summarize_text
from agents.checker_agent import fact_check
from agents.report_agent import generate_report

def run_research_pipeline(topic: str) -> dict:
    """
    Execute the complete multi-agent research pipeline
    
    Steps:
    1. Search Agent - Gathers raw information
    2. Summarizer Agent - Condenses findings
    3. Fact-Checker Agent - Reviews for accuracy
    4. Report Generator Agent - Creates final report
    """
    
    print(f"🔍 Starting research on: {topic}")
    
    # Step 1: Search
    print("📡 Agent 1: Searching for information...")
    search_results = run_search(topic)
    
    # Step 2: Summarize
    print("📝 Agent 2: Summarizing findings...")
    summary = summarize_text(search_results)
    
    # Step 3: Fact-check
    print("✅ Agent 3: Fact-checking summary...")
    corrections = fact_check(summary)
    
    # Step 4: Generate Report
    print("📄 Agent 4: Generating final report...")
    report = generate_report(summary, corrections)
    
    print("🎯 Research complete!")
    
    return {
        "topic": topic,
        "search": search_results,
        "summary": summary,
        "corrections": corrections,
        "report": report
    }