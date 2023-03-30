def find_min(data):
    """
    Given the list of numbers, return the minimum number in the list
    args:
        data: list of numbers
    returns: minimum number in the list
    """
    i = 0
    n = data[0]
    
    while i < len(data):
        if data[i] <= n:
            n = data[i]
        i += 1
    return n
# print(find_min([1, 2, 3, 4, 5]))
print(find_min([12, 34, 6, 23, 76, 45]))