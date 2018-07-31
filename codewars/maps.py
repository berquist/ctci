# http://www.codewars.com/kata/beginner-lost-without-a-map/train/python

def maps(a):
    return list(map(lambda x: 2 * x, a))


def test_maps():
    test_cases = [
        ([1, 2, 3], [2, 4, 6]),
        ([], []),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]),
    ]
    for a, outcome in test_cases:
        assert maps(a) == outcome
