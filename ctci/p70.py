from itertools import permutations


def a1():
    count = 0
    for i in range(lb):
        w = b[i:(i + ls)]
        for p in ps:
            if p == w:
                count += 1
    return count


def a2():
    count = 0
    for i in range(lb):
        w = b[i:(i + ls)]
        if w in ps:
            count += 1
    return count


def a3():
    count = 0
    for i in range(lb):
        w = b[i:(i + ls)]
        f = True
        for c in w:
            if c not in s:
                f = False
        if f:
            if w in ps:
                count += 1
    return count


# Consider the permutation generation to be part of the algorithm.

def a1p(s, b):
    ps = [''.join(t) for t in sorted(set(permutations(s)))]
    ls = len(s)
    lb = len(b)
    count = a1()
    return count


def a2p(s, b):
    ps = [''.join(t) for t in sorted(set(permutations(s)))]
    ls = len(s)
    lb = len(b)
    count = a2()
    return count


def a4(s, b):
    count = 0
    ls = len(s)
    lb = len(b)
    for i in range(lb):
        w = set(b[i:(i + ls)])
        if set(s) == set(w):
            count += 1
    return count

if __name__ == '__main__':
    s = 'abbc'
    b = 'cbabadcbbabbcbabaabccbabc'
    r = 7

    ps = [''.join(t) for t in sorted(set(permutations(s)))]
    print(ps)
    print(len(ps))

    ls = len(s)
    lb = len(b)

    assert a1() == r
    assert a2() == r
    assert a3() == r

    assert a1p(s, b) == r
    assert a1p(s, b) == r

    print(a4(s, b))
    # assert a4(s, b) == r
