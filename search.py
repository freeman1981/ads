def bin_search(alist, item):
    """
    >>> bin_search([1, 2, 3], 2)
    1
    >>> bin_search([1, 2, 3], 4)
    Traceback (most recent call last):
        ...
    ValueError: item not found
    """
    if not alist:
        raise ValueError('item not found')
    half_ind = len(alist) // 2
    half = alist[half_ind]
    if half == item:
        return half_ind
    elif half < item:
        return bin_search(alist[item + 1:], item)
    else:  # alist[half] > item:
        return bin_search(alist[:item], item)
