#!/bin/bash

input_file="log.lammps"
output_file="LogLog_1000"

# Check if the input file exists
if [ ! -f "$input_file" ]; then
    echo "Input file '$input_file' not found."
    exit 1
fi

# Extract and format the desired columns from "LogLog" lines
awk '/LogLog/ { if (NF == 6) print $2, $3, $4, $5, $6 }' "$input_file" > "$output_file"

echo "Desired columns from 'LogLog' lines have been extracted and written to '$output_file'."
