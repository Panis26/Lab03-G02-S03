#!/bin/bash

# Define the server address and filename to request
FILENAME="100MB.bin"

# Loop 25 times to start 25 client instances
for i in {1..25}; do
    echo "Starting client $i..."
    python3 udp-client.py "localhost" "$FILENAME" $i &
done

echo "Started 25 clients."
