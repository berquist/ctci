class Solution:
    """Given a roman numeral, convert it to an integer.

    Input is guaranteed to be within the range from 1 to 3999."""
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import OrderedDict
        m = OrderedDict([
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000),
        ])
        lm = list(m.keys())
        acc = 0
        # If the index of the current character is larger than the
        # previous one, that indicates subtraction.
        for i in range(len(s)):
            if (i > 0) and (lm.index(s[i]) > lm.index(s[i - 1])):
                acc += (m[s[i]] - (2 * m[s[i - 1]]))
            else:
                acc += m[s[i]]
        return acc


def test_romanToInt():
    assert Solution().romanToInt('I') == 1
    assert Solution().romanToInt('V') == 5
    assert Solution().romanToInt('X') == 10
    assert Solution().romanToInt('L') == 50
    assert Solution().romanToInt('C') == 100
    assert Solution().romanToInt('D') == 500
    assert Solution().romanToInt('M') == 1000
    # 1000, 100, 1000, 10, 100, 5, 1
    assert Solution().romanToInt('MCMXCVI') == 1996
    assert Solution().romanToInt('DCXXI') == 621
    return True
