"""
Grammar Checker Tool

This module provides grammar and syntax checking functionality.
"""

import json

from google.adk.tools.tool_context import ToolContext


def check_grammar(text: str, tool_context: ToolContext) -> str:
    """
    Check grammar and syntax in the given text.
    
    Args:
        text (str): The text to analyze
        tool_context (ToolContext): The context in which the tool operates
        
    Returns:
        str: JSON string containing grammar analysis results
    """
    # Simple grammar checks
    issues = []
    
    # Check for common issues
    if not text.strip():
        issues.append("Empty text provided")
    
    # Check for basic punctuation
    if text and not text.endswith(('.', '!', '?')):
        issues.append("Missing ending punctuation")
    
    # Check for capitalization
    if text and not text[0].isupper():
        issues.append("Sentence should start with capital letter")
    
    # Count words
    word_count = len(text.split())
    
    result = {
        "text": text,
        "word_count": word_count,
        "issues_found": len(issues),
        "grammar_issues": issues,
        "overall_score": max(0, 10 - len(issues))  # Simple scoring
    }
    
    tool_context.actions.skip_summarization = True
    return json.dumps(result) 