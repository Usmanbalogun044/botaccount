#!/bin/bash

# Infinite loop to restart the script if it crashes
while true
do
    echo "Starting bot script..."
    python3 botaccount.py
    echo "Script crashed with exit code $?. Restarting in 5 seconds..."
    sleep 5
done
