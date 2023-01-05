"""

Goal:

We want to be able to customise what a function does in a flexible way.

Below we demonstrate the "mode function parameter" pattern (I don't know what the name for this is).
The behaviour of the do_something() function is customised based which mode we select.

"""


def do_something(a, b, mode="add", value_on_zero_division=0):
    """Returns the result of applying an operation to two numbers - add, subtract, multiply or
     divide.  The divide option is able to manage a Zero Division Error with a default result of 0."""
    if mode == "add":
        return add(a, b)
    elif mode == "subtract":
        return subtract(a, b)
    elif mode == "multiply":
        return multiply(a, b)
    elif mode == "divide":
        return divide(a, b, value_on_zero_division)
    else:
        raise Exception(f"'{mode}' mode not supported")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b, value_on_zero_division):
    """Divide one floating point number by another and return the answer.  Manage a Zero Division Error
     with a default value defined by the main function."""
    try:
        return a / b
    except ZeroDivisionError:
        return value_on_zero_division


def test_do_something():
    print(f"Expected 5, got: {do_something(3, 2)}")
    print(f"Expected 5, got: {do_something(3, 2, 'add')}")
    print(f"Expected 1, got: {do_something(3, 2, 'subtract')}")
    print(f"Expected 6, got: {do_something(3, 2, 'multiply')}")


if __name__ == '__main__':
    test_do_something()


class Something:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self, value_on_zero_division=0):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return value_on_zero_division


c = Something(16, 5)
print(Something.add(c))


class ExtendSomething(Something):

    def __init__(self, a=0, b=0):
        super().__init__(a=0, b=0)

    def modulo(self):
        return self.a % self.b


b = ExtendSomething(12, 5)
print(ExtendSomething.add(b))
