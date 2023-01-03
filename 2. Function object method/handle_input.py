"""
handle_user_input() handles user input and allows custom behaviour based on the input given.
Review the code and comments below to see how it works.
Note in the docstring below that parameters are described using the standard Python format:

    :param parameter_name: Description of parameter.

"""


def handle_user_input(message, on_integer_input, on_string_input):
    """
    Get input from the user. The input is handled with custom functions
    that are called based on the type of input entered.

    :param message: Message to display when asking for user input.
    :param on_integer_input: If the user enters a valid integer this function is called.
    The function should accept one parameter of type int and
    return True if we should keep asking for more input.
    :param on_string_input: If the user enters anything other than an integer this function is called.
    The function should accept one parameter of type string and
    return True if we should keep asking for more input.
    """
    ask_for_input = True
    while ask_for_input:
        print(message)
        user_input = input(">>>")
        try:
            user_input = int(user_input)  # Attempt to convert input to integer.
            ask_for_input = on_integer_input(user_input)
        except ValueError:
            ask_for_input = on_string_input(user_input)
