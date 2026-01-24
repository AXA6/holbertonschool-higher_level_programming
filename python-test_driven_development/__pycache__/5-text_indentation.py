#!/usr/bin/python3
"""
5-text_indentation module.

This module provides a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters:
    '.', '?' and ':'.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Remove leading and trailing spaces
    text = text.strip()

    # Build the formatted output
    output = ""
    for char in text:
        output += char
        if char in ".?:":
            output += "\n\n"

    # Remove spaces after new lines
    lines = [line.strip() for line in output.split("\n")]
    formatted_text = "\n".join(lines)

    print(formatted_text, end="")
