import pytest


class Solution:
    """Determine whether an integer is a palindrome. Do this without extra
    space.
    """
    def isPalindrome_extra(self, x):
        """
        :type x: int
        :rtype: bool
        """
        is_negative = x < 0
        if is_negative:
            return False
        s = str(x)[is_negative:]
        m = len(s) // 2
        n = m
        if len(s) % 2 == 1:
            n += 1
        return s[:m] == s[n:][::-1]

    def isPalindrome(self, x):
        import math
        ax = abs(x)
        # apparently negative numbers aren't palindromes
        if ax != x:
            return False
        if ax < 10:
            return True
        ndigits = int(math.log10(ax) + 1)
        for i in range(1, ndigits + 1):
            j = ndigits - i + 1
            dj = ax % (10 ** j) // (10 ** (j - 1))
            di = ax % (10 ** i) // (10 ** (i - 1))
            if di != dj:
                return False
        return True

    def isPalindrome_solution(self, x):
        # Special cases: As discussed above, when x < 0, x is not a
        # palindrome. Also if the last digit of the number is 0, in
        # order to be a palindrome, the first digit of the number also
        # needs to be 0. Only 0 satisfies this property.
        if (x < 0) or ((x % 10 == 0) and (x != 0)):
            return False
        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = (revertedNumber * 10) + (x % 10)
            x /= 10
        # When the length is an odd number, we can get rid of the
        # middle digit by revertedNumber/10 For example when the input
        # is 12321, at the end of the while loop we get x = 12,
        # revertedNumber = 123, since the middle digit doesn't matter
        # in palidrome(it will always equal to itself), we can simply
        # get rid of it.
        return (x == revertedNumber) or (x == (revertedNumber / 10))


def test_isPalindrome_extra():
    assert Solution().isPalindrome_extra(11)
    assert not Solution().isPalindrome_extra(12)
    assert Solution().isPalindrome_extra(12321)
    assert not Solution().isPalindrome_extra(-2147483648)
    assert Solution().isPalindrome_extra(0)
    assert not Solution().isPalindrome_extra(-2147447412)


def test_isPalindrome():
    assert Solution().isPalindrome(11)
    assert not Solution().isPalindrome(12)
    assert Solution().isPalindrome(12321)
    assert not Solution().isPalindrome(-2147483648)
    assert Solution().isPalindrome(0)
    assert not Solution().isPalindrome(-2147447412)


@pytest.mark.skip()
def test_isPalindrome_solution():
    assert Solution().isPalindrome_solution(11)
    assert not Solution().isPalindrome_solution(12)
    assert Solution().isPalindrome_solution(12321)
    assert not Solution().isPalindrome_solution(-2147483648)
    assert Solution().isPalindrome_solution(0)
    assert not Solution().isPalindrome_solution(-2147447412)
