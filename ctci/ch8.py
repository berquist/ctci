from math import factorial


## 8.1

def nperm(x, y, z):
    n = factorial(x + y + z)
    d = factorial(x) * factorial(y) * factorial(z)
    return int(n / d)


def test_nperm():
    tests = [
        [(0, 0, 2), 1],
        [(1, 1, 1), 6],
        [(3, 0, 1), 4],
        [(0, 3, 0), 1],
        [(2, 2, 0), 6],
        [(4, 1, 0), 5],
    ]
    for test, outcome in tests:
        assert nperm(*test) == outcome
    return True


def triple_step(n):
    """8.1, iterative

    A child is running up a staircase with n steps and can hop either
    1 step, 2 steps, or 3 steps at a time. Implement a method to count
    how many possible ways the child can run up the stairs.

    Strategy: find all nonnegative solutions {x, y, z} for x + 2y + 3z
    = n. It is done top down, as it is easiest for n to dictate the
    largest possible value of z rather than starting from x.

    There may be permutations within each solution; count those too.
    """
    if n < 1:
        return 0
    counter = 0
    max_z = n // 3
    for z in range(max_z, -1, -1):
        rz = n - (3 * z)
        for y in range(rz, -1, -1):
            x = rz - (2 * y)
            # only roots where all 3 coefficients are geq 0 are
            # admissable
            if x >= 0:
                val = int(x + (2 * y) + (3 * z))
                assert val == n
                counter += nperm(x, y, z)
    return counter


def test_triple_step():
    assert triple_step(5) == 13
    assert triple_step(10) == 274
    nsteps = list(range(11))
    rets = [triple_step(n) for n in nsteps]
    refs = [0, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274]
    assert rets == refs
    return True

## 8.3

def magic_index_bf(arr):
    """8.3, brute force"""
    for i in range(len(arr)):
        if arr[i] == i:
            return i


def magic_index_unsorted(arr, bot=None, top=None):
    if bot is None:
        bot = 0
    if top is None:
        top = len(arr) - 1
    if bot > top:
        return None
    mid = (top + bot) // 2
    if arr[mid] == mid:
        return mid
    ret_left = magic_index_unsorted(arr, bot, mid - 1)
    ret_right = magic_index_unsorted(arr, mid + 1, top)
    if ret_left is not None:
        return ret_left
    if ret_right is not None:
        return ret_right


def magic_index_sorted(arr, bot=None, top=None):
    if bot is None:
        bot = 0
    if top is None:
        top = len(arr) - 1
    if bot > top:
        return None
    mid = (top + bot) // 2
    if mid > arr[mid]: # right
        return magic_index_sorted(arr, mid + 1, top)
    if mid < arr[mid]: # left
        return magic_index_sorted(arr, bot, mid - 1)
    return mid


def magic_index_sorted_nonunique(arr, bot=None, top=None):
    if bot is None:
        bot = 0
    if top is None:
        top = len(arr) - 1
    if bot > top:
        return None
    mid = (top + bot) // 2
    if arr[mid] == mid:
        return mid
    lindex = min(mid - 1, arr[mid])
    lret = magic_index_sorted_nonunique(arr, bot, lindex)
    if lret:
        return lret
    rindex = max(mid + 1, arr[mid])
    rret = magic_index_sorted_nonunique(arr, rindex, top)
    return rret


def test_magic_index_bf():
    tests = [
        ([1, 2, 3, 3], 3),
        ([1, 2, 3, 4, 5, 6, 10, 20, 8, 9], 8),
        ([-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13], 7),
    ]
    for arr, outcome in tests:
        assert magic_index_bf(arr) == outcome
    return True


def test_magic_index_unsorted():
    tests = [
        ([1, 2, 3, 3], 3),
        ([1, 2, 3, 4, 5, 6, 10, 20, 8, 9], 8),
    ]
    for arr, outcome in tests:
        assert magic_index_unsorted(arr) == outcome
    return True


def test_magic_index_sorted():
    tests = [
        ([-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13], 7),
    ]
    for arr, outcome in tests:
        assert magic_index_sorted(arr) == outcome
    return True


def test_magic_index_sorted_nonunique():
    tests = [
        ([-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13], 2),
    ]
    for arr, outcome in tests:
        assert magic_index_sorted_nonunique(arr) == outcome
    return True


if __name__ == '__main__':
    test_magic_index_bf()
    test_magic_index_unsorted()
    test_magic_index_sorted()
    test_magic_index_sorted_nonunique()
