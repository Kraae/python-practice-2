def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    def multiple_letter_count(word):
     return {letter: word.count(letter) for letter in set(word)}


print(multiple_letter_count('yay'))