class Solution(object):
    """Given a sorted array and a target value, return the index if the
    target is found. If not, return the index where it would be if it were
    inserted in order.

    You may assume no duplicates in the array.
    """
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # ideal solution would be binary search to find index of
        # closest element
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        for i in range(len(nums)):
            if target <= nums[i]:
                return i


def test_searchInsert():
    assert Solution().searchInsert([1, 3, 5, 6], 5) == 2
    assert Solution().searchInsert([1, 3, 5, 6], 2) == 1
    assert Solution().searchInsert([1, 3, 5, 6], 7) == 4
    assert Solution().searchInsert([1, 3, 5, 6], 0) == 0
    assert Solution().searchInsert([1, 3], 3) == 1
    return True
