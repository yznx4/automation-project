import re

# The regular expression pattern
pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*\d+$'

# Test cases
testCases = [
    "x = 10",
    "myVar = 20",
    "1x = 10",
    "var@name = 30",
    "_validVar123 = 45"
]

for test in testCases:
    match = re.match(pattern, test)
    if match:
        print("(" + test + ")" + " is valid.")
    else:
        print("(" + test + ")" + " is not valid.")
