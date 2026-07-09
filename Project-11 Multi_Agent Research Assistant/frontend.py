import streamlit as st
from orchestrator import run_research_pipeline
import time

st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Multi-Agent Research Assistant")
st.markdown("*Horizon Insights - AI-powered competitive intelligence*")

# Sidebar
with st.sidebar:
    st.header("🤖 Agents")
    st.write("""
    **Specialized AI Team:**
    
    1. 🔍 **Search Agent**
    - Collects raw information
    
    2. 📝 **Summarizer Agent**
    - Condenses findings
    
    3. ✅ **Fact-Checker Agent**
    - Reviews for accuracy
    
    4. 📄 **Report Generator Agent**
    - Produces final report
    """)
    
    st.header("💡 Tips")
    st.write("""
    - Be specific with research topics
    - Use company names, technologies, or trends
    - Allow 1-2 minutes for complete analysis
    """)
    
    st.header("📊 Example Topics")
    st.write("""
    - "AI trends in healthcare"
    - "EV market growth 2024"
    - "Blockchain in finance"
    - "Renewable energy startups"
    - "Quantum computing applications"
    """)

# Main content
st.subheader("🔬 Research Topic")

col1, col2 = st.columns([3, 1])

with col1:
    topic = st.text_input(
        "Enter a research topic:",
        placeholder="e.g., AI trends in healthcare",
        label_visibility="collapsed"
    )

with col2:
    run_button = st.button("🚀 Run Research", type="primary", use_container_width=True)

# Quick topic buttons
st.caption("Quick topics:")
col_a, col_b, col_c, col_d, col_e = st.columns(5)

if col_a.button("AI Healthcare"):
    topic = "AI trends in healthcare"
if col_b.button("EV Market"):
    topic = "EV market growth 2024"
if col_c.button("Blockchain"):
    topic = "Blockchain in finance"
if col_d.button("Renewable Energy"):
    topic = "Renewable energy startups"
if col_e.button("Quantum"):
    topic = "Quantum computing applications"

# Run research
if run_button and topic:
    with st.spinner("🧠 Multi-agent research in progress..."):
        try:
            # Create progress tracking
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            status_text.text("🔍 Agent 1: Searching for information...")
            progress_bar.progress(20)
            time.sleep(1)
            
            # Run the pipeline
            result = run_research_pipeline(topic)
            
            status_text.text("📝 Agent 2: Summarizing findings...")
            progress_bar.progress(40)
            time.sleep(1)
            
            status_text.text("✅ Agent 3: Fact-checking...")
            progress_bar.progress(60)
            time.sleep(1)
            
            status_text.text("📄 Agent 4: Generating final report...")
            progress_bar.progress(80)
            time.sleep(1)
            
            progress_bar.progress(100)
            status_text.text("✅ Research complete!")
            
            # Display results in tabs
            tab1, tab2, tab3, tab4 = st.tabs([
                "🔍 Search Results",
                "📝 Summary",
                "✅ Fact-Checker",
                "📄 Final Report"
            ])
            
            with tab1:
                st.subheader("Raw Search Findings")
                st.markdown("---")
                st.text(result.get("search", "No search results"))
                
                st.download_button(
                    label="📥 Download Search Results",
                    data=result.get("search", ""),
                    file_name="search_results.txt",
                    mime="text/plain"
                )
            
            with tab2:
                st.subheader("Condensed Summary")
                st.markdown("---")
                st.write(result.get("summary", "No summary generated"))
                
                st.download_button(
                    label="📥 Download Summary",
                    data=result.get("summary", ""),
                    file_name="summary.txt",
                    mime="text/plain"
                )
            
            with tab3:
                st.subheader("Fact-Checker Feedback")
                st.markdown("---")
                
                corrections = result.get("corrections", "No feedback")
                
                # Check if there are corrections
                if "bias" in corrections.lower() or "error" in corrections.lower():
                    st.warning("⚠️ Suggestions for improvement found")
                else:
                    st.success("✅ Summary appears balanced and accurate")
                
                st.write(corrections)
                
                st.download_button(
                    label="📥 Download Fact-Checker Feedback",
                    data=corrections,
                    file_name="fact_checker_feedback.txt",
                    mime="text/plain"
                )
            
            with tab4:
                st.subheader("Executive Research Report")
                st.markdown("---")
                
                # Display report in a nice format
                report = result.get("report", "No report generated")
                st.code(report, language="markdown")
                
                # Download buttons
                col1, col2 = st.columns(2)
                
                with col1:
                    st.download_button(
                        label="📥 Download Full Report (TXT)",
                        data=report,
                        file_name="research_report.txt",
                        mime="text/plain"
                    )
                
                with col2:
                    # Also offer as markdown
                    st.download_button(
                        label="📥 Download Report (MD)",
                        data=f"# Research Report: {topic}\n\n{report}",
                        file_name="research_report.md",
                        mime="text/markdown"
                    )
            
            # Export all results
            st.subheader("📦 Export All Results")
            all_results = f"""
=== MULTI-AGENT RESEARCH REPORT ===
Topic: {topic}
Date: {time.strftime('%Y-%m-%d %H:%M:%S')}

🔍 SEARCH RESULTS:
{result.get("search", "N/A")}

📝 SUMMARY:
{result.get("summary", "N/A")}

✅ FACT-CHECKER FEEDBACK:
{result.get("corrections", "N/A")}

📄 FINAL REPORT:
{result.get("report", "N/A")}

============================================
Generated by Horizon Insights Multi-Agent System
"""
            
            st.download_button(
                label="📥 Download Complete Research Package",
                data=all_results,
                file_name=f"research_package_{topic.replace(' ', '_')}.txt",
                mime="text/plain",
                use_container_width=True
            )
            
            st.balloons()
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.info("Make sure Ollama is running with the model installed")

elif run_button and not topic:
    st.warning("⚠️ Please enter a research topic")

# Footer
st.markdown("---")
st.caption("🧠 Horizon Insights | Multi-Agent Research Assistant | AI-Powered Competitive Intelligence")