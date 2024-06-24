class Solution:
    """Given a 32-bit signed integer, reverse digits of an integer."""
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        is_negative = x < 0
        intermediate = ''.join(reversed(str(x)[is_negative:])).lstrip('0')
        ret = int(('-' * is_negative) + intermediate)
        if abs(ret) > ((2 ** 31) - 1):
            return 0
        return ret


def test_reverse():
    assert Solution().reverse(123) == 321
    assert Solution().reverse(-123) == -321
    assert Solution().reverse(120) == 21
    # not 9646324351, there should be overflow
    assert Solution().reverse(1534236469) == 0
    # not -8463847412
    assert Solution().reverse(-2147483648) == 0
