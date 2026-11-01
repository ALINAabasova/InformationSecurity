#!/bin/bash
# Usage: delete_empty_files.sh <directory>
if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi
dir=$1
if [ ! -d "$dir" ]; then
    echo "Error: directory '$dir' not found"
    exit 1
fi
found=0
while IFS= read -r f; do
    rm -- "$f"
    echo "Deleted: $f"
    found=1
done < <(find "$dir" -type f -empty)
if [ $found -eq 0 ]; then
    echo "No empty files found in $dir"
fi
