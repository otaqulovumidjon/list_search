def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    i = 0
    n = data[0]

    while i < len(data):
        if data[i] <= n and data[i]%2 == 0:
            n = data[i]
        i += 1
    return n

print(find_min_even([7, 8, 4, 3, 5]))