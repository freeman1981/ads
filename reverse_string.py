from datastructures.stack import Stack


def revert(s: str):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    res = []
    while not stack.isEmpty():
        res.append(stack.pop())

    return ''.join(res)


string = input('enter string:')

print(revert(string))
print(string[::-1])  # pythonick
