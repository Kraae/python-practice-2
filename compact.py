def compact(list):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    falsey = [None, False, 0, '', {}, []]
    truthy = [val for val in list if val not in falsey]
    return truthy