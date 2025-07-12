"""
Sentiment Analyzer Tool

This module provides sentiment analysis functionality.
"""

import json

from google.adk.tools.tool_context import ToolContext


def analyze_sentiment(text: str, tool_context: ToolContext) -> str:
    """
    Analyze the sentiment of the given text.
    
    Args:
        text (str): The text to analyze
        tool_context (ToolContext): The context in which the tool operates
        
    Returns:
        str: JSON string containing sentiment analysis results
    """
    if not text.strip():
        return json.dumps({"error": "No text provided for sentiment analysis"})
    
    # Simple sentiment analysis
    text_lower = text.lower()
    
    # Define positive and negative words
    positive_words = ['good', 'great', 'excellent', 'amazing', 'wonderful', 'happy', 'love', 'like', 'best', 'fantastic']
    negative_words = ['bad', 'terrible', 'awful', 'hate', 'dislike', 'worst', 'horrible', 'sad', 'angry', 'disappointed']
    
    positive_count = sum(1 for word in positive_words if word in text_lower)
    negative_count = sum(1 for word in negative_words if word in text_lower)
    
    # Determine sentiment
    if positive_count > negative_count:
        sentiment = "positive"
        score = min(1.0, positive_count / max(1, positive_count + negative_count))
    elif negative_count > positive_count:
        sentiment = "negative"
        score = min(1.0, negative_count / max(1, positive_count + negative_count))
    else:
        sentiment = "neutral"
        score = 0.5
    
    result = {
        "text": text,
        "sentiment": sentiment,
        "confidence_score": round(score, 2),
        "positive_words_found": positive_count,
        "negative_words_found": negative_count
    }
    
    tool_context.actions.skip_summarization = True
    return json.dumps(result) 