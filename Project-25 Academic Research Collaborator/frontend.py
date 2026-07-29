import streamlit as st
from agents.research_agent import process_research, validate_hypothesis, polish_draft_with_feedback, get_research_history
from orchestrator import get_topic_list, delete_topic_memory

st.set_page_config(
    page_title="Academic Research Collaborator",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Academic Research Collaborator")
st.markdown("*AI-powered research assistant for scholars*")

# Session state
if "topic" not in st.session_state:
    st.session_state.topic = None
if "research_results" not in st.session_state:
    st.session_state.research_results = None

# Sidebar
with st.sidebar:
    st.header("📂 Research Projects")
    
    topics = get_topic_list()
    
    if topics:
        for t in topics:
            if st.button(f"📚 {t['name']} ({t['message_count']})", key=f"topic_{t['name']}"):
                st.session_state.topic = t['name']
                st.session_state.research_results = None
                st.rerun()
    else:
        st.info("No research projects yet")
    
    st.markdown("---")
    st.header("🆕 New Project")
    new_topic = st.text_input("Research Topic:")
    if st.button("Create Project"):
        if new_topic:
            st.session_state.topic = new_topic
            st.session_state.research_results = None
            st.rerun()
    
    st.markdown("---")
    st.header("🤖 Research Agents")
    st.write("""
    - 📄 **Literature Review** - Reviews literature
    - 🔬 **Hypothesis Validator** - Validates hypotheses
    - ✍️ **Draft Polisher** - Polishes drafts
    """)

# Main content
if st.session_state.topic:
    st.subheader(f"📚 Research: {st.session_state.topic}")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "📄 Literature Review", 
        "🔬 Hypothesis",
        "✍️ Draft",
        "📜 History"
    ])
    
    with tab1:
        st.subheader("📄 Literature Review")
        
        research_question = st.text_area(
            "📝 Research Question:",
            height=80,
            placeholder="What is your research question?"
        )
        
        citations = st.text_area(
            "📚 Citations/Literature:",
            height=150,
            placeholder="Paste your citations or literature notes..."
        )
        
        if st.button("📄 Conduct Literature Review", type="primary"):
            if research_question:
                with st.spinner("🧠 Conducting literature review..."):
                    results = process_research(
                        st.session_state.topic,
                        research_question,
                        citations
                    )
                    st.session_state.research_results = results
                    st.success("✅ Literature review complete!")
                    st.rerun()
            else:
                st.warning("Please enter a research question")
        
        if st.session_state.research_results:
            st.markdown("---")
            st.subheader("📄 Literature Review")
            st.write(st.session_state.research_results.get("review", ""))
            
            st.markdown("---")
            st.subheader("🔍 Research Gaps")
            st.write(st.session_state.research_results.get("gaps", ""))
    
    with tab2:
        st.subheader("🔬 Hypothesis Validator")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            if st.session_state.research_results:
                st.subheader("📋 Generated Hypotheses")
                st.write(st.session_state.research_results.get("hypotheses", ""))
            
            st.markdown("---")
            st.subheader("🧪 Validate Custom Hypothesis")
            
            custom_hypothesis = st.text_area("Hypothesis:", height=80)
            evidence = st.text_area("Evidence:", height=100)
            
            if st.button("🔬 Validate Hypothesis"):
                if custom_hypothesis and evidence:
                    with st.spinner("🧠 Validating hypothesis..."):
                        validation = validate_hypothesis(
                            st.session_state.topic,
                            custom_hypothesis,
                            evidence
                        )
                        st.subheader("📊 Validation Results")
                        st.write(validation)
                else:
                    st.warning("Please enter both hypothesis and evidence")
        
        with col2:
            st.subheader("📊 Hypothesis Validation Tips")
            st.info("""
            **What makes a good hypothesis?**
            - Testable and measurable
            - Clear cause-and-effect relationship
            - Grounded in literature
            - Specific and focused
            
            **What is strong evidence?**
            - Peer-reviewed sources
            - Empirical data
            - Replicable findings
            - Appropriate methodology
            """)
    
    with tab3:
        st.subheader("✍️ Draft Polisher")
        
        draft = st.text_area(
            "📝 Your Draft:",
            height=200,
            placeholder="Paste your paper draft here..."
        )
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            feedback = st.text_area(
                "💬 Specific Feedback:",
                height=80,
                placeholder="Any specific feedback or areas to focus on?"
            )
        
        with col2:
            if st.button("✨ Polish Draft", type="primary"):
                if draft:
                    with st.spinner("🧠 Polishing draft..."):
                        if feedback:
                            polished = polish_draft_with_feedback(
                                st.session_state.topic,
                                draft,
                                feedback
                            )
                        else:
                            from agents.draft_agent import run as polish
                            polished = polish(st.session_state.topic, draft)
                        
                        st.subheader("✨ Polished Draft")
                        st.write(polished)
                else:
                    st.warning("Please paste a draft")
        
        if st.button("💡 Get Writing Tips"):
            with st.spinner("🧠 Generating tips..."):
                from agents.draft_agent import get_writing_tips
                tips = get_writing_tips(st.session_state.topic)
                st.subheader("💡 Academic Writing Tips")
                st.write(tips)
    
    with tab4:
        st.subheader("📜 Research History")
        
        history = get_research_history(st.session_state.topic)
        
        if history:
            for entry in reversed(history):
                with st.expander(f"**{entry['agent']}** - 🕐 {entry.get('timestamp', 'Unknown')}"):
                    st.write(entry['content'])
        else:
            st.info("No research history yet")

else:
    st.info("👈 Create a new research project or select an existing one")
    
    st.markdown("""
    ### 📚 Academic Research Collaborator
    
    **AI-powered research assistant for scholars!**
    
    **How it works:**
    1. Create a research project
    2. Enter your research question
    3. Provide citations and literature
    4. AI agents analyze and generate insights
    
    **The Research Agents:**
    - 📄 **Literature Review** - Reviews and summarizes literature
    - 🔬 **Hypothesis Validator** - Validates hypotheses
    - ✍️ **Draft Polisher** - Polishes and improves drafts
    
    ### 📊 Features:
    - 📄 Literature review and gap analysis
    - 🔬 Hypothesis generation and validation
    - ✍️ Draft polishing with feedback
    - 📜 Persistent research history
    - 💡 Academic writing tips
    """)

# Footer
st.markdown("---")
st.caption("📚 AthenaCore | Academic Research Collaborator | AI-Powered Research Assistant")