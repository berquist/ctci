from collections import namedtuple

class Solution:
    """Given two sorted integer arrays `nums1` and `nums2`, merge `nums2`
    into `nums1` as one sorted array.

    Note:
    * The number of elements initialized in `nums1` and `nums2` are `m` 
    and `n`, respectively.
    * You may assume that `nums1` has enough space (size that is greater or
    equal to `m + n`) to hold additional elements for `nums2`.
    """
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for k in range(n):
            # insert at end
            nums1[m] = nums2[k]
            m += 1
            # swap downward
            for i in reversed(range(1, m)):
                if nums1[i - 1] > nums1[i]:
                    nums1[i - 1], nums1[i] = nums1[i], nums1[i - 1]
                else:
                    break
        return

    def merge_forum1(self, nums1, m, nums2, n):
        if m == 0: nums1 = nums2
        print(id(nums1))
        nums1 = nums1[m:] + nums1[0:m]
        print(id(nums1))
        p1, p2, loc = len(nums1)-m, 0, 0
        while p2 < len(nums2) and loc < len(nums1):
            if p1 < len(nums1) and nums1[p1] <= nums2[p2]:
                nums1[loc] = nums1[p1]
                p1 += 1
            else:
                nums1[loc] = nums2[p2]
                p2 += 1
            loc += 1
        return

Case = namedtuple('Case', ['nums1', 'm', 'nums2', 'n', 'res'])

def test_merge():

    test_cases = [
        Case([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
        Case([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ]
    for test_case in test_cases:
        nums1 = test_case.nums1.copy()
        Solution().merge(nums1, test_case.m, test_case.nums2, test_case.n)
        assert nums1 == test_case.res
