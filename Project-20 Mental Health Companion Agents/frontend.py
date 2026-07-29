import streamlit as st
import pandas as pd
from datetime import datetime
from agents.wellness_agent import process_journal_entry, get_wellness_report
from agents.wellness_tracker_agent import get_mood_data
from orchestrator import get_topic_list, delete_topic_memory

st.set_page_config(
    page_title="Mental Health Companion",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Mental Health Companion Agents")
st.markdown("*Your compassionate AI journaling and wellness coach*")

# Disclaimer
st.warning("""
⚠️ **Educational Prototype**: This is NOT a medical device. 
Please consult qualified mental health professionals for clinical support.
""")

# Session state
if "topic" not in st.session_state:
    st.session_state.topic = None
if "journal_results" not in st.session_state:
    st.session_state.journal_results = None

# Sidebar
with st.sidebar:
    st.header("📓 Journals")
    
    topics = get_topic_list()
    
    if topics:
        for t in topics:
            if st.button(f"📔 {t['name']} ({t['message_count']})", key=f"topic_{t['name']}"):
                st.session_state.topic = t['name']
                st.session_state.journal_results = None
                st.rerun()
    else:
        st.info("No journals yet")
    
    st.markdown("---")
    st.header("📝 New Journal")
    new_topic = st.text_input("Journal Name:")
    if st.button("Create Journal"):
        if new_topic:
            st.session_state.topic = new_topic
            st.session_state.journal_results = None
            st.rerun()
    
    st.markdown("---")
    st.header("🤖 Wellness Agents")
    st.write("""
    - 🪞 **Reflection** - Summarizes emotions
    - 🔄 **Cognitive Reframe** - Offers perspective
    - 📊 **Wellness Tracker** - Tracks over time
    """)
    
    st.markdown("---")
    st.header("📊 Journal Stats")
    if st.session_state.topic:
        mood_data = get_mood_data(st.session_state.topic)
        if mood_data["count"] > 0:
            st.metric("Total Entries", mood_data["count"])
            if st.button("📈 View Trends"):
                st.rerun()

# Main content
if st.session_state.topic:
    st.subheader(f"📔 Journal: {st.session_state.topic}")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "📝 Journal Entry", 
        "🪞 Reflection", 
        "🔄 Cognitive Reframe",
        "📊 Wellness Tracking"
    ])
    
    with tab1:
        st.subheader("📝 Today's Journal Entry")
        st.write("How are you feeling today?")
        
        mood_options = ["😊 Excellent", "😌 Good", "😐 Okay", "😔 Low", "😢 Struggling"]
        mood = st.selectbox("Select your mood:", mood_options)
        
        journal = st.text_area(
            "Write your thoughts:",
            placeholder="What's on your mind today?",
            height=200
        )
        
        if st.button("💫 Process Journal Entry", type="primary"):
            if journal.strip():
                with st.spinner("🧠 Processing your entry..."):
                    results = process_journal_entry(st.session_state.topic, mood, journal)
                    st.session_state.journal_results = results
                    
                    st.success("✅ Journal processed!")
                    st.rerun()
            else:
                st.warning("Please write something in your journal")
        
        if st.session_state.journal_results:
            st.subheader("✅ Journal Processed")
            st.success("Your entry has been analyzed. Check the Reflection tab!")
    
    with tab2:
        st.subheader("🪞 Reflection Agent")
        st.write("*Summarizing your emotions and themes*")
        
        if st.session_state.journal_results:
            reflection = st.session_state.journal_results.get("reflection", "")
            st.markdown("---")
            st.write(reflection)
        else:
            st.info("Write a journal entry first to get a reflection")
    
    with tab3:
        st.subheader("🔄 Cognitive Reframe Agent")
        st.write("*Gaining new perspectives*")
        
        if st.session_state.journal_results:
            reframe = st.session_state.journal_results.get("reframe", "")
            st.markdown("---")
            st.write(reframe)
        else:
            st.info("Write a journal entry first to get cognitive reframing")
    
    with tab4:
        st.subheader("📊 Wellness Tracking Agent")
        st.write("*Tracking your well-being over time*")
        
        mood_data = get_mood_data(st.session_state.topic)
        
        if mood_data["count"] > 0:
            # Show mood distribution
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("📈 Mood Trends")
                
                # Create DataFrame for visualization
                df = pd.DataFrame(mood_data["trend"])
                if not df.empty and "date" in df.columns:
                    # Limit to last 30 entries
                    df = df.tail(30)
                    
                    # Plot
                    st.line_chart(df.set_index("date")["value"])
                    
                    st.caption("📌 5 = Excellent, 1 = Struggling")
            
            with col2:
                st.subheader("📊 Mood Distribution")
                
                mood_counts = mood_data.get("mood_counts", {})
                if mood_counts:
                    # Create bar chart
                    df_moods = pd.DataFrame({
                        "Mood": list(mood_counts.keys()),
                        "Count": list(mood_counts.values())
                    })
                    st.bar_chart(df_moods.set_index("Mood"))
            
            # Detailed report
            st.subheader("📋 Wellness Report")
            
            if st.button("📊 Generate Wellness Report"):
                with st.spinner("Generating wellness insights..."):
                    report = get_wellness_report(st.session_state.topic)
                    st.write(report)
            
            # Export data
            st.subheader("📥 Export Journal Data")
            
            if st.button("📥 Download Mood Data"):
                df_export = pd.DataFrame(mood_data["trend"])
                if not df_export.empty:
                    csv = df_export.to_csv(index=False)
                    st.download_button(
                        label="📥 Download CSV",
                        data=csv,
                        file_name=f"mood_data_{st.session_state.topic}.csv",
                        mime="text/csv"
                    )
        else:
            st.info("No wellness data yet. Start journaling to track your well-being!")

else:
    st.info("👈 Create a new journal or select an existing one")
    
    st.markdown("""
    ### 🧠 Mental Health Companion Agents
    
    **Your compassionate AI journaling and wellness coach!**
    
    **How it works:**
    1. Create a journal
    2. Write daily entries with mood
    3. AI agents reflect and support
    4. Track well-being over time
    
    **The Wellness Agents:**
    - 🪞 **Reflection** - Summarizes emotions and themes
    - 🔄 **Cognitive Reframe** - Offers perspective
    - 📊 **Wellness Tracker** - Tracks trends over time
    
    ### 💡 Tips for Journaling:
    - ✍️ Write freely and honestly
    - 📝 Focus on your thoughts and feelings
    - 🕐 Try to write daily for best results
    - 💫 Use the reframe for new perspectives
    """)

# Footer
st.markdown("---")
st.caption("🧠 AthenaCore | Mental Health Companion | Your Compassionate Wellness Coach")