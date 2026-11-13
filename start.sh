#!/usr/bin/env bash
# API stays on localhost (not exposed publicly); only the Streamlit UI is public on $PORT.
set -e
PORT="${PORT:-7860}"
uvicorn app.api:app --host 127.0.0.1 --port 8000 &
exec streamlit run app/ui.py --server.port "$PORT" --server.address 0.0.0.0 \
     --server.headless true --browser.gatherUsageStats false
