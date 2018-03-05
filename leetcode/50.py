class Solution(object):

    def myPow(self, x, n):
        """
        Implement pow(x, n).
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        else:
            acc = 1
            for _ in range(1, abs(n) + 1):
                acc = acc * x
            if n < 0:
                return 1 / acc
            else:
                return acc

# print(Solution().myPow(5.2, 3), 5.2 ** 3)
# print(Solution().myPow(5.2, -3), 5.2 ** (-3))
# print(Solution().myPow(0.00001, 2147483647))
# print(Solution().myPow(8.88023, 3), 8.88023 ** 3)
# assert Solution().myPow(5.2, 3) == (5.2 ** 3)
# assert Solution().myPow(5.2, -3) == (5.2 ** (-3))
