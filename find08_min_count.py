def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    i = 0
    m = 0
    n = data[0]
    
    while i < len(data):
        if data[i] <= n:
            n = data[i]
            m = data.count(n)
        i += 1
    return m

print(find_min_count([0, -4, 3, 9, -4, -4]))