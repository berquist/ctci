def bubble_sort(l):
    ln = len(l)
    if ln == 1:
        return
    is_sorted = False
    while not is_sorted:
        # bubble pass
        for i in range(1, ln):
            if l[i - 1] > l[i]:
                tmp = l[i - 1]
                l[i - 1] = l[i]
                l[i] = tmp
        # check pass
        pass_is_sorted = True
        for i in range(1, ln):
            if l[i - 1] > l[i]:
                pass_is_sorted = False
                break
        if pass_is_sorted:
            is_sorted = True
    return


def test_bubble_sort():
    l1 = [9, 8, 7, 6, 5, -1, -2]
    l1_ref = [-2, -1, 5, 6, 7, 8, 9]
    bubble_sort(l1)
    assert l1 == l1_ref
    l2 = [2, 3, 4, 10, 20, 90]
    l2_ref = l2.copy()
    bubble_sort(l2)
    assert l2 == l2_ref
    return True


def sorted_matrix_search(mat, element):
    """return the matrix tuple (i, j) of the element's location in the
    matrix; if not found, return None
    """
    # scan along the shortest dimension which presumably has the
    # longest stride -> future optimization
    assert len(mat) > 0
    assert len(mat[0]) > 0
    m, n = len(mat), len(mat[0])
    if mat[0][0] > element:
        return None
    if mat[m - 1][n - 1] < element:
        return None
    # this is really searching for the midpoint
    for i in range(m):
        if mat[i][0] == element:
            return (i, 0)
        elif mat[i][0] > element:
            i = i - 1
            break
    # this should be binary search
    for j in range(n):
        if mat[i][j] == element:
            return (i, j)
        elif mat[i][j] > element:
            break
    return None


def test_sorted_matrix_search():
    mat1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    # mat1t = [[1, 4, 7],
    #          [2, 5, 8],
    #          [3, 6, 9]]
    assert sorted_matrix_search(mat1, 0) == None
    assert sorted_matrix_search(mat1, 1) == (0, 0)
    assert sorted_matrix_search(mat1, 2) == (0, 1)
    assert sorted_matrix_search(mat1, 3) == (0, 2)
    assert sorted_matrix_search(mat1, 4) == (1, 0)
    assert sorted_matrix_search(mat1, 5) == (1, 1)
    assert sorted_matrix_search(mat1, 6) == (1, 2)
    assert sorted_matrix_search(mat1, 7) == (2, 0)
    assert sorted_matrix_search(mat1, 8) == (2, 1)
    assert sorted_matrix_search(mat1, 9) == (2, 2)
    assert sorted_matrix_search(mat1, 10) == None
    return True


if __name__ == '__main__':
    test_bubble_sort()
    test_sorted_matrix_search()
