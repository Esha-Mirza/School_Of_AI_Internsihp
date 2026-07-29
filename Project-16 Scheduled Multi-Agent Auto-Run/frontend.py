import streamlit as st
from orchestrator import run_agent, get_topic_memory, get_topic_list, delete_topic_memory
from scheduler import (
    get_workflows, 
    save_workflow, 
    delete_workflow,
    schedule_workflow,
    start_scheduler,
    get_scheduler_status,
    get_workflow_history,
    run_workflow
)
from datetime import datetime
import pandas as pd

st.set_page_config(
    page_title="AthenaCore Agent Workflow",
    page_icon="⏰",
    layout="wide"
)

st.title("⏰ AthenaCore: Scheduled Agent Workflow Engine")
st.markdown("*Automate your research with scheduled agent runs*")

# Start scheduler automatically
start_scheduler()

# Session state initialization
if "topic" not in st.session_state:
    st.session_state.topic = None

# Sidebar
with st.sidebar:
    st.header("📂 Topics")
    
    topics = get_topic_list()
    
    if topics:
        for t in topics:
            if st.button(f"📁 {t['name']} ({t['message_count']})", key=f"topic_{t['name']}"):
                st.session_state.topic = t['name']
                st.rerun()
    else:
        st.info("No topics yet. Create one!")
    
    st.markdown("---")
    st.header("➕ New Topic")
    new_topic = st.text_input("Enter new topic name:")
    if st.button("Create Topic"):
        if new_topic:
            st.session_state.topic = new_topic
            st.rerun()
    
    st.markdown("---")
    st.header("📊 Scheduler Status")
    
    status = get_scheduler_status()
    if status["running"]:
        st.success("✅ Scheduler Running")
    else:
        st.warning("⚠️ Scheduler Stopped")
    
    if status["jobs"]:
        st.write(f"📋 {len(status['jobs'])} scheduled jobs")
        for job in status["jobs"]:
            st.caption(f"- {job['id']} (Next: {job['next_run']})")

# Main content
tab1, tab2, tab3 = st.tabs(["📋 Workflows", "⏰ Schedule", "📊 Run History"])

with tab1:
    st.subheader("📋 Agent Workflows")
    
    workflows = get_workflows()
    
    if workflows:
        for wf in workflows:
            with st.expander(f"**{wf['name']}** - {wf.get('enabled', True) and '✅ Active' or '❌ Paused'}"):
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.write(f"**Topic:** {wf['topic']}")
                    st.write(f"**Agents:** {', '.join(wf['agents'])}")
                    st.write(f"**Schedule:** {wf['schedule_type']} - {wf['schedule_config']}")
                    st.write(f"**Last Run:** {wf.get('last_run', 'Never')}")
                    st.write(f"**Next Run:** {wf.get('next_run', 'Not scheduled')}")
                
                with col2:
                    if st.button("▶️ Run Now", key=f"run_{wf['name']}"):
                        result = run_workflow(wf['name'])
                        if result.get("status") == "success":
                            st.success("✅ Workflow executed!")
                            st.rerun()
                        else:
                            st.error(f"Error: {result.get('error', 'Unknown error')}")
                    
                    if st.button("⏰ Schedule", key=f"schedule_{wf['name']}"):
                        result = schedule_workflow(wf['name'])
                        if result.get("status") == "success":
                            st.success(f"✅ Scheduled! Next run: {result['next_run']}")
                            st.rerun()
                        else:
                            st.error(f"Error: {result.get('error', 'Unknown error')}")
                    
                    if st.button("🗑️ Delete", key=f"delete_{wf['name']}"):
                        delete_workflow(wf['name'])
                        st.rerun()
    else:
        st.info("No workflows created yet. Create one in the Schedule tab!")
    
    # Quick run button for single agents
    st.subheader("🚀 Quick Agent Run")
    if st.session_state.topic:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🔍 Run Research", use_container_width=True):
                result = run_agent("Research", st.session_state.topic, "Provide a comprehensive update")
                st.write(result)
        
        with col2:
            if st.button("📝 Run Summarizer", use_container_width=True):
                result = run_agent("Summarizer", st.session_state.topic, "")
                st.write(result)
        
        with col3:
            if st.button("💡 Run Insight", use_container_width=True):
                result = run_agent("Insight", st.session_state.topic, "")
                st.write(result)
    else:
        st.warning("Please select a topic first")

with tab2:
    st.subheader("⏰ Create Workflow")
    
    # Workflow form
    with st.form("workflow_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            workflow_name = st.text_input("Workflow Name", placeholder="e.g., Morning Research")
            selected_topic = st.selectbox("Topic", options=get_topic_list() or [""])
            
            if not selected_topic:
                st.warning("Please create a topic first")
        
        with col2:
            workflow_agents = st.multiselect(
                "Select Agents",
                options=["Research", "Summarizer", "Devil", "Insight"],
                default=["Research", "Summarizer", "Insight"]
            )
        
        st.subheader("📅 Schedule Settings")
        
        schedule_type = st.radio(
            "Schedule Type",
            ["Daily (Cron)", "Interval (Minutes)"]
        )
        
        if schedule_type == "Daily (Cron)":
            col1, col2 = st.columns(2)
            with col1:
                hour = st.selectbox("Hour", list(range(0, 24)), index=8)
            with col2:
                minute = st.selectbox("Minute", list(range(0, 60)), index=0)
            
            schedule_config = {"hour": hour, "minute": minute}
        else:
            interval_hours = st.number_input("Hours between runs", min_value=1, max_value=72, value=24)
            schedule_config = {"hours": interval_hours}
        
        submitted = st.form_submit_button("💾 Create Workflow")
        
        if submitted:
            if not workflow_name:
                st.error("Please enter a workflow name")
            elif not selected_topic:
                st.error("Please select a topic")
            elif not workflow_agents:
                st.error("Please select at least one agent")
            else:
                # Save workflow
                save_workflow(
                    name=workflow_name,
                    schedule_type="cron" if schedule_type == "Daily (Cron)" else "interval",
                    schedule_config=schedule_config,
                    agents=workflow_agents,
                    topic=selected_topic
                )
                
                st.success(f"✅ Workflow '{workflow_name}' created!")
                
                # Schedule it immediately
                result = schedule_workflow(workflow_name)
                if result.get("status") == "success":
                    st.success(f"✅ Scheduled! Next run: {result['next_run']}")
                else:
                    st.warning("Workflow created but not scheduled. Please schedule it manually.")
                
                st.rerun()

with tab3:
    st.subheader("📊 Run History")
    
    workflows = get_workflows()
    
    if workflows:
        for wf in workflows:
            history = get_workflow_history(wf['name'])
            
            if history:
                with st.expander(f"**{wf['name']}** - {len(history)} runs"):
                    for run in reversed(history[-10:]):  # Show last 10
                        st.markdown(f"**🕐 {run['timestamp']}**")
                        
                        for agent, data in run['results'].items():
                            status_icon = "✅" if data['status'] == 'success' else "❌"
                            st.write(f"{status_icon} **{agent}**: {data['result'][:200]}...")
                        
                        st.markdown("---")
            else:
                st.info(f"No runs yet for '{wf['name']}'")
    else:
        st.info("No workflows created yet")

# Display topic log (if selected)
if st.session_state.topic:
    with st.expander("📜 Shared Topic Log"):
        log = get_topic_memory(st.session_state.topic)
        if log:
            for entry in reversed(log):
                st.markdown(f"**{entry['agent']}** - 🕐 {entry.get('timestamp', 'Unknown')}")
                st.write(entry['content'])
                st.markdown("---")

# Footer
st.markdown("---")
st.caption("⏰ AthenaCore | Scheduled Agent Workflow Engine | Automated Research")