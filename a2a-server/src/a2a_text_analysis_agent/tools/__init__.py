"""
Text Analysis Tools

This module contains the text analysis tools that can be used by the A2A agent.
"""

from .grammar_checker import check_grammar
from .sentiment_analyzer import analyze_sentiment
from .statistics_analyzer import count_words_and_characters
from .summarizer import summarize_text
from .paraphraser import paraphrase_text
from .entity_extractor import extract_entities

__all__ = [
    "check_grammar",
    "analyze_sentiment", 
    "count_words_and_characters",
    "summarize_text",
    "paraphrase_text",
    "extract_entities",
]
