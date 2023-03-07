# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’)
# and an arbitrary number of arguments (only numbers) as the second parameter.

# def make_operation(a, b, c):
#     return (a + b + c)
# print(make_operation(7, 7, 2))

# def make_operation(a, b, c, d):
#     return (a - b - c - d)
# print(make_operation(5, 5, -10, -20))

def make_operation(a, b):
    return (a * b)


print(make_operation(7, 6))


def make_operation_new(operator: str, *args):
    ...  # some logic


make_operation_new("+", 1, 3, 4, 5)  # expected result: 13
make_operation_new("-", 1, 3, 4, 5)  # expected result: -11
make_operation_new("*", 1, 3, 4, 5)  # expected result: 60
