def bubble_sort(lst):
    for pass_num in range(len(lst)):
        for i in range(len(lst) - 1):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]


def bubble_sort2(lst):
    len_ = len(lst)
    for _ in range(len_):
        flip = False
        for i in range(len_ - 1):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                flip = True
        if not flip:
            return


def select_sort(lst):
    len_ = len(lst)

    for i in range(len_):
        min_pos = 0
        j = 0
        for j in range(len_ - i):
            if lst[min_pos] > lst[j]:
                min_pos = j
        lst[min_pos], lst[j] = lst[j], lst[min_pos]


def insertion_sort(lst):
    for index in range(1, len(lst)):

        current_val = lst[index]
        position = index

        while position > 0 and lst[position - 1] < current_val:
            lst[position] = lst[position - 1]
            position -= 1

        lst[position] = current_val


def merge_sort(lst):

    if len(lst) <= 1:
        return

    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    i = 0
    j = 0
    k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] > right_half[j]:
            lst[k] = left_half[i]
            i = i + 1
        else:
            lst[k] = right_half[j]
            j = j + 1
        k = k + 1

    while i < len(left_half):
        lst[k] = left_half[i]
        i = i + 1
        k = k + 1

    while j < len(right_half):
        lst[k] = right_half[j]
        j = j + 1
        k = k + 1


list_ = [3, 5, 1, 7]
merge_sort(list_)
print(list_)
