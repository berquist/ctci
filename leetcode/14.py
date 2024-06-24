class Solution:
    """Write a function to find the longest common prefix string amongst
    an array of strings.
    """
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        maxlen = min(len(s) for s in strs)
        lcp = []
        for i in range(maxlen):
            c = strs[0][i]
            sc = [s[i] for s in strs]
            if sc.count(c) == len(strs):
                lcp.append(c)
            else:
                break
        return ''.join(lcp)


def test_longestCommonPrefix():
    assert Solution().longestCommonPrefix([]) == ""
    assert Solution().longestCommonPrefix(['car', 'card', 'carding']) == "car"
