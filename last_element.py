def last_element(lst):
    """Return last item in list (None if list is empty.

        >>> last_element([1, 2, 3])
        3

        >>> last_element([]) is None
        True
    """
#-1 is the last item in the list; 
    if lst:
        #if a list has any value then it is true 
        return lst[-1]
    return None
