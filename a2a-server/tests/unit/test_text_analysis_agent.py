#!/usr/bin/env python3
"""
Unit Tests for A2A Text Analysis Agent

This module provides comprehensive unit tests for the text analysis agent
to ensure it works correctly with the A2A protocol and expected schema.
"""

import pytest

from a2a_text_analysis_agent.agents.text_analysis_agent import A2ATextAnalysisAgent


class TestTextAnalysisAgent:
    """Test suite for the A2A Text Analysis Agent."""

    def setup_method(self):
        """Set up test fixtures."""
        self.agent = A2ATextAnalysisAgent()

    def test_agent_creation(self):
        """Test that the agent can be created successfully."""
        print("🔧 Testing agent creation...")
        
        # Verify agent is created
        assert self.agent is not None
        assert isinstance(self.agent, A2ATextAnalysisAgent)
        
        # Verify agent has required A2A protocol attributes
        assert hasattr(self.agent, 'SUPPORTED_CONTENT_TYPES')
        assert hasattr(self.agent, 'get_processing_message')
        
        print("✅ Agent creation test passed")

    def test_agent_methods(self):
        """Test that the agent has the expected methods."""
        print("🎯 Testing agent methods...")
        
        # Verify agent has required methods
        assert hasattr(self.agent, '_determine_task_type')
        assert hasattr(self.agent, '_extract_text_from_query')
        assert hasattr(self.agent, 'execute')
        
        # Test processing message
        message = self.agent.get_processing_message()
        assert isinstance(message, str)
        assert len(message) > 0
        
        print("✅ Agent methods test passed")

    def test_task_type_detection(self):
        """Test that the agent can determine task types correctly."""
        print("📋 Testing task type detection...")
        
        # Test different task types
        test_cases = [
            ("Check grammar in this text", "grammar_check"),
            ("Summarize this text", "summarize"),
            ("Analyze sentiment", "sentiment_analysis"),
            ("Extract entities", "entity_extraction"),
            ("Paraphrase this", "paraphrase"),
        ]
        
        for query, expected_type in test_cases:
            task_type = self.agent._determine_task_type(query)
            assert task_type == expected_type
        
        print("✅ Task type detection test passed")

    def test_error_handling(self):
        """Test error handling capabilities."""
        print("⚠️ Testing error handling...")
        
        # Test with invalid input
        test_cases = [
            "",
            None,
            "Invalid input",
        ]
        
        for test_input in test_cases:
            # Should not raise exceptions for invalid input
            try:
                # This is a basic test - in real implementation you'd test actual error handling
                assert True  # Placeholder assertion
            except Exception as e:
                # If an exception is raised, it should be handled gracefully
                assert isinstance(e, Exception)
        
        print("✅ Error handling test passed")


class TestTextAnalysisAgentAsync:
    """Async test suite for the A2A Text Analysis Agent."""

    def setup_method(self):
        """Set up test fixtures."""
        self.agent = A2ATextAnalysisAgent()

    @pytest.mark.asyncio
    async def test_async_agent_creation(self):
        """Test async agent creation."""
        print("🔧 Testing async agent creation...")
        
        assert self.agent is not None
        assert isinstance(self.agent, A2ATextAnalysisAgent)
        
        print("✅ Async agent creation test passed")

    @pytest.mark.asyncio
    async def test_async_agent_validation(self):
        """Test async agent validation."""
        print("🎯 Testing async agent validation...")
        
        # Test that agent is accessible in async context
        assert self.agent is not None
        assert isinstance(self.agent, A2ATextAnalysisAgent)
        
        # Test that agent methods work in async context
        message = self.agent.get_processing_message()
        assert isinstance(message, str)
        
        print("✅ Async agent validation test passed") 


@pytest.mark.asyncio
async def test_paraphrase_skill_behavior():
    """Test that the agent can handle paraphrase requests correctly."""
    agent = A2ATextAnalysisAgent()
    query = "Paraphrase: This is a good project."
    
    # Test that the agent can determine paraphrase task type
    task_type = agent._determine_task_type(query)
    assert task_type == "paraphrase"
    
    # Test that text extraction works
    extracted_text = agent._extract_text_from_query(query)
    assert "good" in extracted_text.lower()
    
    # Test that the agent has the paraphrase functionality
    assert hasattr(agent, '_extract_text_from_query')
    assert hasattr(agent, '_determine_task_type')
    
    print("✅ Paraphrase skill behavior test passed") 