def multiply_even_numbers(list):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    total = 1
    even_only = [num for num in list if num % 2 == 0]
    for num in even_only:
        total *= num
        #dict = {num: num if list[num] % 2 == 0 for num in list}
    return total

print(multiply_even_numbers([2, 3, 4, 5, 6]))