from typing import List, Tuple


def compound_to_square(dim: int, ci: int) -> Tuple[int, int]:
    d2 = dim * dim
    # if ci >= d2 or ci < 0:
    #     raise ValueError
    return ci // dim, ci % dim


def square_to_compound(dim: int, i: int, j: int) -> int:
    # if i >= dim or i < 0:
    #     raise ValueError
    # if j >= dim or j < 0:
    #     raise ValueError
    return (dim * i) + j


class Solution:
    """Given a 2D grid of size m x n and an integer k. You need to shift the
    grid k times.

    In one shift operation:

    - Element at grid[i][j] moves to grid[i][j + 1].
    - Element at grid[i][n - 1] moves to grid[i + 1][0].
    - Element at grid[m - 1][n - 1] moves to grid[0][0].

    Return the 2D grid after applying shift operation k times.
    """
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        n2 = n * n
        k = n2 % k
        shifted = [r for r in grid]
        it = 0
        ci = 0
        # place = shifted[i1][j1]
        while it <= n:
            cik = ci + k
            if cik >= n:
                cik %= n
            i1, j1 = compound_to_square(n, ci)
            i2, j2 = compound_to_square(n, cik)
            # - Store what we're about to replace
            # - Put the store from the last iter in that spot
            # store = shifted[i2][j2]
            # shifted[i2][j2] = place
            ci = cik
            it += 1
        return shifted


def test_square_to_compound() -> None:
    assert square_to_compound(3, 0, 0) == 0
    assert square_to_compound(3, 0, 1) == 1
    assert square_to_compound(3, 0, 2) == 2
    assert square_to_compound(3, 1, 0) == 3
    assert square_to_compound(3, 2, 2) == 8


def test_compound_to_square() -> None:
    assert compound_to_square(3, 0) == (0, 0)
    assert compound_to_square(3, 3) == (1, 0)
    assert compound_to_square(3, 5) == (1, 2)
    assert compound_to_square(3, 7) == (2, 1)
    assert compound_to_square(3, 8) == (2, 2)


def test_shiftGrid() -> None:
    sln = Solution()
    assert sln.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 1) == [[9,1,2],[3,4,5],[6,7,8]]
    # assert sln.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 2) == [[8,9,1],[2,3,4],[5,6,7]]
    # assert sln.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 3) == [[7,8,9],[1,2,3],[4,5,6]]
    # assert sln.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 9) == [[1,2,3],[4,5,6],[7,8,9]]
    # assert sln.shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4) == [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
