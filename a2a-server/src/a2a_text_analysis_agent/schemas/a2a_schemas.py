"""
A2A Protocol Schema Classes

This module contains the A2A protocol schema classes that are duplicated
for independence from the backend project. These classes follow the A2A
protocol specification as defined by Google.
"""

from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, Field


class A2AAgentCapabilities(BaseModel):
    """A2A Agent Capabilities schema."""
    pushNotifications: Optional[bool] = None
    stateTransitionHistory: Optional[bool] = None
    streaming: Optional[bool] = None


class A2AAgentProvider(BaseModel):
    """A2A Agent Provider schema."""
    organization: str
    url: str


class A2AAgentSkill(BaseModel):
    """A2A Agent Skill schema."""
    id: str
    name: str
    description: str
    examples: list[str] | None = None
    inputModes: list[str] | None = None
    outputModes: list[str] | None = None
    tags: list[str] = []


class A2AAgentCard(BaseModel):
    """A2A Agent Card schema."""
    name: str
    description: str
    provider: Optional[A2AAgentProvider] = None
    defaultInputModes: list[str]
    defaultOutputModes: list[str]
    documentationUrl: Optional[str] = None
    security: Optional[list[dict[str, list[str]]]] = None
    securitySchemes: Optional[dict[str, Any]] = None
    skills: list[A2AAgentSkill]
    supportsAuthenticatedExtendedCard: Optional[bool] = None
    url: str
    version: str
    capabilities: A2AAgentCapabilities


class A2AJsonSchema(BaseModel):
    """
    Model to structure adjusted A2A agent schema without the a2a agent skills.
    """
    title: str
    description: str
    properties: dict[str, Any] = Field(
        default={
            "task": {
                "type": "string",
                "description": "A meaningful, well-formulated task for the agent",
            },
            "text": {"type": "string"},
        },
    )
    required: list[Optional[str]] = Field(default=["task", "text"])
    type: Optional[str] = Field(default="object")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None 