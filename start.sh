#!/bin/bash
cd /app/backend
source venv/bin/activate
uvicorn main:app --host 0.0.0.0 --port 8000 &
nginx -g "daemon off;"
