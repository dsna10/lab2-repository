#!/usr/bin/env python3
import sys

# Check if exactly 3 arguments are provided (script name + 2 arguments)
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit(1)  # Exit with an error status

name = sys.argv[1]  # First argument (name)
age = sys.argv[2]   # Second argument (age)

# Ensure that age is a valid integer
try:
    age = int(age)  # Convert age to an integer
except ValueError:
    print("Error: Age must be a number.")
    sys.exit(1)

# Print output exactly as expected
print(f"Hi {name}, you are {age} years old.")

