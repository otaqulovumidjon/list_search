def find_min_index(data):
    """
    Given the list of numbers, return the index of minimum number in the list
    args:
        data: list of numbers
    returns: index of minimum number in the list
    """
    i = 0
    m = 0
    n = data[0]

    while i < len(data):
        if data[i] <= n:
            n = data[i]
            m = data.index(n)
        i += 1
    return m

print(find_min_index([1, 2, -3, 4, -5]))