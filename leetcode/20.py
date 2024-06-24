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
        seen = [s[0]]
        m = {')': '(', ']': '[', '}': '{'}
        for c in s[1:]:
            # If we're looking at a left, push it onto the stack. If we're
            # looking at a right, pop from the stack.  If they don't match,
            # fail.
            if c in m.values():
                seen.append(c)
            else:
                right = c
                if seen:
                    left = seen.pop()
                    if m[right] != left:
                        return False
                else:
                    return False
        # If any are left on the stack, something didn't match.
        if seen:
            return False
        return True


def test_isValid() -> None:
    sln = Solution()
    assert not sln.isValid("[")
    assert sln.isValid("()")
    assert sln.isValid("()[]{}")
    assert not sln.isValid("(]")
    assert not sln.isValid("([)]")
    assert sln.isValid("([])")
    assert not sln.isValid("((")
    assert not sln.isValid("(){}}{")
