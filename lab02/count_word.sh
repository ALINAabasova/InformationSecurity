#!/bin/bash
# Usage: count_word.sh <file> <word>
if [ $# -ne 2 ]; then
    echo "Usage: $0 <file> <word>"
    exit 1
fi
file=$1
word=$2
if [ ! -f "$file" ]; then
    echo "Error: file '$file' not found"
    exit 1
fi
count=$(grep -o -w -- "$word" "$file" | wc -l)
echo "The word '$word' appears $count times in $file"
