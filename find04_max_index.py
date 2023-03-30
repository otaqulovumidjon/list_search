def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    i = 0
    n = 0
    s = 0

    while i < len(data):
        if data[i] > n:
            n = data[i]
            s = i
        i += 1
    return s

print(find_max_index([6, 8, 7, 4, 0]))
