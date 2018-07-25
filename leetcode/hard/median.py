def median(l):
    is_even = (len(l) % 2) == 0
    i = len(l) // 2
    if not is_even:
        return l[i]
    else:
        return (l[i - 1] + l[i]) / 2
