def magic_index_sorted(arr, bot=None, top=None):
    if bot is None:
        bot = 0
    if top is None:
        top = len(arr)
    mid = (top + bot) // 2
    ret = -1
    if arr[mid] == mid:
        ret = mid
    else:
        ret_left = magic_index_sorted(arr, bot, mid - 1)
        ret_right = magic_index_sorted(arr, mid + 1, top)
        if ret_left != -1:
            return ret_left
        if ret_right != -1:
            return ret_right
    return ret


def test_magic_index_sorted():
    tests = [
        ([1, 2, 3, 3], 3),
    ]
    for arr, outcome in tests:
        assert magic_index_sorted(arr) == outcome
    return True


if __name__ == '__main__':
    test_magic_index_sorted()
