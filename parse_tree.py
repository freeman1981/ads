from datastructures.tree import BinaryTree


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
assert 1
