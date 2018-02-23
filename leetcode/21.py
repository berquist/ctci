import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """Merge two sorted linked lists and return it as a new list. The new
    list should be made by splicing together the nodes of the first
    two lists.

    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
    """
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val <= l2.val:
            n = ListNode(l1.val)
            n.next = self.mergeTwoLists(l1.next, l2)
        else:
            n = ListNode(l2.val)
            n.next = self.mergeTwoLists(l1, l2.next)
        return n


@pytest.mark.skip()
def test_mergeTwoLists():
    # assert Solution().mergeTwoLists() == ""
    # assert Solution().mergeTwoLists() == "car"
    # [1], []
    return True
