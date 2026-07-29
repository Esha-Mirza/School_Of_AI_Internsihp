import streamlit as st
from agents.incident_agent import run_incident_response, get_incident_history
from orchestrator import get_topic_list, delete_topic_memory

st.set_page_config(
    page_title="Cybersecurity Incident Response Agent",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 Cybersecurity Incident Response Agent")
st.markdown("*AI-powered security incident triage and response*")

# Session state
if "topic" not in st.session_state:
    st.session_state.topic = None
if "incident_results" not in st.session_state:
    st.session_state.incident_results = None

# Sidebar
with st.sidebar:
    st.header("📂 Incidents")
    
    topics = get_topic_list()
    
    if topics:
        for t in topics:
            if st.button(f"📁 {t['name']} ({t['message_count']})", key=f"topic_{t['name']}"):
                st.session_state.topic = t['name']
                st.session_state.incident_results = None
                st.rerun()
    else:
        st.info("No incidents yet")
    
    st.markdown("---")
    st.header("🆕 New Incident")
    new_topic = st.text_input("Incident ID / Name:")
    if st.button("Create Incident"):
        if new_topic:
            st.session_state.topic = new_topic
            st.session_state.incident_results = None
            st.rerun()
    
    st.markdown("---")
    st.header("🤖 Response Agents")
    st.write("""
    - 📋 **Log Parser** - Analyzes logs and alerts
    - 🔍 **Threat Intel** - Provides threat context
    - 🛡️ **Containment** - Recommends response actions
    """)
    
    st.markdown("---")
    st.header("📊 Incident Stats")
    if st.session_state.topic:
        log = get_incident_history(st.session_state.topic)
        if log:
            st.metric("Total Actions", len(log))

# Main content
if st.session_state.topic:
    st.subheader(f"🆔 Incident: {st.session_state.topic}")
    
    tab1, tab2, tab3 = st.tabs(["📤 Upload Logs", "📊 Incident Response", "📜 Timeline"])
    
    with tab1:
        st.subheader("📤 Upload System Logs or Alerts")
        
        uploaded_file = st.file_uploader(
            "Choose a log file",
            type=["txt", "log", "json", "csv"],
            help="Upload system logs, security alerts, or incident reports"
        )
        
        log_text = st.text_area(
            "Or paste log data here:",
            placeholder="Paste your logs or alerts...",
            height=200
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            if uploaded_file:
                st.success(f"✅ File uploaded: {uploaded_file.name}")
                log_text = uploaded_file.getvalue().decode('utf-8')
        
        with col2:
            if st.button("🔍 Analyze Incident", type="primary", use_container_width=True):
                if log_text.strip():
                    with st.spinner("🧠 Running incident response agents..."):
                        # Progress tracking
                        progress_bar = st.progress(0)
                        status_text = st.empty()
                        
                        status_text.text("📋 Log Parser Agent analyzing logs...")
                        progress_bar.progress(25)
                        
                        results = run_incident_response(st.session_state.topic, log_text)
                        st.session_state.incident_results = results
                        
                        status_text.text("🔍 Threat Intelligence Agent analyzing...")
                        progress_bar.progress(50)
                        
                        status_text.text("🛡️ Containment Advisor planning response...")
                        progress_bar.progress(75)
                        
                        status_text.text("✅ Incident response complete!")
                        progress_bar.progress(100)
                        
                        st.success("✅ Incident analysis complete!")
                        st.rerun()
                else:
                    st.warning("Please provide log data")
    
    with tab2:
        st.subheader("📊 Incident Response Report")
        
        if st.session_state.incident_results:
            results = st.session_state.incident_results
            
            # Display results in cards
            with st.container():
                st.markdown("""
                <div style="border: 3px solid #FF5722; border-radius: 10px; padding: 20px; margin: 10px 0;">
                    <h3 style="color: #FF5722;">⚠️ IMMEDIATE RESPONSE REQUIRED</h3>
                    <p>Incident analysis complete. Review recommendations below.</p>
                </div>
                """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            
            severity = "🔴 Critical"
            if "low" in results.get("log_analysis", "").lower():
                severity = "🟢 Low"
            elif "medium" in results.get("log_analysis", "").lower():
                severity = "🟡 Medium"
            elif "high" in results.get("log_analysis", "").lower():
                severity = "🟠 High"
            
            with col1:
                st.metric("Incident Severity", severity)
            
            with col2:
                log_agent = "⚠️ Logs Analyzed"
                if results.get("log_analysis"):
                    log_agent = "✅ Logs Analyzed"
                st.metric("Log Parser", log_agent)
            
            with col3:
                threat_agent = "⚠️ Intel Pending"
                if results.get("threat_report"):
                    threat_agent = "✅ Intel Collected"
                st.metric("Threat Intel", threat_agent)
            
            # Detailed results
            st.subheader("📋 Log Parser Analysis")
            st.write(results.get("log_analysis", "No analysis available"))
            
            st.subheader("🔍 Threat Intelligence Report")
            st.write(results.get("threat_report", "No threat intelligence available"))
            
            st.subheader("🛡️ Containment & Response Plan")
            st.write(results.get("containment_plan", "No containment plan available"))
            
            # Export results
            st.subheader("📥 Export Incident Report")
            
            export_text = f"""=== INCIDENT RESPONSE REPORT ===
Incident: {st.session_state.topic}
Time: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📋 LOG PARSER ANALYSIS:
{results.get("log_analysis", "N/A")}

🔍 THREAT INTELLIGENCE:
{results.get("threat_report", "N/A")}

🛡️ CONTAINMENT PLAN:
{results.get("containment_plan", "N/A")}

================================
Generated by Cybersecurity Incident Response Agent
"""
            
            st.download_button(
                label="📥 Download Incident Report",
                data=export_text,
                file_name=f"incident_report_{st.session_state.topic}.txt",
                mime="text/plain"
            )
            
            if st.button("🔄 Clear Results"):
                st.session_state.incident_results = None
                st.rerun()
        else:
            st.info("Upload logs to generate an incident response report")
    
    with tab3:
        st.subheader("📜 Incident Timeline")
        
        log = get_incident_history(st.session_state.topic)
        
        if log:
            for entry in reversed(log):
                with st.expander(f"**{entry['agent']}** - 🕐 {entry.get('timestamp', 'Unknown')}"):
                    st.write(entry['content'])
        else:
            st.info("No incident timeline yet")

else:
    st.info("👈 Create a new incident or select an existing one")
    
    st.markdown("" "
    ### 🔐 Cybersecurity Incident Response Agent
    
    **AI-powered security incident triage and response!**
    
    **How it works:**
    1. Create an incident (e.g., "Compromised Server")
    2. Upload logs or paste alerts
    3. Agents analyze and recommend response
    
    **The Response Team:**
    - 📋 **Log Parser** - Analyzes logs and alerts
    - 🔍 **Threat Intel** - Provides threat context
    - 🛡️ **Containment** - Recommends response actions
    
    **Sample Log Data:** 