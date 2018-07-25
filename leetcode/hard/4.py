class Solution:
    """There are two sorted arrays nums1 and nums2 of size m and n
    respectively.

    Find the median of the two sorted arrays. The overall run time
    complexity should be O(log (m+n)).
    """
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def median(l):
            is_even = (len(l) % 2) == 0
            i = len(l) // 2
            if not is_even:
                return l[i]
            else:
                return (l[i - 1] + l[i]) / 2
        m1 = median(nums1)
        m2 = median(nums2)
        return (m1 + m2) / 2


def test_findMedianSortedArrays():
    test_cases = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
    ]
    for nums1, nums2, result in test_cases:
        assert abs(Solution().findMedianSortedArrays(nums1, nums2) - result) < 1.0e-13
    return True
