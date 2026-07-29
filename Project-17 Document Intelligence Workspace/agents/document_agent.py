
import streamlit as st
import PyPDF2
import docx
import tempfile
import os
from datetime import datetime
from agents.base import call_llm, log_agent_response, get_topic_log

def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extract text from PDF file"""
    try:
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
            tmp.write(file_bytes)
            tmp_path = tmp.name
        
        text = ""
        with open(tmp_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        
        os.unlink(tmp_path)
        return text.strip()
    except Exception as e:
        return f"Error extracting PDF: {str(e)}"

def extract_text_from_docx(file_bytes: bytes) -> str:
    """Extract text from DOCX file"""
    try:
        with tempfile.NamedTemporaryFile(suffix=".docx", delete=False) as tmp:
            tmp.write(file_bytes)
            tmp_path = tmp.name
        
        doc = docx.Document(tmp_path)
        text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        
        os.unlink(tmp_path)
        return text.strip()
    except Exception as e:
        return f"Error extracting DOCX: {str(e)}"

def extract_text_from_txt(file_bytes: bytes) -> str:
    """Extract text from TXT file"""
    try:
        return file_bytes.decode('utf-8').strip()
    except Exception as e:
        return f"Error extracting TXT: {str(e)}"

def process_uploaded_file(file) -> str:
    """
    Process uploaded file and extract text
    
    Args:
        file: Streamlit uploaded file object
    
    Returns:
        Extracted text
    """
    file_bytes = file.getvalue()
    file_type = file.type
    
    if file_type == "application/pdf":
        return extract_text_from_pdf(file_bytes)
    elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return extract_text_from_docx(file_bytes)
    elif file_type == "text/plain":
        return extract_text_from_txt(file_bytes)
    else:
        return f"Unsupported file type: {file_type}"

def summarize_document(text: str) -> str:
    """Summarize document content"""
    prompt = f"""
You are a Document Summary Agent. Provide a concise summary of the following document.

Document:
{text[:3000]}

Summary (3-5 sentences covering key points):
"""
    return call_llm(prompt)

def detect_red_flags(text: str) -> str:
    """Detect red flags, risks, or concerning items"""
    prompt = f"""
You are a Red Flag Detector. Review the following document and identify potential risks, concerning items, or red flags.

Document:
{text[:3000]}

Red Flags (list any risks, concerns, or issues found):
"""
    return call_llm(prompt)

def extract_decisions(text: str) -> str:
    """Extract decisions, action items, or commitments"""
    prompt = f"""
You are a Decision Extractor. Review the following document and extract all decisions, action items, commitments, or next steps.

Document:
{text[:3000]}

Decisions and Action Items:
"""
    return call_llm(prompt)

def analyze_document(topic: str, text: str, run_all: bool = True) -> dict:
    """
    Run all document analysis agents
    
    Args:
        topic: Topic name
        text: Document text
        run_all: Run all agents or just individual
    
    Returns:
        Dictionary with analysis results
    """
    results = {}
    
    # Log the original document
    log_agent_response(topic, "Document Upload", f"Document uploaded: {len(text)} characters")
    
    # Run all agents
    if run_all:
        # Summary Agent
        summary = summarize_document(text)
        log_agent_response(topic, "Summary Agent", summary)
        results["summary"] = summary
        
        # Red Flag Detector
        red_flags = detect_red_flags(text)
        log_agent_response(topic, "Red Flag Detector", red_flags)
        results["red_flags"] = red_flags
        
        # Decision Extractor
        decisions = extract_decisions(text)
        log_agent_response(topic, "Decision Extractor", decisions)
        results["decisions"] = decisions
    
    return results