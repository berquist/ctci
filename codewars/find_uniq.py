# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python

def find_uniq(arr):
    frequencies = {i: arr.count(i) for i in arr}
    return [x for x in frequencies if frequencies[x] == 1][0]


def test_find_uniq():
    test_cases = [
        ([1, 1, 1, 2, 1, 1], 2),
        ([0, 0, 0.55, 0, 0], 0.55),
        ([3, 10, 3, 3, 3], 10),
    ]
    for arr, outcome in test_cases:
        assert find_uniq(arr) == outcome
