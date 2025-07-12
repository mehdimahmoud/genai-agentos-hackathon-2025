#!/usr/bin/env python3
"""
A2A Text Analysis Agent Server

This is the main entry point for the A2A text analysis agent server.
"""

import os
from pathlib import Path
import sys

# Add the src directory to the Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from a2a_text_analysis_agent.services.a2a_server import create_a2a_server

# Create the A2A server and expose the ASGI app
server = create_a2a_server()
app = server.build()  # This is the ASGI app for Uvicorn

if __name__ == "__main__":
    import uvicorn
    host = os.getenv("A2A_SERVER_HOST", "0.0.0.0")
    port = int(os.getenv("A2A_SERVER_PORT", "10002"))
    log_level = os.getenv("LOG_LEVEL", "info")
    uvicorn.run(app, host=host, port=port, log_level=log_level) 