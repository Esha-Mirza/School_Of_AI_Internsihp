
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from datetime import datetime
import json
import os
from tinydb import TinyDB, Query

# Database for scheduled workflows
scheduler_db = TinyDB("memory/scheduler_store.json")
Workflow = Query()

# Initialize scheduler
scheduler = BackgroundScheduler()

# Store for scheduled jobs
scheduled_jobs = {}

def get_workflows():
    """Get all saved workflows"""
    return scheduler_db.all()

def save_workflow(name: str, schedule_type: str, schedule_config: dict, agents: list, topic: str):
    """Save a workflow configuration"""
    
    workflow = {
        "name": name,
        "schedule_type": schedule_type,  # "cron" or "interval"
        "schedule_config": schedule_config,
        "agents": agents,
        "topic": topic,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "last_run": None,
        "next_run": None,
        "enabled": True,
        "run_history": []
    }
    
    if scheduler_db.contains(Workflow.name == name):
        scheduler_db.update(workflow, Workflow.name == name)
    else:
        scheduler_db.insert(workflow)
    
    return workflow

def delete_workflow(name: str):
    """Delete a workflow"""
    scheduler_db.remove(Workflow.name == name)
    if name in scheduled_jobs:
        scheduled_jobs[name].remove()
        del scheduled_jobs[name]

def run_workflow(name: str):
    """Execute a workflow"""
    workflow = scheduler_db.search(Workflow.name == name)
    
    if not workflow:
        return {"error": f"Workflow '{name}' not found"}
    
    workflow = workflow[0]
    
    if not workflow.get("enabled", True):
        return {"error": f"Workflow '{name}' is disabled"}
    
    from orchestrator import run_agent
    from agents.base import db, Topic
    
    # Run each agent in sequence
    results = {}
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    for agent in workflow["agents"]:
        try:
            # For Research Agent, use a default query
            if agent == "Research":
                result = run_agent(agent, workflow["topic"], "Provide a status update on this topic")
            else:
                result = run_agent(agent, workflow["topic"], "")
            
            results[agent] = {
                "result": result,
                "timestamp": timestamp,
                "status": "success"
            }
        except Exception as e:
            results[agent] = {
                "result": str(e),
                "timestamp": timestamp,
                "status": "error"
            }
    
    # Update workflow with run history
    run_entry = {
        "timestamp": timestamp,
        "results": results
    }
    
    scheduler_db.update(
        {
            "last_run": timestamp,
            "next_run": workflow.get("next_run", None),
            "run_history": workflow.get("run_history", []) + [run_entry]
        },
        Workflow.name == name
    )
    
    return {"status": "success", "results": results, "timestamp": timestamp}

def schedule_workflow(name: str):
    """Schedule a workflow to run"""
    workflow = scheduler_db.search(Workflow.name == name)
    
    if not workflow:
        return {"error": f"Workflow '{name}' not found"}
    
    workflow = workflow[0]
    
    # Remove existing job if any
    if name in scheduled_jobs:
        scheduled_jobs[name].remove()
        del scheduled_jobs[name]
    
    # Create new job based on schedule type
    if workflow["schedule_type"] == "cron":
        config = workflow["schedule_config"]
        trigger = CronTrigger(
            day=config.get("day", "*"),
            hour=config.get("hour", 8),
            minute=config.get("minute", 0)
        )
    else:  # interval
        config = workflow["schedule_config"]
        trigger = IntervalTrigger(
            days=config.get("days", 0),
            hours=config.get("hours", 24),
            minutes=config.get("minutes", 0)
        )
    
    # Add job to scheduler
    job = scheduler.add_job(
        run_workflow,
        trigger,
        args=[name],
        id=f"workflow_{name}",
        replace_existing=True
    )
    
    scheduled_jobs[name] = job
    
    # Update next run time
    next_run = job.next_run_time.strftime("%Y-%m-%d %H:%M:%S") if job.next_run_time else None
    
    scheduler_db.update(
        {"next_run": next_run},
        Workflow.name == name
    )
    
    return {"status": "success", "next_run": next_run}

def start_scheduler():
    """Start the background scheduler"""
    if not scheduler.running:
        scheduler.start()

def stop_scheduler():
    """Stop the background scheduler"""
    if scheduler.running:
        scheduler.shutdown()

def get_scheduler_status():
    """Get scheduler status and pending jobs"""
    jobs = []
    for job in scheduler.get_jobs():
        jobs.append({
            "id": job.id,
            "next_run": job.next_run_time.strftime("%Y-%m-%d %H:%M:%S") if job.next_run_time else None,
            "trigger": str(job.trigger)
        })
    
    return {
        "running": scheduler.running,
        "jobs": jobs
    }

def get_workflow_history(name: str):
    """Get run history for a workflow"""
    workflow = scheduler_db.search(Workflow.name == name)
    if workflow:
        return workflow[0].get("run_history", [])
    return []