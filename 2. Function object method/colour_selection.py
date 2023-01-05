"""
In this final exercise we practice using the display_word_colour() function,
which allows us to customise how it behaves.

Create a function that takes in a word and returns the string "red" if
the first letter of the word is lowercase. Otherwise, return "green".
I recommend "select_colour" as a good name for the function.

Next, modify the arguments passed into the display_word_colour functions in main()
so that the output is:

    red
    green

Do not modify display_word_colour in any way.

That's the end of part 2. The part 3 will try to achieve the same goal of
customising the behaviour of a function, but by using classes instead of function objects.
Classes are more complex than function objects, but they allow greater flexibility
in customising and extending behaviour.
"""


# def display_word_colour(word, colour_selector=None):
#     if not colour_selector:
#         print("Error: No colour_selector given")
#         return
#
#     colour = colour_selector(word)
#     print(colour)
#
#
# def main():
#     display_word_colour("lowercase")  # Output should be: red
#     display_word_colour("UPPERCASE")  # Output should be: green
#
#
# if __name__ == '__main__':
#     main()


def select_colour(word):
    """Return a colour dependent on the first character of the word."""
    if word[0].islower():
        return "red"
    else:
        return "green"


def display_word_colour(word, colour_selector=None):
    if not colour_selector:
        print("Error: No colour_selector given")
        return

    colour = colour_selector(word)
    print(colour)


def main():
    display_word_colour("lowercase", select_colour)  # Output should be: red
    display_word_colour("UPPERCASE", select_colour)  # Output should be: green


if __name__ == '__main__':
    main()
