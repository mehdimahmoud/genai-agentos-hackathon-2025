"""
Text Summarizer Tool

This module provides text summarization functionality.
"""

import json
from typing import Optional


def summarize_text(text: str, max_length: Optional[int] = 100, tool_context=None) -> str:
    """
    Create a summary of the given text.
    
    Args:
        text (str): The text to summarize
        max_length (int): Maximum length of summary
        tool_context: The context in which the tool operates (optional for compatibility)
        
    Returns:
        str: JSON string containing summary results
    """
    if not text.strip():
        return json.dumps({"error": "No text provided for summarization"})
    
    # Simple summarization
    sentences = text.split('.')
    sentences = [s.strip() for s in sentences if s.strip()]
    
    if not sentences:
        return json.dumps({"error": "No valid sentences found"})
    
    # Take first few sentences as summary
    summary_sentences = sentences[:2]
    summary = '. '.join(summary_sentences) + '.'
    
    # Truncate if too long
    if max_length and len(summary) > max_length:
        summary = summary[:max_length-3] + "..."
    
    result = {
        "original_text": text,
        "summary": summary,
        "original_length": len(text),
        "summary_length": len(summary),
        "compression_ratio": round(len(summary) / len(text) * 100, 2)
    }
    
    if tool_context:
        tool_context.actions.skip_summarization = True
    
    return json.dumps(result) 