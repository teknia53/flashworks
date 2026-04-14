#!/bin/bash
# FlashWorks Launcher
# Double-click this file to start FlashWorks in your browser.

cd "$(dirname "$0")"

PORT=8234

# Check if something is already using the port
if lsof -i :$PORT > /dev/null 2>&1; then
    echo "FlashWorks is already running (or port $PORT is in use)."
    open "http://localhost:$PORT"
    exit 0
fi

echo "Starting FlashWorks on http://localhost:$PORT ..."
echo "Close this terminal window to stop the server."
echo ""

# Open the browser after a short delay
(sleep 1 && open "http://localhost:$PORT") &

# Start the server (blocks until you close the terminal)
python3 -m http.server $PORT
