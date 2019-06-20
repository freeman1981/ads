from collections import deque


def pal_checker(s: str) -> bool:
    """
    >>> pal_checker('123')
    False
    >>> pal_checker('121')
    True
    """
    dq = deque(s)
    while len(dq) > 1:
        if dq.pop() != dq.popleft():
            return False
    return True


def pal_checker2(s: str) -> bool:
    """
    >>> pal_checker2('123')
    False
    >>> pal_checker2('121')
    True
    """
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True
