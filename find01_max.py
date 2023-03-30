def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    i = 0
    n = 0
    while i < len(data):
        if data[i] > n:
            n = data[i]
        i += 1
    return n

print(find_max([1, 2, 3, 4, 5])) 