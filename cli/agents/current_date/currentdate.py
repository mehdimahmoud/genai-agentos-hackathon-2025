import asyncio
from typing import Annotated
from genai_session.session import GenAISession
from genai_session.utils.context import GenAIContext
from datetime import datetime

AGENT_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzY2VhYmE2Mi1hNjcxLTRjYTgtOWNjYi1iZjQ5MTA0NmQxOTAiLCJleHAiOjI1MzQwMjMwMDc5OSwidXNlcl9pZCI6IjI4ZWUwM2NhLTZlMjctNGUyZC04ZmI1LWQwOGIyNGU2NzM5MiJ9.BdbqlsLMiCEHvy12qK4IimTfPTt9frHCvpLUwHCn8aI" # noqa: E501
session = GenAISession(jwt_token=AGENT_JWT)


@session.bind(
    name="current_date",
    description="Agent that returns current date"
)
async def currentdate(agent_context: GenAIContext):
    """Agent that returns current date"""
    return datetime.now().strftime("%Y-%m-%d")


async def main():
    print(f"Agent with token '{AGENT_JWT}' started")
    await session.process_events()

if __name__ == "__main__":
    asyncio.run(main())
