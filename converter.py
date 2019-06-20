def divide_by2(dec_number: int):
    """
    >>> divide_by2(3)
    '11'
    """
    remstack = []

    while dec_number > 0:
        remstack.append(dec_number % 2)
        dec_number //= 2

    return ''.join(map(str, remstack[::-1]))

