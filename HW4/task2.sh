#!/bin/bash
grep -rl 'sample' . | while read file; do
	count=$(grep -o 'CSC510' "$file" | wc -l)
	if [ "$count" -ge 3 ]; then
		size=$(stat -c%s "$file")
		echo "$count $size $file"
	fi																				done | sort -k1,1nr -k2,2nr | gawk '{print $1, $2, $3}' | awk '{print $3}' | sed 's/file_/filtered_/g'
