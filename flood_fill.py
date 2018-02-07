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

def flood_fill_recursive(array, shape, index, target_val, replacement_val):
    if target_val == replacement_val:
        return
    n, m = shape
    i, j = index
    if i >= n:
        return
    if j >= m:
        return
    if array[i][j] != target_val:
        return
    array[i][j] = replacement_val
    flood_fill_recursive(array, shape, (i + 1, j), target_val, replacement_val)
    flood_fill_recursive(array, shape, (i - 1, j), target_val, replacement_val)
    flood_fill_recursive(array, shape, (i, j - 1), target_val, replacement_val)
    flood_fill_recursive(array, shape, (i, j + 1), target_val, replacement_val)
    return


flood_fill = flood_fill_recursive


def check_representation(grid):
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
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                index = (i, j)
                break
    flood_fill(grid, shape, index, 1, 2)
    # 2.2 Look at every array element; if any 1s remain, not all light
    # squares were connected.
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                return False
    return True


def test_check_representation():
    grid_good = [[0, 0, 1, 1, 1, 1],
                 [0, 1, 1, 1, 1, 0],
                 [1, 1, 1, 1, 0, 0]]
    assert check_representation(grid_good)
    grid_bad = [[0, 0, 1, 1, 0, 0],
                [1, 1, 0, 0, 1, 1],
                [0, 0, 1, 1, 0, 0]]
    assert not check_representation(grid_bad)
    small_not_symmetric = [[0],
                           [1]]
    assert not check_representation(small_not_symmetric)
    small_not_connected = [[0, 1],
                           [1, 0]]
    assert not check_representation(small_not_connected)
    good_2_1 = [[1],
                [1]]
    assert check_representation(good_2_1)
    good_2_2 = [[1, 1],
                [1, 1]]
    assert check_representation(good_2_2)
    return True
