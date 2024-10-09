#!/bin/bash
echo "task1.sh started successfully"
PID=$(pgrep -f infinite.sh)
if [ -n "$PID" ]; then
	kill "$PID"
	echo "process infinite.sh found with pid $PID and killed"
else 
	echo "process not found infinite.sh"
fi
echo "task1.sh ran successfully"
