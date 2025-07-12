"""
Entity Extractor Tool

This module provides named entity extraction functionality.
"""

import json
import re


def extract_entities(text: str, tool_context=None) -> str:
    """
    Extract named entities from the given text.
    
    Args:
        text (str): The text to analyze
        tool_context: The context in which the tool operates (optional for compatibility)
        
    Returns:
        str: JSON string containing entity extraction results
    """
    if not text.strip():
        return json.dumps({"error": "No text provided for entity extraction"})
    
    # Simple entity extraction using regex patterns
    entities = {
        "people": [],
        "organizations": [],
        "locations": [],
        "dates": [],
        "numbers": []
    }
    
    # Extract people (capitalized words that might be names)
    people_pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
    people = re.findall(people_pattern, text)
    entities["people"] = list(set(people))
    
    # Extract organizations (words ending with Inc, Corp, LLC, etc.)
    org_pattern = r'\b[A-Z][a-zA-Z\s]+(?:Inc|Corp|LLC|Ltd|Company|Organization)\b'
    orgs = re.findall(org_pattern, text)
    entities["organizations"] = list(set(orgs))
    
    # Extract locations (words that might be cities/countries)
    location_pattern = r'\b[A-Z][a-z]+(?: City| Town| State| Country)\b'
    locations = re.findall(location_pattern, text)
    entities["locations"] = list(set(locations))
    
    # Extract dates
    date_pattern = r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b|\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4}\b'
    dates = re.findall(date_pattern, text)
    entities["dates"] = list(set(dates))
    
    # Extract numbers
    number_pattern = r'\b\d+(?:\.\d+)?\b'
    numbers = re.findall(number_pattern, text)
    entities["numbers"] = list(set(numbers))
    
    result = {
        "text": text,
        "entities": entities,
        "total_entities": sum(len(v) for v in entities.values())
    }
    
    if tool_context:
        tool_context.actions.skip_summarization = True
    
    return json.dumps(result) 