VOWELS = set("aeiou")


def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!')
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    phrase = phrase.lower()
    #keeps the running count of vowels in the string
    counter = {}

    for chr in phrase:
        if chr in VOWELS:
            counter[chr] = counter.get(chr, 0) + 1

    return counter




    