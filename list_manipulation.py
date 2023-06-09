def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """

    if command == "remove" and location == "end":
        return list.pop()
    elif command == "remove" and location == "beginning":
        return list.pop(0)
    elif command == "add" and location == "end":
        list.append(value)
        return list
    elif command == "add" and location == "beginning":
        list.insert(0, value)
        return list
    else:
        return "Oops, something went wrong"


sample_list = [1, 2, 4, 'gaylon', True]
sample_list2 = ['red', 'blue', 3, 11.1, True]
print(list_manipulation(sample_list, "add", "beginning", "ashley"))
print(list_manipulation([1, 2, 3, 4], "add", "end", "aaron"))
print(list_manipulation(sample_list2, "remove", "beginning"))  # 'red'
