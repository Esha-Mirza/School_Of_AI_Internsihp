import streamlit as st
from agents.proposal_agent import create_proposal, get_proposal_history, refine_proposal
from orchestrator import get_topic_list, delete_topic_memory
from datetime import datetime

st.set_page_config(
    page_title="Grant Proposal Assistant",
    page_icon="📝",
    layout="wide"
)

st.title("📝 AI-Powered Grant Proposal Assistant")
st.markdown("*Helping researchers and nonprofits draft winning proposals*")

# Session state
if "topic" not in st.session_state:
    st.session_state.topic = None
if "proposal_results" not in st.session_state:
    st.session_state.proposal_results = None
if "selected_agency" not in st.session_state:
    st.session_state.selected_agency = ""

# Sidebar
with st.sidebar:
    st.header("📂 Proposals")
    
    topics = get_topic_list()
    
    if topics:
        for t in topics:
            if st.button(f"📝 {t['name']} ({t['message_count']})", key=f"topic_{t['name']}"):
                st.session_state.topic = t['name']
                st.session_state.proposal_results = None
                st.rerun()
    else:
        st.info("No proposals yet")
    
    st.markdown("---")
    st.header("🆕 New Proposal")
    new_topic = st.text_input("Proposal Title:")
    if st.button("Create Proposal"):
        if new_topic:
            st.session_state.topic = new_topic
            st.session_state.proposal_results = None
            st.rerun()
    
    st.markdown("---")
    st.header("🤖 Proposal Agents")
    st.write("""
    - 📋 **Outline Designer** - Creates proposal structure
    - 💰 **Budget Estimator** - Creates budget estimates
    - 🎯 **Reviewer Simulator** - Generates feedback
    """)

# Main content
if st.session_state.topic:
    st.subheader(f"📝 Proposal: {st.session_state.topic}")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "📝 Create Proposal", 
        "📋 Outline",
        "💰 Budget",
        "🎯 Review"
    ])
    
    with tab1:
        st.subheader("📝 Proposal Details")
        
        col1, col2 = st.columns(2)
        
        with col1:
            agency = st.selectbox(
                "🏛️ Funding Agency",
                ["NSF", "NIH", "EU Horizon", "Wellcome Trust", "Gates Foundation", "Other"]
            )
            
            if agency == "Other":
                agency = st.text_input("Enter agency name")
            
            st.session_state.selected_agency = agency
            
            duration = st.number_input("📅 Project Duration (months)", min_value=1, max_value=60, value=12)
        
        with col2:
            team_size = st.number_input("👥 Team Size", min_value=1, max_value=20, value=3)
            goals = st.text_area("🎯 Project Goals", height=100, placeholder="What do you aim to achieve?")
        
        if st.button("📝 Generate Proposal", type="primary"):
            if goals:
                with st.spinner("🧠 Drafting your proposal..."):
                    results = create_proposal(
                        st.session_state.topic, 
                        goals, 
                        st.session_state.selected_agency,
                        duration, 
                        team_size
                    )
                    st.session_state.proposal_results = results
                    st.success("✅ Proposal drafted!")
                    st.rerun()
            else:
                st.warning("Please enter project goals")
    
    with tab2:
        st.subheader("📋 Proposal Outline")
        
        if st.session_state.proposal_results:
            outline = st.session_state.proposal_results.get("outline", "")
            st.write(outline)
            
            st.markdown("---")
            st.subheader("🔄 Refine Outline")
            
            feedback = st.text_area("Feedback for refinement:", height=100)
            
            if st.button("🔄 Refine Outline"):
                if feedback:
                    with st.spinner("Refining outline..."):
                        refined = refine_proposal(st.session_state.topic, outline, feedback)
                        st.subheader("📋 Refined Outline")
                        st.write(refined)
                        st.session_state.proposal_results["outline"] = refined
                else:
                    st.warning("Please enter feedback")
        else:
            st.info("Generate a proposal first")
    
    with tab3:
        st.subheader("💰 Budget Estimate")
        
        if st.session_state.proposal_results:
            budget = st.session_state.proposal_results.get("budget", "")
            st.write(budget)
        else:
            st.info("Generate a proposal first")
    
    with tab4:
        st.subheader("🎯 Reviewer Feedback")
        
        if st.session_state.proposal_results:
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("📋 Feedback")
                review = st.session_state.proposal_results.get("review", "")
                st.write(review)
            
            with col2:
                st.subheader("📊 Scores")
                scores = st.session_state.proposal_results.get("scores", "")
                st.write(scores)
            
            st.markdown("---")
            st.subheader("📊 Proposal Summary")
            
            # Calculate total score if available
            if "Score:" in str(scores):
                try:
                    score_line = [line for line in str(scores).split("\n") if "Score:" in line]
                    if score_line:
                        total_score = score_line[0].split(":")[1].strip()
                        st.metric("Estimated Score", total_score)
                except:
                    pass
            
            st.markdown("---")
            st.subheader("📥 Export Proposal")
            
            export_text = f"""=== GRANT PROPOSAL ===
Title: {st.session_state.topic}
Funding Agency: {st.session_state.selected_agency}

📋 OUTLINE:
{st.session_state.proposal_results.get("outline", "N/A")}

💰 BUDGET:
{st.session_state.proposal_results.get("budget", "N/A")}

🎯 REVIEWER FEEDBACK:
{st.session_state.proposal_results.get("review", "N/A")}

📊 SCORES:
{st.session_state.proposal_results.get("scores", "N/A")}

================================
Generated by Grant Proposal Assistant
"""
            
            st.download_button(
                label="📥 Download Proposal Package",
                data=export_text,
                file_name=f"proposal_{st.session_state.topic}.txt",
                mime="text/plain"
            )
        else:
            st.info("Generate a proposal first")

else:
    st.info("👈 Create a new proposal or select an existing one")
    
    st.markdown("""
    ### 📝 Grant Proposal Assistant
    
    **AI-powered grant proposal drafting!**
    
    **How it works:**
    1. Create a proposal
    2. Enter goals and funding agency
    3. AI agents design outline and budget
    4. Reviewer simulates feedback
    
    **The Proposal Agents:**
    - 📋 **Outline Designer** - Creates proposal structure
    - 💰 **Budget Estimator** - Creates budget estimates
    - 🎯 **Reviewer Simulator** - Generates feedback
    
    ### 🏛️ Funding Agencies:
    - NSF
    - NIH
    - EU Horizon
    - Wellcome Trust
    - Gates Foundation
    """)

# Footer
st.markdown("---")
st.caption("📝 AthenaCore | Grant Proposal Assistant | AI-Powered Proposal Writing")