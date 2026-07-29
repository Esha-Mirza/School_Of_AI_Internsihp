import streamlit as st
from orchestrator import run_agent, get_topic_memory, get_topic_list, delete_topic_memory
from agents.document_agent import process_uploaded_file, analyze_document
import time

st.set_page_config(
    page_title="Document Intelligence Workspace",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Document Intelligence Workspace")
st.markdown("*Upload documents for collaborative AI analysis*")

# Session state initialization
if "topic" not in st.session_state:
    st.session_state.topic = None
if "doc_analysis" not in st.session_state:
    st.session_state.doc_analysis = None

# Sidebar
with st.sidebar:
    st.header("📂 Topics")
    
    topics = get_topic_list()
    
    if topics:
        for t in topics:
            if st.button(f"📁 {t['name']} ({t['message_count']})", key=f"topic_{t['name']}"):
                st.session_state.topic = t['name']
                st.session_state.doc_analysis = None
                st.rerun()
    else:
        st.info("No topics yet. Create one!")
    
    st.markdown("---")
    st.header("➕ New Topic")
    new_topic = st.text_input("Enter new topic name:")
    if st.button("Create Topic"):
        if new_topic:
            st.session_state.topic = new_topic
            st.session_state.doc_analysis = None
            st.rerun()
    
    st.markdown("---")
    st.header("📁 Supported Files")
    st.write("""
    - 📄 **PDF** (.pdf)
    - 📝 **Word** (.docx)
    - 📃 **Text** (.txt)
    """)
    
    st.header("🤖 Analysis Agents")
    st.write("""
    - 📝 **Summary Agent** - Concise document summary
    - 🚨 **Red Flag Detector** - Identify risks and concerns
    - 📋 **Decision Extractor** - Extract decisions and action items
    """)

# Main content
if st.session_state.topic:
    st.subheader(f"📚 Topic: {st.session_state.topic}")
    
    tab1, tab2, tab3 = st.tabs(["📤 Upload Document", "📊 Analysis Results", "📜 Memory Log"])
    
    with tab1:
        st.subheader("📤 Upload Document")
        
        uploaded_file = st.file_uploader(
            "Choose a document to analyze",
            type=["pdf", "docx", "txt"],
            help="Upload PDF, DOCX, or TXT files for AI analysis"
        )
        
        if uploaded_file:
            st.success(f"✅ File uploaded: {uploaded_file.name} ({uploaded_file.size} bytes)")
            
            # Process file on button click
            if st.button("🔍 Analyze Document", type="primary"):
                with st.spinner("📄 Extracting text from document..."):
                    try:
                        # Extract text
                        text = process_uploaded_file(uploaded_file)
                        
                        if "Error" not in text:
                            # Show extracted text preview
                            with st.expander("📄 View Extracted Text"):
                                st.text_area(
                                    "Extracted Text",
                                    value=text[:2000] + ("..." if len(text) > 2000 else ""),
                                    height=200
                                )
                            
                            st.info(f"📊 Extracted {len(text)} characters")
                            
                            # Run document analysis
                            st.subheader("🧠 Running Document Analysis...")
                            progress_bar = st.progress(0)
                            status_text = st.empty()
                            
                            status_text.text("📝 Running Summary Agent...")
                            progress_bar.progress(25)
                            
                            # Analyze document
                            results = analyze_document(st.session_state.topic, text, run_all=True)
                            st.session_state.doc_analysis = results
                            
                            status_text.text("✅ Analysis complete!")
                            progress_bar.progress(100)
                            
                            st.success("✅ Document analysis complete!")
                            st.rerun()
                        else:
                            st.error(text)
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
    
    with tab2:
        st.subheader("📊 Document Analysis Results")
        
        if st.session_state.doc_analysis:
            results = st.session_state.doc_analysis
            
            # Display results in cards
            col1, col2, col3 = st.columns(3)
            
            with col1:
                with st.container():
                    st.markdown("""
                    <div style="border: 2px solid #4CAF50; border-radius: 10px; padding: 15px; margin: 10px 0;">
                        <h3 style="color: #4CAF50;">📝 Summary</h3>
                        <hr>
                        <p>{}</p>
                    </div>
                    """.format(results.get("summary", "No summary generated")), unsafe_allow_html=True)
            
            with col2:
                with st.container():
                    st.markdown("""
                    <div style="border: 2px solid #FF5722; border-radius: 10px; padding: 15px; margin: 10px 0;">
                        <h3 style="color: #FF5722;">🚨 Red Flags</h3>
                        <hr>
                        <p>{}</p>
                    </div>
                    """.format(results.get("red_flags", "No red flags detected")), unsafe_allow_html=True)
            
            with col3:
                with st.container():
                    st.markdown("""
                    <div style="border: 2px solid #2196F3; border-radius: 10px; padding: 15px; margin: 10px 0;">
                        <h3 style="color: #2196F3;">📋 Decisions</h3>
                        <hr>
                        <p>{}</p>
                    </div>
                    """.format(results.get("decisions", "No decisions extracted")), unsafe_allow_html=True)
            
            # Export results
            st.subheader("📥 Export Results")
            
            export_text = f"""=== DOCUMENT INTELLIGENCE ANALYSIS ===
Topic: {st.session_state.topic}

📝 SUMMARY:
{results.get("summary", "N/A")}

🚨 RED FLAGS:
{results.get("red_flags", "N/A")}

📋 DECISIONS:
{results.get("decisions", "N/A")}

================================
Generated by AthenaCore Document Intelligence
"""
            
            st.download_button(
                label="📥 Download Analysis Results",
                data=export_text,
                file_name=f"document_analysis_{st.session_state.topic}.txt",
                mime="text/plain"
            )
            
            # Clear results button
            if st.button("🔄 Clear Analysis"):
                st.session_state.doc_analysis = None
                st.rerun()
        else:
            st.info("No document analyzed yet. Upload a document in the Upload tab!")
    
    with tab3:
        st.subheader("📜 Memory Log")
        
        log = get_topic_memory(st.session_state.topic)
        
        if log:
            for entry in reversed(log):
                with st.expander(f"**{entry['agent']}** - 🕐 {entry.get('timestamp', 'Unknown')}"):
                    st.write(entry['content'])
        else:
            st.info("No memory entries yet")

else:
    st.info("👈 Select a topic or create a new one to get started!")
    
    st.markdown("""
    ### 📄 Document Intelligence Workspace
    
    **Upload documents for collaborative AI analysis!**
    
    **How it works:**
    1. Create a topic for your document
    2. Upload a PDF, DOCX, or TXT file
    3. AI agents analyze the document
    4. Get insights from all agents!
    
    **The Agents:**
    - 📝 **Summary Agent** - Concise document summary
    - 🚨 **Red Flag Detector** - Identify risks and concerns
    - 📋 **Decision Extractor** - Extract decisions and action items
    """)

# Footer
st.markdown("---")
st.caption("📄 AthenaCore | Document Intelligence Workspace | Collaborative Document Analysis")