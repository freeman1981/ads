from datastructures.tree import BinaryTree
import operator


def build_parse_tree(exp: str) -> BinaryTree:
    fplist = exp.split()
    e_tree = BinaryTree('')
    p_stack = [e_tree]
    current_tree = e_tree

    for i in fplist:
        if i == '(':
            current_tree.insert_left('')
            p_stack.append(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in ['+', '-', '*', '/', ')']:
            current_tree.set_root_val(int(i))
            current_tree = p_stack.pop()
        elif i in ['+', '-', '*', '/']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            p_stack.append(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError

    return e_tree


pt = build_parse_tree("( ( 10 + 5 ) * 3 )")


def evaluate(parse_tree: BinaryTree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    left_ch = parse_tree.get_left_child()
    right_ch = parse_tree.get_right_child()

    if left_ch and right_ch:
        fn = opers[parse_tree.get_root_val()]
        return fn(evaluate(left_ch), evaluate(right_ch))
    else:
        return parse_tree.get_root_val()


# ret = evaluate(pt)
# assert 1


def preorder(tree: BinaryTree):
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


def postorder(tree: BinaryTree):
    if tree:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val())


def inorder(tree: BinaryTree):
    if tree:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())


preorder(pt)

print('*' * 33)

postorder(pt)

print('*' * 33)

inorder(pt)

