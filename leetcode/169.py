from collections import Counter
from typing import List


class Solution:
    """Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋
    times. You may assume that the majority element always exists in the
    array.
    """
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        bound = n / 2
        c = Counter(nums)
        for k, v in c.items():
            if v > bound:
                return k

def test_majorityElement() -> None:
    sln = Solution()
    assert sln.majorityElement([3, 2, 3]) == 3
    assert sln.majorityElement([2,2,1,1,1,2,2]) == 2
    assert sln.majorityElement([20]) == 20
