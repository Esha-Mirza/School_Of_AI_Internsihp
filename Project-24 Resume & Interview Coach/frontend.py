import streamlit as st
from agents.career_agent import process_resume, conduct_interview, analyze_fit, get_career_history
from orchestrator import get_topic_list, delete_topic_memory

st.set_page_config(
    page_title="Resume & Interview Coach",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Resume & Interview Coach")
st.markdown("*AI-powered career preparation*")

# Session state
if "topic" not in st.session_state:
    st.session_state.topic = None
if "career_results" not in st.session_state:
    st.session_state.career_results = None
if "interview_mode" not in st.session_state:
    st.session_state.interview_mode = "questions"

# Sidebar
with st.sidebar:
    st.header("📂 Careers")
    
    topics = get_topic_list()
    
    if topics:
        for t in topics:
            if st.button(f"📄 {t['name']} ({t['message_count']})", key=f"topic_{t['name']}"):
                st.session_state.topic = t['name']
                st.session_state.career_results = None
                st.rerun()
    else:
        st.info("No career files yet")
    
    st.markdown("---")
    st.header("🆕 New Career")
    new_topic = st.text_input("Job Title / Goal:")
    if st.button("Create Profile"):
        if new_topic:
            st.session_state.topic = new_topic
            st.session_state.career_results = None
            st.rerun()
    
    st.markdown("---")
    st.header("🤖 Career Agents")
    st.write("""
    - 📝 **Resume Optimizer** - Improves your resume
    - 🎯 **Interview Agent** - Conducts mock interviews
    - 📊 **Role-Fit Analyzer** - Analyzes fit
    """)

# Main content
if st.session_state.topic:
    st.subheader(f"📄 Career: {st.session_state.topic}")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "📝 Resume", 
        "🎯 Interview",
        "📊 Role-Fit",
        "📜 History"
    ])
    
    with tab1:
        st.subheader("📝 Resume Optimizer")
        
        role = st.text_input("🎯 Target Role", value=st.session_state.topic)
        
        resume_text = st.text_area(
            "📄 Paste your resume here:",
            height=200,
            placeholder="Paste your resume text..."
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🔍 Analyze Resume", type="primary"):
                if resume_text:
                    with st.spinner("🧠 Analyzing resume..."):
                        results = process_resume(st.session_state.topic, resume_text, role)
                        st.session_state.career_results = results
                        st.success("✅ Resume analyzed!")
                        st.rerun()
                else:
                    st.warning("Please paste your resume")
        
        with col2:
            bullet_points = st.text_area("✏️ Bullet points to optimize:", height=80)
            if st.button("⚡ Optimize Bullet Points"):
                if bullet_points:
                    from agents.resume_agent import optimize_bullet_points
                    optimized = optimize_bullet_points(st.session_state.topic, bullet_points, role)
                    st.subheader("✨ Optimized Bullet Points")
                    st.write(optimized)
                else:
                    st.warning("Please enter bullet points")
        
        if st.session_state.career_results:
            st.markdown("---")
            st.subheader("📊 Resume Analysis")
            st.write(st.session_state.career_results.get("resume", ""))
    
    with tab2:
        st.subheader("🎯 Mock Interview Coach")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            interview_mode = st.radio(
                "Mode:",
                ["Generate Questions", "Practice Answering"],
                key="interview_mode_radio"
            )
        
        with col2:
            if interview_mode == "Generate Questions":
                if st.button("📝 Generate Questions"):
                    with st.spinner("🧠 Generating questions..."):
                        results = conduct_interview(st.session_state.topic, st.session_state.topic)
                        st.session_state.career_results = results
                        st.rerun()
            else:
                st.write("")
        
        if interview_mode == "Generate Questions" and st.session_state.career_results:
            st.subheader("📋 Interview Questions")
            questions = st.session_state.career_results.get("questions", "")
            st.write(questions)
        
        if interview_mode == "Practice Answering":
            st.subheader("💬 Practice Answer")
            
            question = st.text_area("📝 Interview Question:", height=80)
            answer = st.text_area("✍️ Your Answer (STAR Method):", height=150)
            
            if st.button("📊 Get Feedback"):
                if question and answer:
                    with st.spinner("🧠 Analyzing your answer..."):
                        from agents.interview_agent import generate_feedback
                        feedback = generate_feedback(st.session_state.topic, st.session_state.topic, question, answer)
                        st.subheader("📊 Feedback")
                        st.write(feedback)
                else:
                    st.warning("Please enter both question and answer")
    
    with tab3:
        st.subheader("📊 Role-Fit Analyzer")
        
        job_description = st.text_area(
            "📄 Paste job description here:",
            height=150,
            placeholder="Paste the job description..."
        )
        
        if st.button("🔍 Analyze Fit"):
            if resume_text and job_description:
                with st.spinner("🧠 Analyzing role fit..."):
                    results = analyze_fit(st.session_state.topic, resume_text, job_description)
                    st.session_state.career_results = results
                    st.success("✅ Fit analysis complete!")
                    st.rerun()
            else:
                st.warning("Please paste resume and job description")
        
        if st.session_state.career_results and "fit" in st.session_state.career_results:
            st.markdown("---")
            st.subheader("📊 Role-Fit Analysis")
            st.write(st.session_state.career_results.get("fit", ""))
    
    with tab4:
        st.subheader("📜 Career History")
        
        history = get_career_history(st.session_state.topic)
        
        if history:
            for entry in reversed(history):
                with st.expander(f"**{entry['agent']}** - 🕐 {entry.get('timestamp', 'Unknown')}"):
                    st.write(entry['content'])
        else:
            st.info("No career history yet")

else:
    st.info("👈 Create a new career profile or select an existing one")
    
    st.markdown("""
    ### 📄 Resume & Interview Coach
    
    **AI-powered career preparation!**
    
    **How it works:**
    1. Create a career profile
    2. Upload resume or paste text
    3. AI agents analyze and improve
    4. Practice mock interviews
    
    **The Career Agents:**
    - 📝 **Resume Optimizer** - Improves your resume
    - 🎯 **Interview Agent** - Conducts mock interviews
    - 📊 **Role-Fit Analyzer** - Analyzes fit
    
    ### 💡 Features:
    - 📊 Resume analysis and scoring
    - 🎯 Behavioral interview questions
    - ⭐ STAR method feedback
    - 📈 Role-fit analysis
    - 📜 Persistent history
    """)

# Footer
st.markdown("---")
st.caption("📄 AthenaCore | Resume & Interview Coach | AI-Powered Career Preparation")