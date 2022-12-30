"""

See something.py first.

Goal:

Now what if we wanted to extend do_something to have a mode for dividing two numbers.
We could call this mode "divide".

Because division by zero causes an error, how about we add an extra parameter for what value to return
when a division by zero occurs. We can call this parameter "value_on_zero_division", which defaults to 0.
So even if we do do_something(2, 0, mode="divide", value_on_zero_division=10) there will be no error.
Instead, 10 will be returned.

Review the code below (at bottom of page) to see how it should be used. Note that currently it will
produce errors.

Problem:

Now you could go back to something.py and add a "divide" mode, and add a value_on_zero_division parameter
to do_something(), perhaps with the default value of 0. For practice, you might want to have a go at this
yourself, then come back and compare with my solution below:

    def do_something(a, b, mode="add", value_on_zero_division=0):
        ...
        elif mode == "multiply":
            return multiply(a, b)
        elif mode == "divide":
            return divide(a, b, value_on_zero_division)
        else:
            raise Exception(f"'{mode}' mode not supported")

    def multiply(a, b):
        return a * b

    def divide(a, b, value_on_zero_division):
        try:
            return a / b
        except ZeroDivisionError:
            return value_on_zero_division

Notice how the parameter "value_on_zero_division" is always present even if we are using a mode that doesn't
need it, like "multiply". This seems wasteful. But worse, it can make the code harder to understand.
As another practice challenge, try to write a complete docstring for the do_something function.
It should list what the modes are and how value_on_zero_division is used.

Here's my version:

    def do_something(a, b, mode="add", value_on_zero_division=0):
        '''Do some operation on a and b, then return the result.

        mode can be "add", "subtract", "multiply" or "divide".
        value_on_zero_division is the value to return when a division by zero occurs while using
        the "divide" mode.'''

Notice how it was hard to write, as well as hard to read. There's a lot going on, and this is just
a simple function. Imagine if we had more modes, where each mode had its own specific set of parameters
that only applied to that particular mode. It would be a mess!

Here's another scenario where this isn't ideal:

What if another teammate was working on something.py, but you wanted to add a new mode or change an
existing mode a little bit. You could go in and mess with something.py yourself, but then the other
person would have to fix any "merge conflicts" between your version and theirs. Alternatively, you
could ask them to make the change for you. Either way, you're forced to disrupt their work.

Another situation might be that you found a Python plugin that almost does what you need.
It has a number of modes that you can choose from, but the mode you need isn't provided.
You don't have access to their code, so it is impossible for you to make the changes yourself!

Separation of concerns:

Should something.py (or some plugin) anticipate every possible mode you might need? Or would it be
better if the user can create their own modes, or even extend existing modes? We could even put our
own modes in our own file (e.g. extend_something.py), without having to touch the original
(e.g. something.py).

If that was possible we could separate how a function is used (e.g. calling do_something) from
what it actually does "under the hood". The technical term for this is separating
interface from implementation. That is a very powerful concept used widely in programming.
I recommend looking up the terms "interface" and "implementation".

The problem:

You could attempt the following challenge (don't start yet...):

Add a new mode called "modulo" that returns the modulus (%)
of a and b when calling do_something(6, 5, mode="modulo")  # result: 1.
BUT only add the mode in this file, without modifying something.py in any way!

Ok, now that you've considered that, you should be totally stumped!
That's because it cannot be done, at least not while using the "mode" function parameter method.

We'll explore two different solutions to this problem in part 2 and 3:
- Function Objects method, and
- Classes method (using polymorphism)

"""
import something


def do_something(a, b, mode, value_on_zero_division=0):
    if mode == "divide":
        return divide(a, b, value_on_zero_division)
    elif mode == "modulo":
        return modulo(a, b)
    else:
        return something.do_something(a, b, mode)


def divide(a, b, value_on_zero_division):
    try:
        return a / b
    except ZeroDivisionError:
        return value_on_zero_division


def modulo(a, b):
    return a % b


def main():
    print(do_something(4, 2, mode="add"))  # 6
    print(do_something(4, 2, mode="divide"))  # 2.0
    print(do_something(2, 0, mode="divide", value_on_zero_division=10))  # Output: 10
    print(do_something(5, 4, mode="modulo"))  # Output: 1


if __name__ == '__main__':
    main()
