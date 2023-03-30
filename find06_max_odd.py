def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    i = 0
    n = 0

    while i < len(data):
        if data[i]%2 == 1 and data[i] > n:
            n = data[i]
        i += 1
    return n
    # return -1

print(find_max_odd([11, 7, 51, 4, 91]))