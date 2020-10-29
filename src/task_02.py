"""
Create a function that returns True if the given string has any of the following:

Only letters and no numbers.
Only numbers and no letters.
If a string has both numbers and letters or contains characters that don't fit into any category, return False.

Examples:

csAlphanumericRestriction("Bold") ➞ True
csAlphanumericRestriction("123454321") ➞ True
csAlphanumericRestriction("H3LL0") ➞ False

Notes:

Any string that contains spaces or is empty should return False.

[execution time limit] 4 seconds (py3)

[input] string input_str

[output] boolean

[Python 3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name

"""

def csAlphanumericRestriction(input_str:str) -> bool:
    if input_str.isdigit() or input_str.isalpha():
        return True
    elif input_str.isalpha() and input_str.isdigit():
        return False
    elif len(input_str) == 0 or input_str.isspace():
        return False
    return False
    
print(csAlphanumericRestriction("Bold"))
print(csAlphanumericRestriction("123454321"))
print(csAlphanumericRestriction("H3llo"))
print(csAlphanumericRestriction("|ax:ik\tN?Y"))
