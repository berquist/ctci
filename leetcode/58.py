import pytest


class Solution(object):
    """Given a string s consists of upper/lower-case alphabets and empty
    space characters ' ', return the length of last word in the string.

    If the last word does not exist, return 0.

    Note: A word is defined as a character sequence consists of non-space
    characters only.
    """
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ln = 0
        counter = 0
        for i in len(s):
            if s[i] == ' ':
                ln = len(s[counter:i])
        return ln


@pytest.mark.skip()
def test_lengthOfLastWord():
    assert Solution().lengthOfLastWord("Hello World") == 5
    assert Solution().lengthOfLastWord("") == 0
    assert Solution().lengthOfLastWord(" ") == 0
    return True
