from list_implementation import Stack

def decimal_integer_to_binary(decimal_integer):
    s = Stack()
    binary_string = ""

    while decimal_integer > 0:
        remainder = decimal_integer % 2
        s.push(remainder)
        decimal_integer = decimal_integer // 2

    while not s.is_empty():
        binary_string += str(s.pop())
    return binary_string

test_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1000]
for integer in test_integers:
    print(f"{integer} in binary is: {decimal_integer_to_binary(integer)}")

