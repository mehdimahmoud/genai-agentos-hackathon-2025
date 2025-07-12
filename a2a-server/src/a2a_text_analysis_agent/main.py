"""
A2A Text Analysis Agent Main Application

This is the main entry point for the A2A text analysis agent server.
"""

import os
import uvicorn
from .services.a2a_server import create_a2a_server


def main():
    """Main application entry point."""
    # Create the A2A server
    server = create_a2a_server()
    
    # Get configuration from environment variables
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "10002"))
    debug = os.getenv("DEBUG", "false").lower() == "true"
    
    # Start the server using the built Starlette app
    uvicorn.run(
        server.build(),
        host=host,
        port=port,
        log_level="info" if not debug else "debug"
    )


if __name__ == "__main__":
    main() 