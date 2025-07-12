"""
A2A Text Analysis Agent - A2A Protocol Compliant Implementation

This module implements a text analysis agent that follows the A2A protocol specification
using simple text processing functions without requiring any AI API keys.
"""

import json
import re
from typing import Any

from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.server.tasks import TaskUpdater
from a2a.types import (
    Part,
    TaskState,
    TextPart,
    UnsupportedOperationError,
)
from a2a.utils import new_agent_text_message, new_task
from a2a.utils.errors import ServerError

def check_grammar(text: str) -> dict[str, Any]:
    """
    Check grammar and syntax in the given text.
    
    Args:
        text: The text to check
        
    Returns:
        Dictionary with grammar analysis results
    """
    # Simple grammar checking logic
    errors = []
    suggestions = []
    
    # Check for common grammar issues
    if "i " in text.lower():
        errors.append("Use 'I' instead of 'i' for the first person pronoun")
        suggestions.append("Capitalize 'i' to 'I'")
    
    if "  " in text:
        errors.append("Multiple spaces detected")
        suggestions.append("Remove extra spaces")
    
    return {
        "original_text": text,
        "errors": errors,
        "suggestions": suggestions,
        "error_count": len(errors),
        "is_grammatically_correct": len(errors) == 0
    }

def analyze_sentiment(text: str) -> dict[str, Any]:
    """
    Analyze the sentiment of the given text.
    
    Args:
        text: The text to analyze
        
    Returns:
        Dictionary with sentiment analysis results
    """
    # Simple sentiment analysis using keyword matching
    positive_words = ["good", "great", "excellent", "amazing", "wonderful", "love", "like", "happy", "joy"]
    negative_words = ["bad", "terrible", "awful", "hate", "dislike", "sad", "angry", "frustrated"]
    
    text_lower = text.lower()
    positive_count = sum(1 for word in positive_words if word in text_lower)
    negative_count = sum(1 for word in negative_words if word in text_lower)
    
    if positive_count > negative_count:
        sentiment = "positive"
        confidence = min(0.9, 0.5 + (positive_count - negative_count) * 0.1)
    elif negative_count > positive_count:
        sentiment = "negative"
        confidence = min(0.9, 0.5 + (negative_count - positive_count) * 0.1)
    else:
        sentiment = "neutral"
        confidence = 0.5
    
    return {
        "text": text,
        "sentiment": sentiment,
        "confidence": confidence,
        "positive_score": positive_count,
        "negative_score": negative_count
    }

def summarize_text(text: str, max_length: int = 150) -> dict[str, Any]:
    """
    Create a summary of the given text.
    
    Args:
        text: The text to summarize
        max_length: Maximum length of the summary
        
    Returns:
        Dictionary with summary results
    """
    # Simple summarization by taking the first sentence
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    if not sentences:
        summary = text[:max_length]
    else:
        summary = sentences[0]
        if len(summary) > max_length:
            summary = summary[:max_length] + "..."
    
    return {
        "original_text": text,
        "summary": summary,
        "original_length": len(text),
        "summary_length": len(summary),
        "compression_ratio": len(summary) / len(text) if text else 0
    }

def extract_entities(text: str) -> dict[str, Any]:
    """
    Extract named entities from the given text.
    
    Args:
        text: The text to extract entities from
        
    Returns:
        Dictionary with entity extraction results
    """
    # Simple entity extraction using regex patterns
    entities = []
    
    # Extract names (capitalized words that might be names)
    name_pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
    names = re.findall(name_pattern, text)
    for name in names:
        entities.append({
            "text": name,
            "type": "PERSON",
            "confidence": 0.7
        })
    
    # Extract organizations (words ending with common org suffixes)
    org_pattern = r'\b[A-Z][a-zA-Z]*(?: Inc\.| Corp\.| LLC| Ltd\.| Company| Corporation)\b'
    orgs = re.findall(org_pattern, text)
    for org in orgs:
        entities.append({
            "text": org,
            "type": "ORGANIZATION",
            "confidence": 0.8
        })
    
    # Extract locations (words that might be locations)
    location_pattern = r'\b[A-Z][a-z]+(?: City| State| Country| Street| Avenue| Road)\b'
    locations = re.findall(location_pattern, text)
    for location in locations:
        entities.append({
            "text": location,
            "type": "LOCATION",
            "confidence": 0.6
        })
    
    return {
        "text": text,
        "entities": entities,
        "entity_count": len(entities)
    }

def paraphrase_text(text: str) -> dict[str, Any]:
    """
    Paraphrase the given text.
    
    Args:
        text: The text to paraphrase
        
    Returns:
        Dictionary with paraphrasing results
    """
    # Simple paraphrasing by replacing common words with synonyms
    paraphrases = {
        "good": "excellent",
        "bad": "poor",
        "big": "large",
        "small": "tiny",
        "happy": "joyful",
        "sad": "unhappy",
        "fast": "quick",
        "slow": "sluggish",
        "beautiful": "gorgeous",
        "ugly": "unattractive"
    }
    
    paraphrased = text
    for original, synonym in paraphrases.items():
        paraphrased = re.sub(r'\b' + original + r'\b', synonym, paraphrased, flags=re.IGNORECASE)
    
    return {
        "original_text": text,
        "paraphrased_text": paraphrased,
        "similarity_score": 0.85  # Placeholder similarity score
    }

class A2ATextAnalysisAgent(AgentExecutor):
    """
    A2A-compliant text analysis agent using simple text processing functions.
    
    This agent provides five main capabilities:
    1. Grammar checking
    2. Text summarization
    3. Sentiment analysis
    4. Entity extraction
    5. Text paraphrasing
    """
    
    SUPPORTED_CONTENT_TYPES = ["text", "text/plain"]
    
    def __init__(self):
        """Initialize the text analysis agent."""
        super().__init__()
    
    def get_processing_message(self) -> str:
        """Get the processing message for the agent."""
        return "Processing text analysis request..."
    
    def _determine_task_type(self, query: str) -> str:
        """
        Determine the type of task from the query.
        
        Args:
            query (str): The user query
            
        Returns:
            str: The task type
        """
        query_lower = query.lower()
        
        if any(word in query_lower for word in ['grammar', 'check grammar', 'grammatical']):
            return "grammar_check"
        elif any(word in query_lower for word in ['summarize', 'summary', 'summarization']):
            return "summarize"
        elif any(word in query_lower for word in ['sentiment', 'emotion', 'feeling', 'mood']):
            return "sentiment_analysis"
        elif any(word in query_lower for word in ['entity', 'entities', 'extract', 'named']):
            return "entity_extraction"
        elif any(word in query_lower for word in ['paraphrase', 'rewrite', 'rephrase']):
            return "paraphrase"
        else:
            # Default to sentiment analysis
            return "sentiment_analysis"
    
    def _extract_text_from_query(self, query: str) -> str:
        """
        Extract the text to analyze from the query.
        
        Args:
            query (str): The user query
            
        Returns:
            str: The extracted text
        """
        # Remove task keywords to get the actual text
        task_keywords = [
            'grammar check', 'check grammar', 'summarize', 'sentiment analysis',
            'analyze sentiment', 'paraphrase', 'extract entities'
        ]
        
        text = query
        for keyword in task_keywords:
            text = text.replace(keyword, '').strip()
        
        return text
    
    async def execute(
        self,
        context: RequestContext,
        event_queue: EventQueue,
    ) -> None:
        """
        Execute the text analysis task.
        
        Args:
            context (RequestContext): The request context
            event_queue (EventQueue): The event queue for sending responses
            
        Returns:
            None
        """
        query = context.get_user_input()
        task = context.current_task
        
        # This agent always produces Task objects. If this request does
        # not have current task, create a new one and use it.
        if not task and context.message:
            task = new_task(context.message)
            await event_queue.enqueue_event(task)
        
        if not task:
            return
            
        updater = TaskUpdater(event_queue, task.id, task.contextId)
        
        if not query:
            await updater.update_status(
                TaskState.failed,
                new_agent_text_message("No text provided for analysis.", task.contextId, task.id),
                final=True,
            )
            return
        
        # Determine the task type
        task_type = self._determine_task_type(query)
        text_to_analyze = self._extract_text_from_query(query)
        
        # If no specific text was extracted, use the whole input
        if not text_to_analyze:
            text_to_analyze = query
        
        # Show processing status
        await updater.update_status(
            TaskState.working,
            new_agent_text_message(self.get_processing_message(), task.contextId, task.id),
        )
        
        # Process based on task type
        try:
            if task_type == "grammar_check":
                result = check_grammar(text_to_analyze)
            elif task_type == "summarize":
                result = summarize_text(text_to_analyze)
            elif task_type == "sentiment_analysis":
                result = analyze_sentiment(text_to_analyze)
            elif task_type == "entity_extraction":
                result = extract_entities(text_to_analyze)
            elif task_type == "paraphrase":
                result = paraphrase_text(text_to_analyze)
            else:
                result = {"error": f"Unknown task type: {task_type}"}
            
            # Format the response
            if "error" in result:
                response_text = f"Error: {result['error']}"
            else:
                response_text = json.dumps(result, indent=2)
            
            # Complete the task
            await updater.add_artifact(
                [Part(root=TextPart(text=response_text))], name="analysis_result"
            )
            await updater.complete()
            
        except Exception as e:
            await updater.update_status(
                TaskState.failed,
                new_agent_text_message(f"Error processing request: {str(e)}", task.contextId, task.id),
                final=True,
            )
    
    async def cancel(
        self, context: RequestContext, event_queue: EventQueue
    ) -> None:
        """Cancel the task execution."""
        raise ServerError(error=UnsupportedOperationError()) 