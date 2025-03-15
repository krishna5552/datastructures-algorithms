from list_implementation import Stack

def reverse_string(string):
    s = Stack()
    reversed_string = ""

    for char in string:
        s.push(char)

    while not s.is_empty():
        reversed_string += s.pop()

    return reversed_string

test_strings = [
    "",                # Empty string
    "a",               # Single character
    "madam",           # Palindrome
    "hello, world!",   # Special characters
    "a" * 1000         # Long string
]

for string in test_strings:
    print(f"'{string}' reversed is: '{reverse_string(string)}'")
    