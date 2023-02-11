"""
This file, along with handle_input.py demonstrates using function objects to allow
users of a function to customise the behaviour of that function.

Firstly, try running this file to get a feel for how it works.

Now let's take a closer look:

You can see below in main() that we call the function handle_user_input() (from handle_input.py).
Now would be a good time to look at handle_input.py.

You'll notice that for the on_integer_input parameter we pass in our function handle_integer_input()
and for the on_string_input we pass in handle_string_input().

To help understand how flexible this can be, try the following exercise:

    Write a new function to be used in the on_integer_input parameter of handle_user_input().
    Like handle_integer_input it should have one parameter: the number the user entered (an integer).
    Call it "my_integer_handler" and make it print the number,
    then return True if the number is greater than 0.

    Modify the code inside main() so that it uses your function instead of handle_integer_input().

    Run this file.
    Try entering the number 1. It should ask for another number.
    Next, enter 0. It should exit.

See how the behaviour of handle_user_input() can be customised in a variety of ways.

Now that you've seen an example there's one final exercise to practice using customisable
functions. Proceed to colour_selection.py.
"""

# from handle_input import handle_user_input
#
#
# def handle_integer_input(number):
#     """Display the square of the number given.
#     Returns True to indicate that we should keep asking for input."""
#     print(f"You entered the number {number}")
#     print(f"The square of number is {number ** 2}")
#     return True
#
#
# def handle_string_input(string):
#     """Display the length of the string given.
#     If the string is 'exit', return False to indicate we should stop asking for input.
#     Otherwise, return True."""
#     if string == "exit":
#         return False
#
#     print(f"You entered the string {string}")
#     print(f"The length of string is {len(string)}")
#     return True
#
#
# def main():
#     handle_user_input(
#         message="Enter a number or a string ('exit' to stop):",
#         on_integer_input=handle_integer_input,  # Notice we don't use ()
#         on_string_input=handle_string_input)  # Notice we don't use ()
#
#
# if __name__ == '__main__':
#     main()

from handle_input import handle_user_input


# def handle_integer_input(number):
#     """Display the square of the number given.
#     Returns True to indicate that we should keep asking for input."""
#     print(f"You entered the number {number}")
#     print(f"The square of number is {number ** 2}")
#     return True


def my_integer_handler(number):
    """Display the number entered.
    Returns True (only if number is greater than 0) to indicate that we should keep asking for input."""
    print(f"You entered the number {number}")
    return number > 0


def handle_string_input(string):
    """Display the length of the string given.
    If the string is 'exit', return False to indicate we should stop asking for input.
    Otherwise, return True."""
    if string == "exit":
        return False

    print(f"You entered the string {string}")
    print(f"The length of string is {len(string)}")
    return True


def main():
    handle_user_input(
        message="Enter a number or a string ('exit' to stop):",
        on_integer_input=my_integer_handler,  # Notice we don't use ()
        on_string_input=handle_string_input)  # Notice we don't use ()


if __name__ == '__main__':
    main()
