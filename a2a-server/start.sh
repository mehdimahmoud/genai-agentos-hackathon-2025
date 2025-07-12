#!/bin/bash

# External A2A Server Startup Script

echo "🚀 Starting External A2A Server..."

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

# Build and start the A2A server
echo "📦 Building A2A server..."
docker compose build --no-cache

if [ $? -eq 0 ]; then
    echo "✅ Build successful!"
    echo ""
    echo "🌐 Starting A2A server on port 10002..."
    docker compose up -d
    
    echo ""
    echo "🎉 External A2A Server is running!"
    echo ""
    echo "📋 Server Details:"
    echo "  - URL: http://localhost:10002"
    echo "  - Agent Card: http://localhost:10002/.well-known/agent.json"
    echo "  - Container: a2a-text-analysis-agent"
    echo ""
    echo "🔗 To connect from GenAI infrastructure:"
    echo "  - From host: http://localhost:10002"
    echo "  - From Docker: http://host.docker.internal:10002"
    echo ""
    echo "🧪 Test the server:"
    echo "  curl http://localhost:10002/.well-known/agent.json"
    echo ""
    echo "📊 View logs:"
    echo "  docker compose logs -f"
    echo ""
    echo "🛑 Stop server:"
    echo "  docker compose down"
else
    echo "❌ Build failed!"
    exit 1
fi 