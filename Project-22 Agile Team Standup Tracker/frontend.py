import streamlit as st
from agents.standup_agent import process_standup, get_standup_history, get_sprint_stats
from orchestrator import get_topic_list, delete_topic_memory
from datetime import datetime

st.set_page_config(
    page_title="Agile Team Standup Tracker",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Agile Team Standup Tracker")
st.markdown("*AI-powered asynchronous standup system*")

# Session state
if "topic" not in st.session_state:
    st.session_state.topic = None
if "standup_results" not in st.session_state:
    st.session_state.standup_results = None

# Sidebar
with st.sidebar:
    st.header("📊 Sprints")
    
    topics = get_topic_list()
    
    if topics:
        for t in topics:
            if st.button(f"🚀 {t['name']} ({t['message_count']})", key=f"topic_{t['name']}"):
                st.session_state.topic = t['name']
                st.session_state.standup_results = None
                st.rerun()
    else:
        st.info("No sprints yet")
    
    st.markdown("---")
    st.header("🆕 New Sprint")
    new_topic = st.text_input("Sprint Name:")
    if st.button("Create Sprint"):
        if new_topic:
            st.session_state.topic = new_topic
            st.session_state.standup_results = None
            st.rerun()
    
    st.markdown("---")
    st.header("🤖 Standup Agents")
    st.write("""
    - 📝 **Summary Agent** - Summarizes team updates
    - 🚨 **Blocker Detector** - Identifies blockers
    - 📊 **Sprint Estimator** - Tracks progress
    """)
    
    st.markdown("---")
    st.header("📈 Sprint Stats")
    if st.session_state.topic:
        stats = get_sprint_stats(st.session_state.topic)
        if stats["total_entries"] > 0:
            st.metric("Total Updates", stats["total_entries"])
            st.metric("Active Days", stats["active_days"])

# Main content
if st.session_state.topic:
    st.subheader(f"🚀 Sprint: {st.session_state.topic}")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "📝 Daily Standup", 
        "📊 Summary",
        "🚨 Blockers",
        "📈 Sprint Progress"
    ])
    
    with tab1:
        st.subheader("📝 Daily Standup Update")
        
        team_member = st.text_input("👤 Your Name")
        update_date = st.date_input("📅 Date", datetime.now())
        
        yesterday = st.text_area("🔄 What did you do yesterday?", height=80)
        today = st.text_area("🎯 What will you do today?", height=80)
        blockers = st.text_area("🚧 Any blockers or impediments?", height=80)
        
        if st.button("📤 Submit Update", type="primary"):
            if team_member and (yesterday or today):
                update_text = f"""
Team Member: {team_member}
Date: {update_date}

**Yesterday:** {yesterday}
**Today:** {today}
**Blockers:** {blockers}
"""
                with st.spinner("🧠 Processing standup..."):
                    results = process_standup(st.session_state.topic, update_text)
                    st.session_state.standup_results = results
                    st.success("✅ Standup submitted!")
                    st.rerun()
            else:
                st.warning("Please enter your name and at least one update")
        
        st.markdown("---")
        st.subheader("📋 Recent Updates")
        history = get_standup_history(st.session_state.topic)
        
        if history:
            for entry in reversed(history[-5:]):
                with st.expander(f"**{entry.get('agent', 'Unknown')}** - 🕐 {entry.get('timestamp', 'Unknown')}"):
                    st.write(entry.get("content", ""))
        else:
            st.info("No updates yet")
    
    with tab2:
        st.subheader("📊 Daily Standup Summary")
        
        if st.session_state.standup_results:
            summary = st.session_state.standup_results.get("summary", "")
            st.write(summary)
        else:
            st.info("Submit a standup to see the summary")
        
        st.markdown("---")
        st.subheader("📥 Export Digests")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📥 Download Daily Digest"):
                history = get_standup_history(st.session_state.topic)
                if history:
                    export_text = f"=== DAILY STANDUP DIGEST ===\n"
                    export_text += f"Sprint: {st.session_state.topic}\n"
                    export_text += f"Date: {datetime.now().strftime('%Y-%m-%d')}\n\n"
                    
                    for entry in history[-10:]:
                        export_text += f"[{entry.get('timestamp', '')}]\n"
                        export_text += f"{entry.get('content', '')}\n\n"
                    
                    st.download_button(
                        label="📥 Download",
                        data=export_text,
                        file_name=f"standup_daily_{st.session_state.topic}.txt",
                        mime="text/plain"
                    )
        
        with col2:
            if st.button("📥 Download Weekly Digest"):
                history = get_standup_history(st.session_state.topic)
                if history:
                    export_text = f"=== WEEKLY STANDUP DIGEST ===\n"
                    export_text += f"Sprint: {st.session_state.topic}\n"
                    export_text += f"Week of: {datetime.now().strftime('%Y-%m-%d')}\n\n"
                    
                    for entry in history:
                        export_text += f"[{entry.get('timestamp', '')}]\n"
                        export_text += f"{entry.get('content', '')}\n\n"
                    
                    st.download_button(
                        label="📥 Download",
                        data=export_text,
                        file_name=f"standup_weekly_{st.session_state.topic}.txt",
                        mime="text/plain"
                    )
    
    with tab3:
        st.subheader("🚨 Blocker Report")
        
        if st.session_state.standup_results:
            blockers = st.session_state.standup_results.get("blockers", "")
            st.write(blockers)
        else:
            st.info("Submit a standup to see blocker detection")
        
        st.markdown("---")
        st.subheader("📋 Known Blockers")
        
        history = get_standup_history(st.session_state.topic)
        if history:
            blocker_entries = [e for e in history if "Blocker" in e.get("agent", "")]
            if blocker_entries:
                for entry in reversed(blocker_entries[-5:]):
                    st.write(f"- {entry.get('content', '')[:200]}...")
            else:
                st.info("No blockers reported")
    
    with tab4:
        st.subheader("📈 Sprint Progress")
        
        if st.session_state.standup_results:
            sprint = st.session_state.standup_results.get("sprint", "")
            st.write(sprint)
        else:
            st.info("Submit a standup to see sprint progress")
        
        st.markdown("---")
        st.subheader("📊 Sprint Statistics")
        
        stats = get_sprint_stats(st.session_state.topic)
        if stats["total_entries"] > 0:
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Total Updates", stats["total_entries"])
            
            with col2:
                st.metric("Active Days", stats["active_days"])
            
            with col3:
                st.metric("Teammates", len(stats["teammates"]))
            
            st.markdown("---")
            st.subheader("📈 Update History")
            
            history = get_standup_history(st.session_state.topic)
            if history:
                dates = {}
                for entry in history:
                    date = entry.get("timestamp", "").split()[0]
                    if date:
                        dates[date] = dates.get(date, 0) + 1
                
                # Convert to DataFrame for charting
                import pandas as pd
                df = pd.DataFrame(list(dates.items()), columns=["Date", "Updates"])
                if not df.empty:
                    st.bar_chart(df.set_index("Date"))
        else:
            st.info("No sprint data yet")

else:
    st.info("👈 Create a new sprint or select an existing one")
    
    st.markdown("""
    ### 🚀 Agile Team Standup Tracker
    
    **AI-powered asynchronous standup system!**
    
    **How it works:**
    1. Create a sprint
    2. Team members submit daily updates
    3. AI agents analyze and summarize
    4. Track blockers and progress
    
    **The Standup Agents:**
    - 📝 **Summary Agent** - Summarizes team updates
    - 🚨 **Blocker Detector** - Identifies blockers
    - 📊 **Sprint Estimator** - Tracks progress
    
    **What makes this special:**
    - 💬 Asynchronous standups
    - 🧠 AI-powered insights
    - 📊 Sprint tracking
    - 📥 Digest exports
    """)

# Footer
st.markdown("---")
st.caption("🚀 AthenaCore | Agile Team Standup Tracker | AI-Powered Standups")