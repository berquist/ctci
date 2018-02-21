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
    return True


if __name__ == '__main__':
    test_sorted_matrix_search()
