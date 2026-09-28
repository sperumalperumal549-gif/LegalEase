#!/usr/bin/env bash
# Starts backend (port 8000) and frontend (port 8501)
cd "$(dirname "$0")"
[ -d venv ] && source venv/bin/activate
uvicorn legalEaseAPI.main:app --port 8000 &
BACKEND_PID=$!
trap "kill $BACKEND_PID 2>/dev/null" EXIT
sleep 3
streamlit run frontend/app.py
