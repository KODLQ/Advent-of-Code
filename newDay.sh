#!/bin/bash

# Get the year and day from command line arguments
year=$1
day=$2

# Check if year and day are provided
if [ -z "$year" ] || [ -z "$day" ]; then
  echo "Usage: $0 <year> <day>"
  exit 1
fi

# Create the year directory if it doesn't exist
mkdir -p "/home/oscar/OscarGit/advent-of-code/$year"

# Create the day directory if it doesn't exist
day_dir="/home/oscar/OscarGit/advent-of-code/$year/day-$day"
mkdir -p "$day_dir"

# Create the main.py file if it doesn't exist
if [ ! -f "$day_dir/main.py" ]; then
  cat > "$day_dir/main.py" << EOF
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from GetInput import getInput

getInput($year, $day)

def main():
    return

if __name__ == "__main__":
    main()
EOF
fi

cd $day_dir
echo "Created directory '$day_dir'"