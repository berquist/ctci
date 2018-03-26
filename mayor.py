"""
N (>= 2) people

Elect a mayor

A mayor is someone who knows no other people, but everyone else knows

function knows(i, j) -> boolean

1. N >= 2
2. no mayor needs to exist
3. everyone else is the (N-1) others
4. 0 or 1 total mayors
5. if A knows B, A cannot be mayor
6. if A does not know B, B cannot be mayor
7. O(n)

14
0,1
12,11
"""


def mayor(pairs, n):
    print('-' * 70)
    left = set([pair[0] for pair in pairs])
    right = set([pair[1] for pair in pairs])
    people = set(range(n))
    candidates = people.copy()
    print(n, candidates)
    candidates = people.difference(left)
    _candidates = candidates.copy()
    print(candidates)
    for candidate in candidates:
        everyone_else = people.copy()
        everyone_else.discard(candidate)
        # if everyone_else != left:
        #     candidates.discard(candidate)
        for person in everyone_else:
            if (person, candidate) not in pairs:
                _candidates.discard(candidate)
                break
    print(_candidates)
    return _candidates


def test_mayor():
    pairs = [
        (0, 1),
    ]
    assert list(mayor(pairs, 2)) == [1]
    pairs = [
        (0, 1),
        (1, 0),
    ]
    assert list(mayor(pairs, 2)) == []
    pairs = [
        (0, 1),
        (0, 2),
    ]
    assert list(mayor(pairs, 3)) == []
    pairs = [
        (0, 1),
        (2, 1),
    ]
    assert list(mayor(pairs, 3)) == [1]
    pairs = [
        (0, 2),
        (1, 2),
    ]
    assert list(mayor(pairs, 3)) == [2]
    pairs = [
        (0, 2),
        (1, 2),
        (2, 1),
    ]
    assert list(mayor(pairs, 3)) == []
    pairs = [
        (0, 1),
        (2, 0),
    ]
    assert list(mayor(pairs, 3)) == []
    return

if __name__ == '__main__':
    test_mayor()
