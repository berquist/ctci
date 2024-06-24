class Solution:
    """Given a sorted array nums, remove the duplicates in-place such that
    each element appear only once and return the new length.

    Do not allocate extra space for another array, you must do this by
    modifying the input array in-place with O(1) extra memory.
    """
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i = 1
        old = nums[0]
        while i != len(nums):
            new = nums[i]
            if new == old:
                nums.pop(i)
            else:
                old = new
                i += 1
        return len(nums)


def test_removeDuplicates():

    nums = []
    length = Solution().removeDuplicates(nums)
    assert length == 0
    assert nums == []

    nums = [1, 1, 2]
    length = Solution().removeDuplicates(nums)
    assert length == 2
    assert nums == [1, 2]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    length = Solution().removeDuplicates(nums)
    assert length == 5
    assert nums == [0, 1, 2, 3, 4]
