def bubble_sort(lst):
    for pass_num in range(len(lst)):
        for i in range(pass_num):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]


def bubble_sort2(lst):
    for pass_num in range(len(lst)):
        for i in range(pass_num):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]


list_ = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(list_)
print(list_)
