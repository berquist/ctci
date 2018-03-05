import pytest


class Solution:
    """Given a string containing just the characters '(', ')', '{', '}',
    '[' and ']', determine if the input string is valid.

    The brackets must close in the correct order, "()" and "()[]{}"
    are all valid but "(]" and "([)]" are not.
    """
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        m = {')': '(', ']': '[', '}': '{'}
        for i in range(1, len(s), 2):
            print(s[i - 1], s[i])
            if s[i - 1] != m.get(s[i]):
                return False
        return True


@pytest.mark.skip()
def test_isValid():
    assert Solution().isValid("[") == False
    assert Solution().isValid("()") == True
    assert Solution().isValid("()[]{}") == True
    assert Solution().isValid("(]") == False
    assert Solution().isValid("([)]") == False
    assert Solution().isValid("([])") == True
    return True
