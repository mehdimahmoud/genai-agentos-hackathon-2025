"""
Standalone A2A Protocol Types

This module provides the necessary A2A protocol types and classes
without depending on the backend's a2a.server module.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, List, Optional
from uuid import uuid4

from pydantic import BaseModel


# Basic A2A Protocol Types
class AgentCapabilities(BaseModel):
    streaming: bool = True
    pushNotifications: bool = False
    stateTransitionHistory: bool = False


class AgentSkill(BaseModel):
    id: str
    name: str
    description: str
    examples: Optional[List[str]] = None
    inputModes: Optional[List[str]] = None
    outputModes: Optional[List[str]] = None
    tags: List[str] = []


class AgentCard(BaseModel):
    name: str
    description: str
    url: str
    version: str
    defaultInputModes: List[str]
    defaultOutputModes: List[str]
    capabilities: AgentCapabilities
    skills: List[AgentSkill]


# Task and Context Types
@dataclass
class RequestContext:
    """Context for A2A requests."""
    user_id: str
    session_id: str
    task_id: Optional[str] = None
    message: Optional[Dict[str, Any]] = None
    
    def get_user_input(self) -> str:
        """Get user input from the message."""
        if self.message and "content" in self.message:
            return self.message["content"]
        return ""


@dataclass
class Task:
    """A2A Task representation."""
    id: str
    context_id: str
    state: str = "pending"
    
    @classmethod
    def create(cls, context_id: str) -> "Task":
        return cls(id=str(uuid4()), context_id=context_id)


class TaskState:
    """Task states."""
    PENDING = "pending"
    WORKING = "working"
    COMPLETED = "completed"
    FAILED = "failed"


# Event Queue
class EventQueue:
    """Simple event queue for A2A protocol."""
    
    def __init__(self):
        self.events: List[Dict[str, Any]] = []
    
    async def enqueue_event(self, event: Dict[str, Any]) -> None:
        """Enqueue an event."""
        self.events.append(event)
    
    async def enqueue_text_message(self, content: str, context_id: str, task_id: str) -> None:
        """Enqueue a text message event."""
        await self.enqueue_event({
            "type": "text",
            "content": content,
            "context_id": context_id,
            "task_id": task_id
        })


# Task Updater
class TaskUpdater:
    """Task updater for A2A protocol."""
    
    def __init__(self, event_queue: EventQueue, task_id: str, context_id: str):
        self.event_queue = event_queue
        self.task_id = task_id
        self.context_id = context_id
    
    async def update_status(self, state: str, message: Dict[str, Any], final: bool = False) -> None:
        """Update task status."""
        await self.event_queue.enqueue_event({
            "type": "task_update",
            "task_id": self.task_id,
            "context_id": self.context_id,
            "state": state,
            "message": message,
            "final": final
        })


# Agent Executor Interface
class AgentExecutor(ABC):
    """Abstract base class for A2A agent executors."""
    
    @abstractmethod
    async def execute(self, context: RequestContext, event_queue: EventQueue) -> None:
        """Execute the agent."""
    
    @abstractmethod
    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> Optional[Task]:
        """Cancel the task execution."""


# Utility Functions
def new_task(message: Dict[str, Any]) -> Task:
    """Create a new task from a message."""
    context_id = str(uuid4())
    return Task.create(context_id)


def new_agent_text_message(content: str, context_id: str, task_id: str) -> Dict[str, Any]:
    """Create a new agent text message."""
    return {
        "type": "text",
        "content": content,
        "context_id": context_id,
        "task_id": task_id
    } 