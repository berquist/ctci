class Solution(object):
    """The count-and-say sequence is the sequence of integers with the
    first five terms as following:

    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221

    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.

    Given an integer n, generate the nth term of the count-and-say
    sequence.

    Note: Each term of the sequence of integers will be represented as
    a string.
    """
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # strategy: build a bottom-up recursive solution
        s = "1"
        if n == 1:
            return s
        def helper(s):
            rs = []
            if len(s) == 1:
                return "1" + str(s)
            old = s[0]
            counter = 1
            for i in range(1, len(s)):
                new = s[i]
                if new != old:
                    rs.append((counter, old))
                    counter = 1
                else:
                    counter += 1
                old = new
            rs.append((counter, old))
            return ''.join(['{}{}'.format(*p) for p in rs])
        for _ in range(n - 1):
            s = helper(s)
        return s


def test_countAndSay():
    assert Solution().countAndSay(1) == "1"
    assert Solution().countAndSay(2) == "11"
    assert Solution().countAndSay(3) == "21"
    assert Solution().countAndSay(4) == "1211"
    assert Solution().countAndSay(5) == "111221"
    assert Solution().countAndSay(6) == "312211"
