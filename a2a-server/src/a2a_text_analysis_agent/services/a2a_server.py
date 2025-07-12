"""
A2A Protocol Server Implementation

This module provides a server that implements the A2A protocol
for the text analysis agent using the Google A2A library.
"""

import os

from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCapabilities, AgentCard, AgentSkill

from ..agents.text_analysis_agent import A2ATextAnalysisAgent

def create_a2a_server() -> A2AStarletteApplication:
    """
    Create an A2A protocol compliant server using the Google A2A library.
    
    Returns:
        A2AStarletteApplication: Configured A2A server
    """
    # Create the text analysis agent
    agent = A2ATextAnalysisAgent()
    
    # Define agent skills
    skills = [
        AgentSkill(
            id="sentiment_analysis",
            name="Sentiment Analysis Tool",
            description="Analyzes the sentiment of a given text and returns whether it is positive, negative, or neutral.",
            examples=[
                "I love this product!",
                "This is the worst service ever.",
                "I feel okay about it."
            ],
            inputModes=["text", "text/plain"],
            outputModes=["text", "text/plain"],
            tags=["sentiment", "text analysis", "emotion detection"]
        ),
        AgentSkill(
            id="summarize",
            name="Text Summarization Tool",
            description="Provides a concise summary of a longer text passage.",
            examples=[
                "Summarize this: Artificial intelligence is transforming industries by automating tasks and providing new insights from data."
            ],
            inputModes=["text", "text/plain"],
            outputModes=["text", "text/plain"],
            tags=["summarization", "text compression", "NLP"]
        ),
        AgentSkill(
            id="grammar_check",
            name="Grammar Checking Tool",
            description="Detects grammatical errors in text and suggests corrections.",
            examples=[
                "Check grammar: I has an apple.",
                "Check grammar: The dog runs fast."
            ],
            inputModes=["text", "text/plain"],
            outputModes=["text", "text/plain"],
            tags=["grammar", "proofreading", "text improvement"]
        ),
        AgentSkill(
            id="entity_extraction",
            name="Entity Extraction Tool",
            description="Extracts named entities such as people, locations, organizations, etc., from text.",
            examples=[
                "Extract entities from: Apple was founded by Steve Jobs in California."
            ],
            inputModes=["text", "text/plain"],
            outputModes=["text", "text/plain"],
            tags=["entities", "text processing", "NLP"]
        ),
        AgentSkill(
            id="paraphrase",
            name="Paraphrasing Tool",
            description="Rephrases text to have a similar meaning using different words.",
            examples=[
                "Paraphrase: I want to go to the store.",
                "Paraphrase: She loves reading books."
            ],
            inputModes=["text", "text/plain"],
            outputModes=["text", "text/plain"],
            tags=["paraphrasing", "text rewriting", "NLP"]
        ),
    ]
    
    # Define capabilities
    capabilities = AgentCapabilities(
        streaming=True,
        pushNotifications=False,
        stateTransitionHistory=False
    )
    
    # Create agent card
    agent_card = AgentCard(
        name="Text Analysis Agent",
        description="A versatile AI assistant for text-related tasks such as sentiment analysis, summarization, grammar checking, entity extraction, and paraphrasing.",
        url=os.getenv("A2A_AGENT_URL", "http://host.docker.internal:10002/"),
        version="1.0.0",
        defaultInputModes=["text", "text/plain"],
        defaultOutputModes=["text", "text/plain"],
        capabilities=capabilities,
        skills=skills,
    )
    
    # Create request handler with agent executor
    request_handler = DefaultRequestHandler(
        agent_executor=agent,
        task_store=InMemoryTaskStore(),
    )
    
    # Create A2A server using the Google A2A library
    server = A2AStarletteApplication(
        agent_card=agent_card, 
        http_handler=request_handler
    )
    
    return server 