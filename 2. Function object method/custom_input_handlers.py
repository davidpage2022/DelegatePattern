"""
This file, along with handle_input.py demonstrate using function objects to allow
users to customise the behaviour of a function.

Firstly, try running this file to get a feel for how it works.

Now let's look a closer look:

- You can see below in main() that we call the function handle_user_input().

  The first parameter is the message to display to the user.

  The second parameter is the function that will be called when the user enters an integer.
  In this case we use our handle_integer_input() function.

  The third parameter is the function that will be called when the user enters anything other
  than an integer. We pass in our handle_string_input() function.

- The result of calling the function is that the user is asked for input.

  If the input is an integer handle_integer_input() gets called with the number that the
  user entered. Note that number is an integer.
  Our function displays the square of the integer and then
  returns true to indicate that we should keep asking for more input.

  If the input is anything else, handle_string_input() gets called with whatever string
  the user entered.
  This time our function checks if the user entered "exit". If they did we return
  False to indicate that we should stop asking for more input.
  Otherwise, we return the length of the string entered.

To help understand how flexible this can be, try the following exercise:

    Write a new function to be used in the on_integer_input parameter of handle_user_input().
    Like handle_integer_input it should have one parameter representing the number the user entered.
    Call it "my_integer_handler" and make it print the number and then
    return True if the number is greater than 0.

    Modify the code inside main() so that it uses your function instead of handle_integer_input().

    Run this file.
    Try entering the number 1. It should ask for another number.
    Then try entering 0. It should exit.

See how the function behaviour can be customised to do whatever you want it to.

Now let's finish off by having a look at handle_user_input(). Go to handle_input.py.
"""

from handle_input import handle_user_input


def handle_integer_input(number):
    """Display the square of the number given.
    Returns True to indicate that we should keep asking for input."""
    print(f"You entered the number {number}")
    print(f"The square of number is {number ** 2}")
    return True


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
        on_integer_input=handle_integer_input,  # Notice we don't use ()
        on_string_input=handle_string_input)  # Notice we don't use ()


if __name__ == '__main__':
    main()
