class Solution:
    @staticmethod
    def strStr(haystack, needle):
        """
        Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if haystack == needle:
            return 0
        elif len(needle) > len(haystack):
            return -1
        else:
            index = -1
            nl = len(needle)
            for i in range(len(haystack)):
                if haystack[i:i+nl] == needle:
                    index = i
                    break
            return index

print(Solution.strStr("", ""))
