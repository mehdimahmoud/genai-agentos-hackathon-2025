"""
Text Paraphraser Tool

This module provides text paraphrasing functionality.
"""

import json
import re
from typing import Optional


def paraphrase_text(text: str, style: Optional[str] = "formal", tool_context=None) -> str:
    """
    Paraphrase the given text in different styles.
    
    Args:
        text (str): The text to paraphrase
        style (str): The style to use ("formal", "casual", "academic", "simple")
        tool_context: The context in which the tool operates (optional for compatibility)
        
    Returns:
        str: JSON string containing paraphrasing results
    """
    if not text.strip():
        return json.dumps({"error": "No text provided for paraphrasing"})
    
    # Simple paraphrasing using synonym replacement
    synonyms = {
        "good": ["excellent", "great", "fine", "superb", "outstanding"],
        "bad": ["poor", "terrible", "awful", "dreadful", "horrible"],
        "big": ["large", "huge", "enormous", "massive", "substantial"],
        "small": ["tiny", "little", "miniature", "petite", "compact"],
        "important": ["significant", "crucial", "essential", "vital", "key"],
        "think": ["believe", "consider", "suppose", "assume", "reckon"],
        "say": ["state", "mention", "declare", "announce", "express"],
        "get": ["obtain", "acquire", "receive", "gain", "secure"],
        "make": ["create", "produce", "generate", "develop", "establish"],
        "use": ["utilize", "employ", "apply", "implement", "leverage"],
    }
    
    paraphrased = text
    for word, replacements in synonyms.items():
        if word in paraphrased.lower():
            replacement = replacements[0]  # Use first synonym
            paraphrased = re.sub(r'\b' + word + r'\b', replacement, paraphrased, flags=re.IGNORECASE)
    
    result = {
        "original_text": text,
        "paraphrased_text": paraphrased,
        "style": style,
        "changes_made": text != paraphrased
    }
    
    if tool_context:
        tool_context.actions.skip_summarization = True
    
    return json.dumps(result) 