def capitalize(string):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

       # there's a built-in method for this!
    return string.capitalize()

    # or, doing it by hand:
    # return phrase[:1].upper() + phrase[1:]

    return string[0].upper() + string[1:]
    #return string.capitalize()

print(capitalize('python'))