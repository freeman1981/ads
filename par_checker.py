from datastructures.stack import Stack


def simple_checker(s: str):
    """
    >>> simple_checker('()')
    True
    >>> simple_checker(')(')
    False
    >>> simple_checker('(foo)(bar)')
    True
    """
    open_par = 0
    for ch in s:
        if open_par < 0:
            return False
        elif ch == '(':
            open_par += 1
        elif ch == ')':
            open_par -= 1
    return open_par == 0


OPENS = "([{"
CLOSERS = ")]}"


def par_checker(in_str: str):
    """
    >>> par_checker('()')
    True
    >>> par_checker(')(')
    False
    >>> par_checker('()()')
    True
    >>> par_checker('({})')
    True
    """
    s = Stack()
    balanced = True
    index = 0
    while index < len(in_str) and balanced:
        symbol = in_str[index]
        if symbol in OPENS:
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if OPENS.index(top) != CLOSERS.index(symbol):
                    balanced = False
        index += 1
    return balanced and s.isEmpty()


def par_checker2(in_str: str):
    """
    >>> par_checker2('()')
    True
    >>> par_checker2(')(')
    False
    >>> par_checker2('(foo)(bar)')
    True
    >>> par_checker2('({})')
    True
    """
    stack = []
    for symbol in in_str:
        if symbol in OPENS:
            stack.append(symbol)
        elif symbol in CLOSERS:
            if stack:
                top = stack.pop()
                if OPENS.index(top) != CLOSERS.index(symbol):
                    return False
            else:
                return False
    return not stack
