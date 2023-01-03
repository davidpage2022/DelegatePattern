"""
handle_user_input() handles user input and allows custom behaviour based on the input given.
Review the code and comments below to see how it works.
Note in the docstring below that parameters are described using the standard Python format:

    :param parameter_name: Description of parameter.

Now that you've seen an example there's one final exercise to practice using customisable
functions. Proceed to colour_selection.py.
"""

def handle_user_input(message, on_integer_input=None, on_string_input=None):
    """
    Get input from the user. The input is handled with optional custom functions
    that are called based on the type of input entered.

    :param message: Message to display when asking for user input.
    :param on_integer_input: If the user enters a valid integer this function is called.
    If the function is None nothing happens.
    The function should accept one parameter of type int and
    return True if we should keep asking for more input.
    :param on_string_input: If the user enters anything other than an integer this function is called.
    The function should accept one parameter of type string and
    return True if we should keep asking for more input.
    If the function is None nothing happens.
    """
    get_more_input = True
    while get_more_input:
        print(message)
        user_input = input(">>>")
        try:
            # Attempt to convert input to integer.
            user_input = int(user_input)

            # Call the integer handling function given if it is not None.
            if on_integer_input:
                get_more_input = on_integer_input(user_input)
            else:
                get_more_input = False

        except ValueError:
            # Call the string handling function given if it is not None.
            if on_string_input:
                get_more_input = on_string_input(user_input)
            else:
                get_more_input = False


if __name__ == '__main__':
    handle_user_input("Enter a number or a string...")  # Test with no input handling functions.
