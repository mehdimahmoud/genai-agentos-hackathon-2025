"""
Statistics Analyzer Tool

This module provides text statistics analysis functionality.
"""

import json


def count_words_and_characters(text: str, tool_context=None) -> str:
    """
    Count words, characters, and other text statistics.
    
    Args:
        text (str): The text to analyze
        tool_context: The context in which the tool operates (optional for compatibility)
        
    Returns:
        str: JSON string containing text statistics
    """
    if not text.strip():
        return json.dumps({"error": "No text provided for analysis"})
    
    # Count characters
    char_count = len(text)
    char_count_no_spaces = len(text.replace(' ', ''))
    
    # Count words
    words = text.split()
    word_count = len(words)
    
    # Count sentences (simple approach)
    sentences = [s.strip() for s in text.split('.') if s.strip()]
    sentence_count = len(sentences)
    
    # Count paragraphs
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    paragraph_count = len(paragraphs)
    
    # Calculate average word length
    avg_word_length = round(sum(len(word) for word in words) / max(1, word_count), 2)
    
    result = {
        "text": text,
        "character_count": char_count,
        "character_count_no_spaces": char_count_no_spaces,
        "word_count": word_count,
        "sentence_count": sentence_count,
        "paragraph_count": paragraph_count,
        "average_word_length": avg_word_length,
        "reading_time_minutes": round(word_count / 200, 1)  # Assuming 200 words per minute
    }
    
    if tool_context:
        tool_context.actions.skip_summarization = True
    
    return json.dumps(result) 