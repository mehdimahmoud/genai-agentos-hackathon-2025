# Google Drive MCP Integration

This project provides a **Model Context Protocol (MCP)** server for integrating with Google Drive, allowing you to search, retrieve, and process Google Docs and Drive files via a unified API. It is containerized with Docker and easily managed with Makefile commands.

---

## Features
- Search and retrieve Google Drive documents
- Convert Google Docs to HTML or Markdown
- Expose endpoints for SSE and StreamableHTTP
- Fully containerized with Docker Compose
- Easy build/run/cleanup with Makefile

---

## Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Python 3.12+](https://www.python.org/downloads/) (for local development)
- Google Cloud project with Google Drive API enabled

---

## Setup

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd mcp_servers/google_drive
```

### 2. Google API Credentials
To access private Google Drive data, you need OAuth 2.0 credentials:
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project (if you don't have one)
3. Enable the **Google Drive API**
4. Go to **APIs & Services > Credentials**
5. Click **Create Credentials > OAuth client ID**
6. Download the `client_secret.json` file
7. Place it in the project directory (and mount it in Docker if needed)

> **Note:** For public data only, you can use an API key, but most use cases require OAuth.

### 3. Environment Variables
Create a `.env` file in this directory (if needed):
```env
GOOGLE_DRIVE_MCP_SERVER_PORT=5001
# Add any other required environment variables here
```

---

## Usage

### With Docker Compose & Makefile
All commands should be run from the `mcp_servers/google_drive` directory.

#### Build the Docker image
```bash
make docker
```

#### Run the server (foreground)
```bash
make up
```

#### Run the server (detached/background)
```bash
make upd
```

#### Stop the server
```bash
make down
```

#### Remove the Docker image
```bash
make rm
```

---

## Endpoints
- **SSE:** `http://localhost:5001/sse`
- **StreamableHTTP:** `http://localhost:5001/mcp`

---

## Development

### Local Python (without Docker)
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the server:
   ```bash
   python server.py
   ```

### Logs & Source Code
- Logs are stored in the `logs/` directory (mounted as a volume in Docker)
- Source code can be edited in `src/` and is mounted for live development

---

## Python Dependencies
See `requirements.txt` for the full list. Key packages:
- `google-api-python-client`, `google-auth`, `google-auth-oauthlib`, `google-auth-httplib2`
- `fastapi`, `uvicorn`, `starlette`, `click`, `python-dotenv`

---

## Troubleshooting
- **Port Issues:** Ensure `GOOGLE_DRIVE_MCP_SERVER_PORT` is set correctly in your `.env` file.
- **Google API 403 Errors:** Make sure you are using valid OAuth credentials and have enabled the Drive API.
- **Container Not Starting:** Run `make rm` and `make docker` to rebuild from scratch.

---

## License
MIT or your project license here. 