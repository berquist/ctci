import sys

import numpy as np

np.set_printoptions(linewidth=200)


def make_frequencies(s):
    frequencies = dict()
    for c in s:
        if c not in frequencies:
            frequencies[c] = 1
        else:
            frequencies[c] += 1
    return frequencies


def ch1_1_1(s):
    ss = set(s)
    if len(ss) < len(s):
        return False
    return True


def ch1_1_2(s):
    ss = set()
    for c in s:
        if c not in ss:
            ss.add(c)
        else:
            return False
    return True


def ch1_1_3(s):
    if len(s) == 1:
        return True
    ss = sorted(s)
    for i in range(1, len(ss)):
        if ss[i] == ss[i - 1]:
            return False
    return True


def ch1_1_4(s):
    """This is a direct translation from the answer on page 193."""
    checker = 0
    ls = len(s)
    for i in range(ls):
        val = int.from_bytes(s[i].encode('ascii'), sys.byteorder)
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val)
    return True


def ch1_2_1(s1, s2):
    if len(s1) != len(s2):
        return False
    ss1 = sorted(s1)
    ss2 = sorted(s2)
    if ss1 != ss2:
        return False
    return True


def ch1_2_2(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

def ch1_2_3(s1, s2):
    """there is also a solution that uses a hash table to store frequencies"""
    f1 = make_frequencies(s1)
    f2 = make_frequencies(s2)
    # first check keys
    if set(f1.keys()).difference(set(f2.keys())):
        return False
    # then check counts
    for k in f1:
        if f1[k] != f2[k]:
            return False
    return True


def ch1_2_4(s1, s2):
    f1 = make_frequencies(s1)
    f2 = make_frequencies(s2)
    return f1 == f2


def ch1_3_1(s):
    """This is almost certainly not what they're looking for."""
    return s.rstrip().replace(' ', '%20')


def ch1_4_1(s):
    # forgot this...
    s = s.lower().replace(' ', '')
    frequencies = dict()
    for c in s:
        if c not in frequencies:
            frequencies[c] = 1
        else:
            frequencies[c] += 1
        if frequencies[c] > 2:
            return False
    values = frequencies.values()
    # c1 = values.count(1)
    c1 = list(values).count(1)
    if c1 > 1:
        return False
    # c2 = values.count(2)
    c2 = list(values).count(2)
    # if (c1 + c2) != len(s):
    if (c1 + 2 * c2) != len(s):
        return False
    return True

# 1. forgot to lower case and remove spaces
# 2. dict_values doesn't have a count method
# 3. forgot that characters with frequency 2 count twice to length

# does this run in O(N) time?
# use a bit vector?

# The above solution is wrong because no character can appear more
# than twice, with a "middle" character that can appear only once. It
# should really be that no character can appear more than an even
# number of times, with a "middle" characted that can appear an even +
# 1 (odd) number of times.

def ch1_4_2(s):
    s = s.lower().replace(' ', '')
    frequencies = make_frequencies(s)
    check_odd = lambda x: (x % 2) != 0
    count_odd = [check_odd(count) for count in frequencies.values()]
    if sum(count_odd) > 1:
        return False
    return True


def ch1_4_3(s):
    s = s.lower().replace(' ', '')
    def toggle(bit_vector, index):
        if index < 0:
            return bit_vector
        mask = 1 << index
        if not (bit_vector & mask):
            bit_vector |= mask
        else:
            bit_vector &= ~mask
        return bit_vector
    def create_bit_vector(s):
        bit_vector = 0
        for c in s:
            val = int.from_bytes(c.encode('ascii'), sys.byteorder)
            bit_vector = toggle(bit_vector, val)
        return bit_vector
    def check_exactly_one_bit_set(bit_vector):
        return not (bit_vector & (bit_vector - 1))
    def is_permutation_of_palindrome(s):
        bit_vector = create_bit_vector(s)
        return (bit_vector == 0) or check_exactly_one_bit_set(bit_vector)
    return is_permutation_of_palindrome(s)


def ch1_5_1(s1, s2):
    l1, l2 = len(s1), len(s2)
    if abs(l1 - l2) > 1:
        return False
    if s1 == s2:
        return True
    # index = 0
    index = -1
    # removal
    if l2 == (l1 - 1):
        # for i in range(l1):
        for i in range(l2):
            if s1[i] != s2[i]:
                index = i
                break
        sr1 = s1[index + 1:]
        sr2 = s2[index:]
        if index == -1:
            return True
        if sr1 != sr2:
            return False
        return True
    # insertion
    elif l2 == (l1 + 1):
        # for i in range(l2):
        for i in range(l1):
            if s1[i] != s2[i]:
                index = i
                break
        sr1 = s1[index:]
        sr2 = s2[index + 1:]
        if index == -1:
            return True
        if sr1 != sr2:
            return False
        return True
    # replacement
    else:
        for i in range(l1):
            if s1[i] != s2[i]:
                index = i
                break
        # sr1 = s1[index:]
        # sr2 = s2[index:]
        sr1 = s1[index + 1:]
        sr2 = s2[index + 1:]
        if index == -1:
            return True
        if sr1 != sr2:
            return False
        return True


def ch1_5_2(s1, s2):
    l1, l2 = len(s1), len(s2)
    if abs(l1 - l2) > 1:
        return False
    if s1 == s2:
        return True
    index = -1
    if l2 == (l1 - 1):
        lr, il1, il2 = l2, 1, 0
    elif l2 == (l1 + 1):
        lr, il1, il2 = l1, 0, 1
    else:
        lr, il1, il2 = l1, 1, 1
    for i in range(lr):
        if s1[i] != s2[i]:
            index = i
            break
    if index == -1:
        return True
    sr1 = s1[index + il1:]
    sr2 = s2[index + il2:]
    if sr1 != sr2:
        return False
    return True


def ch1_5_3(first, second):
    """This is the solution from the answer key."""
    if abs(len(first) - len(second)) > 1:
        return False
    # get shorter and longer string
    s1 = first if len(first) < len(second) else second
    s2 = second if len(first) < len(second) else first
    i1, i2 = 0, 0
    found_diff = False
    while (i1 < len(s1)) and (i2 < len(s2)):
        if s1[i1] != s2[i2]:
            if found_diff:
                return False
            found_diff = True
            if len(s1) == len(s2):
                i1 += 1
        else:
            i1 += 1
        i2 += 1
    return True


def ch1_6_1(s):
    ls = len(s)
    if ls == 1:
        return s
    pairs, count, curr, prev = [], 1, '', ''
    for i in range(1, ls):
        curr = s[i]
        prev = s[i - 1]
        if prev != curr:
            pairs.append((prev, count))
            count = 0
        count += 1
    pairs.append((curr, count))
    ns = ''.join(['{}{}'.format(c, str(count)) for (c, count) in pairs])
    if len(ns) > ls:
        return s
    return ns


def ch1_7_1(mat):
    nr, nc = mat.shape
    assert nr == nc
    for i in range(nr):
        for j in range(i):
            # Pythonic way
            mat[i, j], mat[j, i] = mat[j, i], mat[i, j]
            # non-Pythonic way
            # eij = mat[i][j]
            # mat[i][j] = mat[j][i]
            # mat[j][i] = eij
    return


# I don't understand this question, apparently. But as far as I can
# tell, it would _never_ be done this way.

# def ch1_7_2():
#     nr, nc = mat.shape
#     assert nr == nc

#     return


def find_zero_indices(mat, thresh=1.0e-15):
    nr, nc = mat.shape
    zero_index_pairs = []
    for i in range(nr):
        for j in range(nc):
            if abs(mat[i, j]) < thresh:
                zero_index_pairs.append((i, j))
    return zero_index_pairs


def ch1_8_1(mat):
    """zero_matrix"""
    nr, nc = mat.shape
    zero_index_pairs = find_zero_indices(mat)
    zrows = set([pair[0] for pair in zero_index_pairs])
    zcols = set([pair[1] for pair in zero_index_pairs])
    for ir in zrows:
        for ic in range(nc):
            mat[ir, ic] = 0
    for ic in zcols:
        for ir in range(nr):
            mat[ir, ic] = 0
    return


# def ch1_8_2(mat):

#     return


def ch1_9_1(parent, rotated):
    """string_rotation"""
    doubled = rotated + rotated
    index = doubled.find(parent)
    if index > -1:
        return True
    return False


def test_1_1():
    s1 = 'abcddaasdfh'
    s2 = 'abcdefgh'
    assert not ch1_1_1(s1)
    assert not ch1_1_2(s1)
    assert not ch1_1_3(s1)
    assert not ch1_1_4(s1)
    assert ch1_1_1(s2)
    assert ch1_1_2(s2)
    assert ch1_1_3(s2)
    assert ch1_1_4(s2)


def test_1_2():
    s1 = 'abcddaasdfh'
    s2 = 'abcdefgh'
    s3 = 'abcddassdfh'
    assert not ch1_2_1(s1, s2)
    assert ch1_2_1(s1, s1)
    assert ch1_2_1(s2, s2[::-1])
    assert not ch1_2_1(s1, s3)

    assert not ch1_2_2(s1, s2)
    assert ch1_2_2(s1, s1)
    assert ch1_2_2(s2, s2[::-1])
    assert not ch1_2_2(s1, s3)

    assert not ch1_2_3(s1, s2)
    assert ch1_2_3(s1, s1)
    assert ch1_2_3(s2, s2[::-1])
    assert not ch1_2_3(s1, s3)

    assert not ch1_2_4(s1, s2)
    assert ch1_2_4(s1, s1)
    assert ch1_2_4(s2, s2[::-1])
    assert not ch1_2_4(s1, s3)


def test_1_4():
    test_cases = [
        ('Tact Coa', True),
        ('tactcoapapa', True),
        ('tactcoapapad', False),
    ]
    for test_case, outcome in test_cases:
        # assert ch1_4_1(test_case) == outcome
        assert ch1_4_2(test_case) == outcome
        assert ch1_4_3(test_case) == outcome



def test_1_5():
    tests = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
    ]

    for (s1, s2, outcome) in tests:
        assert ch1_5_1(s1, s2) == outcome
        assert ch1_5_2(s1, s2) == outcome
        assert ch1_5_3(s1, s2) == outcome

    # %timeit ch1_5_2(s1, s2)
    # Answer key solution is slower.
    # %timeit ch1_5_3(s1, s2)


def test_1_6():
    s = 'aabcccccaaa'
    ns = 'a2b1c5a3'
    assert ch1_6_1(s) == ns


def test_1_7():
    mat = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
    mat_t = np.array([[1, 4, 7],
                      [2, 5, 8],
                      [3, 6, 9]])
    ch1_7_1(mat)
    assert np.all(mat == mat_t)


def test_1_8():
    impls = [
        ch1_8_1,
        # ch1_8_2,
    ]
    for impl in impls:
        dim = 10
        a = np.random.random((dim, dim))
        b = a.copy()
        # print(a)
        a[4, 5] = 0
        a[4, 7] = 0
        b[4, :] = 0
        b[:, 5] = 0
        b[:, 7] = 0
        # print(a)
        # print(b)
        impl(a)
        # print(a)
        assert np.all(a == b)


def test_1_9():
    s1 = 'waterbottle'
    s2 = 'erbottlewat'
    s3 = 'erbottlewaf'
    assert ch1_9_1(s1, s2)
    assert not ch1_9_1(s1, s3)


def test_frequencies():
    test_cases = [
        ('', dict()),
        ('Tact Coa', {'T': 1, 'a': 2, 'c': 1, 't': 1, 'C': 1, 'o': 1, ' ': 1}),
        ('tactcoapapa', {'t': 2, 'a': 4, 'c': 2, 'o': 1, 'p': 2}),
    ]
    for test_case, outcome in test_cases:
        assert make_frequencies(test_case) == outcome
