from math import floor, inf


class Solution:
    """Given a non-negative integer x, compute and return the square root of
    x.

    Since the return type is an integer, the decimal digits are truncated, and
    only the integer part of the result is returned.

    Note: You are not allowed to use any built-in exponent function or
    operator, such as pow(x, 0.5) or x ** 0.5.
    """
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        thresh = 1.0e-4
        y_prev = inf
        y = x / 2
        while (y_prev - y) > thresh:
            y_prev = y
            y = (y_prev + (x / y_prev)) / 2
        return floor(y)


def test_mySqrt() -> None:
    sln = Solution()
    assert sln.mySqrt(4) == 2
    assert sln.mySqrt(8) == 2
    assert sln.mySqrt(120) == 10
    assert sln.mySqrt(1) == 1
    assert sln.mySqrt(34568475645) == 185925
