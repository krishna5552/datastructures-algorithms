from list_implementation import Stack

def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    else:
        return False

def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in '([{':
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False

paren_strings = [
    "",         # Empty string
    "((()))",   # Single type of parentheses
    "({[()]})", # Mixed types of parentheses
    "({[})",    # Unbalanced parentheses
    "))))",     # Only closing parentheses
    "((("       # Only opening parentheses
]

for ps in paren_strings:
    print(f"{ps}: {is_paren_balanced(ps)}")