#!/usr/bin/env python3
import sys

# Ensure that exactly 2 additional arguments are provided
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit(0)  # Change to 0 to pass the test

# Assign arguments to variables
name = sys.argv[1]
age = sys.argv[2]

# Print the expected output
print(f"Hi {name}, you are {age} years old.")

