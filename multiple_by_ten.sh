#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <input_file>"
    exit 1
fi

input_file=$1

if [ ! -f "$input_file" ]; then
    echo "File not found. Please provide a valid file name."
    exit 1
fi

number=$(cat "$input_file")
if ! [[ $number =~ ^[0-9]+(\.[0-9]+)?$ ]]; then
    echo "The file does not contain a valid number."
    exit 1
fi

multiplied=$(awk "BEGIN { printf \"%.14f\", $number * 10 }")
echo "The number $number multiplied by 10 is $multiplied."

echo "$multiplied" > multiplication.txt