def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    i = 0
    n = 0
    s = 0
    m = 0

    while i < len(data):
        if data[i] > n:
            n = data[i]
        i += 1

    while s < len(data):
        if data[s] < n:
            m = data[s]
        s += 1
        return m + n

print(find_max_min_sum([1, 2, 3, 4, 5]))