def sorted_matrix_search(mat, element):
    """return the matrix tuple (i, j) of the element's location in the
    matrix; if not found, return None
    """
    # scan along the shortest dimension which presumably has the
    # longest stride -> future optimization
    assert len(mat) > 0
    assert len(mat[0]) > 0
    m, n = len(mat), len(mat[0])
    # the other extreme will be found quickly
    if mat[m - 1][n - 1] < element:
        return None
    i = None
    for p in range(m):
        if mat[p][0] == element:
            return (p, 0)
        elif mat[p][0] > element:
            # need to scan the other dimension
            i = p - 1
            break
    if i is None:
        return None
    for q in range(n):
        if mat[i][q] == element:
            return (i, q)
        elif mat[i][q] > element:
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
    test_sorted_matrix_search()
