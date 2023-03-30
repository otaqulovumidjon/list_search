def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    i = 0
    n = 0
    
    while i < len(data):
        if data[i]%2 == 0 and data[i] > n:
            n = data[i]
        i += 1
    return n

print(find_max_even([7, 6, 3, 4, 9]))
