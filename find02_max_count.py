def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    i = 0
    n = 0
    while i < len(data):
        if data[i] > n:
            n = data[i]
        i += 1
    return data.count(n)

print(find_max_count([113, 8, 113, 4, 91])) 