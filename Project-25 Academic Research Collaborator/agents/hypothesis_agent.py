
from agents.base import call_llm, log_agent_response

def run(topic: str, hypothesis: str, evidence: str) -> str:
    """Validate hypothesis"""
    
    prompt = f"""
You are a Hypothesis Validator Agent. Evaluate this hypothesis based on evidence.

Hypothesis: {hypothesis}

Evidence:
{evidence}

Provide:
1. **Validation** - Does the evidence support the hypothesis?
2. **Strength** - How strong is the evidence? (Weak/Moderate/Strong)
3. **Alternative Explanations** - What else could explain the findings?
4. **Methodological Issues** - Are there any issues with the evidence?
5. **Recommendations** - What further evidence is needed?
6. **Confidence Level** (1-10)

Hypothesis Validation:
"""
    
    validation = call_llm(prompt)
    log_agent_response(topic, "Hypothesis Validator", validation)
    return validation

def generate_hypotheses(topic: str, research_question: str) -> str:
    """Generate hypotheses"""
    
    prompt = f"""
You are a Hypothesis Validator Agent. Generate 3-5 testable hypotheses based on the research question.

Research Question: {research_question}

Hypotheses:
"""
    
    hypotheses = call_llm(prompt)
    log_agent_response(topic, "Hypothesis Validator (Generated)", hypotheses)
    return hypotheses