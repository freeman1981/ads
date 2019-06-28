def sort(lst):
    if len(lst) < 2:
        return lst

    p = lst[0]
    less = [x for x in lst[1:] if x > p]
    greater = [x for x in lst[1:] if x <= p]
    a = sort(less)
    b = sort(greater)
    ret = a + [p] + b
    return ret


list_ = [3, 5, 1, 7]
print(sort(list_))
