from ch3 import Queue


'''Notes from mock interview.

n x m rectangle


2 properties:
* C2 symmetric (axis perpendicular to the grid)
* All light squares are up, down, left, right connected


XXOOXX
OOXXOO
XXOOXX


XXO OOO
XOO OOX
OOO OXX


(x,y) -> (-x, -y)


x1, x2, y1 ,y2 ==> x1 + x2 = const. y1 + y2 = const.


n = 3, m = 6
[0, 3] -> [2, 2]
[1, 3] -> [1, 2]
[x, y] -> [n-x, m-y]


[3-0, 6-3] -> [3, 3] (x)
[3-1, 6-3] -> [2, 3]


Transformation for comparison: [x, y] -> [n-x-1, m-y-1]


Your solution:


def check_representation(grid):
        """Take in an [n, m] grid and return a boolean."""
        # 1. check for C2 symmetry
        for i in range(n):
                for j in range(m):
                        if grid[i, j] != grid[n-i-1, m-j-1]:
                                return False
        # 2. check for light square connectivity
        return True

Notes:
Algorithms:
  Graph algorithms (BFS, DFS, MST, Dijkstra’s, flood fill)
  Trees (binary search tree), walk tree, search a tree, add something, delete something
  Sorting (merge sort, quick sort, insertion sort)
  Priority queue (heap)
  Hash table/map. Bloom filter.


Write something down. A fine finished solution is better than a partially finished perfect solution.


Common data structures and language paradigms.
  Know how to use array/list/vector, set, dict/map, string
  https://docs.python.org/3/library/array.html
'''


def index_in_array(array, index):
    n = len(array)
    if n == 0:
        raise Exception
    m = len(array[0])
    if m == 0:
        raise Exception
    i, j = index
    if i < 0:
        return False
    if i >= n:
        return False
    if j < 0:
        return False
    if j >= m:
        return False
    return True


def flood_fill_recursive(array, index, target_val, replacement_val):
    """Perform flood fill on a 2D array using a stack."""
    if target_val == replacement_val:
        return
    if not index_in_array(array, index):
        return
    i, j = index
    if array[i][j] != target_val:
        return
    array[i][j] = replacement_val
    flood_fill_recursive(array, (i + 1, j), target_val, replacement_val)
    flood_fill_recursive(array, (i - 1, j), target_val, replacement_val)
    flood_fill_recursive(array, (i, j - 1), target_val, replacement_val)
    flood_fill_recursive(array, (i, j + 1), target_val, replacement_val)
    return


def flood_fill_iterative(array, index, target_val, replacement_val):
    """Perform flood fill on a 2D array using a queue."""
    if target_val == replacement_val:
        return
    if not index_in_array(array, index):
        return
    i, j = index
    if array[i][j] != target_val:
        return
    array[i][j] = replacement_val
    q = Queue()
    q.add(index)
    while not q.is_empty():
        a, b = q.remove()
        pairs = [
            (a, b - 1),
            (a, b + 1),
            (a - 1, b),
            (a + 1, b),
        ]
        for (c, d) in pairs:
            if index_in_array(array, (c, d)):
                if array[c][d] == target_val:
                    array[c][d] = replacement_val
                    q.add((c, d))
    return


def check_representation(grid, flood_fill_method=flood_fill_recursive):
    """Take in an [n, m] grid and return a boolean for whether or not the
    grid is C2 symmetric and all light squares are connected to
    each other.

    Light squares are marked as 1 and dark squares are marked as 0.
    """
    n = len(grid)
    if n == 0:
        raise Exception
    m = len(grid[0])
    if m == 0:
        raise Exception
    shape = (n, m)
    # 1. check for C2 symmetry
    for i in range(n):
        for j in range(m):
            if grid[i][j] != grid[n - i - 1][m - j - 1]:
                return False
    # 2. check for light square connectivity
    # cost reduction: only check left half
    # 2.1 Perform flood fill to try and mark all light squares with a 2.
    # Find the first light square and use that as the seed index.
    find = False
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                index = (i, j)
                find = True
                break
        if find:
            break
    flood_fill_method(grid, index, 1, 2)
    # 2.2 Look at every array element; if any 1s remain, not all light
    # squares were connected.
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                return False
    return True


def test_index_in_array():
    good_2_1 = [[1],
                [1]]
    assert index_in_array(good_2_1, (0, 0))
    assert index_in_array(good_2_1, (1, 0))
    assert not index_in_array(good_2_1, (0, 1))
    assert not index_in_array(good_2_1, (0, -1))
    return True


def test_check_representation():
    flood_fill_methods = (
        flood_fill_recursive,
        flood_fill_iterative,
    )
    for flood_fill_method in flood_fill_methods:
        small_not_symmetric = [[0],
                               [1]]
        assert not check_representation(small_not_symmetric, flood_fill_method)
        small_not_connected = [[0, 1],
                               [1, 0]]
        assert not check_representation(small_not_connected, flood_fill_method)
        good_2_1 = [[1],
                    [1]]
        assert check_representation(good_2_1, flood_fill_method)
        good_2_2 = [[1, 1],
                    [1, 1]]
        assert check_representation(good_2_2, flood_fill_method)
        grid_good = [[0, 0, 1, 1, 1, 1],
                     [0, 1, 1, 1, 1, 0],
                     [1, 1, 1, 1, 0, 0]]
        assert check_representation(grid_good, flood_fill_method)
        grid_bad = [[0, 0, 1, 1, 0, 0],
                    [1, 1, 0, 0, 1, 1],
                    [0, 0, 1, 1, 0, 0]]
        assert not check_representation(grid_bad, flood_fill_method)
    return True


if __name__ == '__main__':
    test_check_representation()
