"""

Goal:

We want to be able to customise what a function does in a flexible way.

Below we demonstrate the "mode function parameter" pattern (I don't know what the name for this is).
The behaviour of the do_something() function is customised based which mode we select.

"""


def do_something(a, b, mode="add"):
    if mode == "add":
        return add(a, b)
    elif mode == "subtract":
        return subtract(a, b)
    elif mode == "multiply":
        return multiply(a, b)
    else:
        raise Exception(f"'{mode}' mode not supported")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def test_do_something():
    print(f"Expected 5, got: {do_something(3, 2)}")
    print(f"Expected 5, got: {do_something(3, 2, 'add')}")
    print(f"Expected 1, got: {do_something(3, 2, 'subtract')}")
    print(f"Expected 6, got: {do_something(3, 2, 'multiply')}")


if __name__ == '__main__':
    test_do_something()
