class Solution(object):
    """Given an array of integers, return **indices** of the two numbers
    such that they add up to a specific target.

    You may assume that each input would have _**exactly**_ one
    solution, and you may not use the _same_ element twice.

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for j in range(len(nums)):
            for i in range(j):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum2(self, nums, target):
        d = {nums[i]: i for i in range(len(nums))}
        for i in d:
            j = target - i
            if j in d and j != i:
                return [d[i], d[j]]

    def twoSum3(self, nums, target):
        d = dict()
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in d:
                return [d[comp], i]
            d[nums[i]] = i


def test_twoSum():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]
    return True


def test_twoSum2():
    assert Solution().twoSum2([2, 7, 11, 15], 9) == [0, 1]
    assert Solution().twoSum2([3, 2, 4], 6) == [1, 2]
    return True


def test_twoSum3():
    assert Solution().twoSum3([2, 7, 11, 15], 9) == [0, 1]
    assert Solution().twoSum3([3, 2, 4], 6) == [1, 2]
    return True
