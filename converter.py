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


digits = '0123456789ABCDEF'


def divide_v2(dec_number: int, base: int) -> str:
    """
    >>> divide_v2(3, 2)
    '11'
    >>> divide_v2(10, 16)
    'A'
    """
    if base > dec_number:
        return digits[dec_number]
    return f'{divide_v2(dec_number // base, base)}{digits[dec_number % base]}'


def hanoy(depth, from_, to, with_):
    pass
