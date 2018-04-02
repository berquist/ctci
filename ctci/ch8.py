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


if __name__ == '__main__':
    test_magic_index_bf()
    test_magic_index_unsorted()
    test_magic_index_sorted()
