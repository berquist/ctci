import pytest


class Solution(object):
    """Given an array and a value, remove all instances of that value
    in-place and return the new length.

    Do not allocate extra space for another array, you must do this by
    modifying the input array in-place with O(1) extra memory.

    The order of elements can be changed. It doesn't matter what you
    leave beyond the new length.
    """
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nl = len(nums)
        # loop through the list
        # if i is a matching elemn
        # slice off the tail
        print(nums)
        for i in range(nl):
            if nums[i] == val:
                if (i + 1) >= nl:
                    nums = nums[:i]
                else:
                    nums = nums[:i] + list(nums[i+1:])
                nl = self.removeElement(nums, val)
        return nl


@pytest.mark.skip()
def test_removeElement():
    nums, val = [3, 2, 2, 3], 3
    nl = Solution().removeElement(nums, val)
    assert nums == [2, 2]
    assert nl == 2
    return True
