def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    i = 0
    n = data[0]

    while i < len(data):
        if data[i] <= n and data[i]%2 == 1:
            n = data[i]
        i += 1
    return n

print(find_min_odd([7, 8, 4, 3, 5]))