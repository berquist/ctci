# Problem 1
#
# Given an unsorted array of integers, how many pairs exist that can
# sum to zero?
#
# no duplicates, can include zero

def sum_to_zero(l):
    positive = set()
    negative = set()
    for i in l:
        if i < 0:
            negative.add(i)
        else:
            positive.add(i)

    num_pairs = 0
    for i in negative:
        if -i in positive:
            num_pairs += 1
    return num_pairs

def test_sum_to_zero():
    assert sum_to_zero([0, 1, 2, 3, 4, 5]) == 0
    assert sum_to_zero([-2, 20, -1, 1, 2]) == 2
    return True

# Problem 2
#
# Old Content below(Plain Text):
#
# assume infinite coins
#
# change = [npennies, nnickels, ndimes, nquarters]
# divide int total_change (0 to 99) into change
# example 77 -> [2, 0, 0, 3]
#
# Change = namedtuple('Change', ['npennies', 'nnickels', 'ndimes', 'nquarters'])
#
# change = Change(2, 0, 0, 3)
# change.npennies returns 2

from collections import namedtuple
Change = namedtuple('Change', ['npennies', 'nnickels', 'ndimes', 'nquarters'])
def change_to_coins(change):
    npennies = 0
    nnickels = 0
    ndimes = 0
    nquarters = 0

    nquarters = change // 25
    change = change % 25

    ndimes = change // 10
    change = change % 10

    nnickels = change // 5
    change = change % 5

    npennies = change

    return Change(npennies, nnickels, ndimes, nquarters)


def test_change_to_coins():
    assert change_to_coins(77) == Change(2, 0, 0, 3)
    return True


if __name__ == '__main__':
    test_change_to_coins()
