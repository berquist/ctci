def median(lst):
    is_even = (len(lst) % 2) == 0
    i = len(lst) // 2
    if not is_even:
        return lst[i]
    else:
        return (lst[i - 1] + lst[i]) / 2
