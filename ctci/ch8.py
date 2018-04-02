def magic_index_sorted(arr, bot=None, top=None):
    if bot is None:
        bot = 0
    if top is None:
        top = len(arr) - 1
    if bot > top:
        return None
    mid = (top + bot) // 2
    if arr[mid] == mid:
        return mid
    ret_left = magic_index_sorted(arr, bot, mid - 1)
    ret_right = magic_index_sorted(arr, mid + 1, top)
    if ret_left is not None:
        return ret_left
    if ret_right is not None:
        return ret_right


def test_magic_index_sorted():
    tests = [
        ([1, 2, 3, 3], 3),
        ([1, 2, 3, 4, 5, 6, 10, 20, 8, 9], 8),
    ]
    for arr, outcome in tests:
        assert magic_index_sorted(arr) == outcome
    return True


if __name__ == '__main__':
    test_magic_index_sorted()
