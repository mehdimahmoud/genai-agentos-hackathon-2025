"""
A2A Text Analysis Agent

A proper A2A (Agent-to-Agent Protocol) compliant text analysis agent
that follows the A2A protocol specification and uses Google ADK for
seamless integration with the A2A ecosystem.
"""

__version__ = "0.1.0"
__author__ = "Mehdi K."
__description__ = "A2A Protocol Compliant Text Analysis Agent"

from .agents.text_analysis_agent import A2ATextAnalysisAgent

__all__ = [
    "A2ATextAnalysisAgent",
]
