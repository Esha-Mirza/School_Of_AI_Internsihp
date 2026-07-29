import streamlit as st
from orchestrator import run_agent, get_topic_memory, get_topic_list, delete_topic_memory
from agents.explainer_agent import run as explainer_run
from agents.quiz_agent import run as quiz_run, run_by_level
from agents.motivation_agent import run as motivation_run
from agents.progress_agent import run as progress_run
import time

st.set_page_config(
    page_title="Agent-Guided Learning Coach",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Agent-Guided Learning Coach")
st.markdown("*Your personal AI tutor with specialized learning agents*")

# Session state initialization
if "topic" not in st.session_state:
    st.session_state.topic = None
if "quiz_answer" not in st.session_state:
    st.session_state.quiz_answer = None

# Sidebar
with st.sidebar:
    st.header("📂 Subjects")
    
    topics = get_topic_list()
    
    if topics:
        for t in topics:
            if st.button(f"📁 {t['name']} ({t['message_count']})", key=f"topic_{t['name']}"):
                st.session_state.topic = t['name']
                st.rerun()
    else:
        st.info("No subjects yet. Create one!")
    
    st.markdown("---")
    st.header("➕ New Subject")
    new_topic = st.text_input("Enter subject name:")
    if st.button("Create Subject"):
        if new_topic:
            st.session_state.topic = new_topic
            st.rerun()
    
    st.markdown("---")
    st.header("🤖 Learning Agents")
    st.write("""
    - 🧠 **Explainer** - Simplifies concepts
    - 📝 **Quiz** - Generates questions
    - 💪 **Motivation** - Encouragement & advice
    - 📊 **Progress** - Tracks learning
    """)
    
    st.markdown("---")
    st.header("📊 Your Progress")
    if st.session_state.topic:
        log = get_topic_memory(st.session_state.topic)
        if log:
            st.metric("Total Interactions", len(log))
            
            # Quick stats
            explainer_count = sum(1 for entry in log if entry["agent"] == "Explainer Agent")
            quiz_count = sum(1 for entry in log if entry["agent"] == "Quiz Agent")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("📝 Explained", explainer_count)
            with col2:
                st.metric("📋 Quizzes", quiz_count)

# Main content
if st.session_state.topic:
    st.subheader(f"📚 Subject: {st.session_state.topic}")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🧠 Learn", 
        "📝 Quiz", 
        "💪 Motivation", 
        "📊 Progress",
        "📜 History"
    ])
    
    with tab1:
        st.subheader("🧠 Learn with Explainer Agent")
        st.write("Enter a concept to learn about, or ask any question!")
        
        concept_input = st.text_area(
            "📝 What would you like to learn?",
            placeholder="e.g., Explain photosynthesis, What is machine learning?, Tell me about Python functions...",
            height=100
        )
        
        if st.button("📖 Learn Now", type="primary"):
            if concept_input.strip():
                with st.spinner("🧠 Explaining concept..."):
                    result = explainer_run(st.session_state.topic, concept_input)
                    st.subheader("📖 Explanation")
                    st.write(result)
                    
                    # Quick quiz suggestion
                    st.info("💡 Test your understanding! Try the Quiz tab to generate questions on this concept.")
            else:
                st.warning("Please enter a concept to learn about")
    
    with tab2:
        st.subheader("📝 Quiz Agent")
        st.write("Generate quiz questions to test your understanding!")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            quiz_concept = st.text_input(
                "Enter the concept to be quizzed on:",
                placeholder="e.g., Photosynthesis, Python loops, Machine learning basics..."
            )
        
        with col2:
            difficulty = st.selectbox(
                "Difficulty",
                ["easy", "medium", "hard"]
            )
        
        if st.button("📝 Generate Quiz", type="primary"):
            if quiz_concept.strip():
                with st.spinner("📝 Generating quiz questions..."):
                    result = run_by_level(st.session_state.topic, quiz_concept, difficulty)
                    st.subheader(f"📋 Quiz ({difficulty} difficulty)")
                    st.write(result)
                    
                    # Show feedback option
                    st.info("💡 Check your answers using the Progress tab to track your learning!")
            else:
                st.warning("Please enter a concept for the quiz")
        
        # Quick quiz shortcuts
        st.subheader("⚡ Quick Quiz")
        col1, col2, col3 = st.columns(3)
        
        if st.session_state.topic:
            with col1:
                if st.button("🌱 Easy"):
                    with st.spinner("Generating easy quiz..."):
                        result = run_by_level(st.session_state.topic, st.session_state.topic, "easy")
                        st.write(result)
            
            with col2:
                if st.button("📚 Medium"):
                    with st.spinner("Generating medium quiz..."):
                        result = run_by_level(st.session_state.topic, st.session_state.topic, "medium")
                        st.write(result)
            
            with col3:
                if st.button("🔥 Hard"):
                    with st.spinner("Generating hard quiz..."):
                        result = run_by_level(st.session_state.topic, st.session_state.topic, "hard")
                        st.write(result)
    
    with tab3:
        st.subheader("💪 Motivation Agent")
        st.write("Need encouragement? Get a motivational boost!")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            progress_status = st.selectbox(
                "How's your learning going?",
                ["Just starting", "Making progress", "Stuck on something", "Almost done", "Need a break"]
            )
        
        with col2:
            st.write("")
            st.write("")
            if st.button("💪 Boost Me!", type="primary", use_container_width=True):
                with st.spinner("Generating motivation..."):
                    result = motivation_run(st.session_state.topic, progress_status)
                    st.subheader("💪 Motivation & Advice")
                    st.write(result)
        
        # Daily quote
        st.markdown("---")
        st.subheader("🌟 Daily Wisdom")
        st.info("""
        "The expert in anything was once a beginner."
        
        Keep going, one concept at a time! 🚀
        """)
    
    with tab4:
        st.subheader("📊 Progress Agent")
        st.write("Track your learning journey and get feedback!")
        
        if st.button("📊 Track Progress", type="primary"):
            with st.spinner("Analyzing your progress..."):
                result = progress_run(st.session_state.topic)
                st.subheader("📊 Learning Progress Report")
                st.write(result)
        
        st.markdown("---")
        st.subheader("📈 Learning Activity")
        
        log = get_topic_memory(st.session_state.topic)
        
        if log:
            # Show recent activities
            st.write("**Recent Learning Activities:**")
            for entry in reversed(log[-5:]):
                st.caption(f"🕐 {entry.get('timestamp', 'Unknown')}")
                st.write(f"**{entry['agent']}**")
                st.write(entry['content'][:200] + ("..." if len(entry['content']) > 200 else ""))
                st.markdown("---")
        else:
            st.info("No learning activity yet. Start learning!")
    
    with tab5:
        st.subheader("📜 Learning History")
        
        log = get_topic_memory(st.session_state.topic)
        
        if log:
            for entry in reversed(log):
                with st.expander(f"**{entry['agent']}** - 🕐 {entry.get('timestamp', 'Unknown')}"):
                    st.write(entry['content'])
        else:
            st.info("No history yet. Start learning!")

else:
    st.info("👈 Select a subject or create a new one to get started!")
    
    st.markdown("""
    ### 📚 Welcome to Agent-Guided Learning Coach!
    
    **Your personal AI tutor with specialized learning agents!**
    
    **How it works:**
    1. Create a subject to learn
    2. Use the Explainer Agent to learn concepts
    3. Test yourself with the Quiz Agent
    4. Get motivation from the Motivation Agent
    5. Track your progress with the Progress Agent
    
    **The Learning Agents:**
    - 🧠 **Explainer** - Simplifies complex concepts
    - 📝 **Quiz** - Generates questions to test understanding
    - 💪 **Motivation** - Provides encouragement and advice
    - 📊 **Progress** - Tracks learning and gives feedback
    
    **Example Subjects:**
    - Python Programming
    - Machine Learning
    - World History
    - Biology
    - Mathematics
    """)

# Footer
st.markdown("---")
st.caption("📚 AthenaCore | Agent-Guided Learning Coach | Your Personal AI Tutor")