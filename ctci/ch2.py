class SNode(object):
    """A node in a singly-linked list."""

    def __init__(self, data=None):

        self.data = data
        self.next = None

    def __bool__(self):
        return self.data is not None

    def __eq__(self, other_node):
        """Another node is equal to this one if it is exactly the same: both
        its data and next are identical.
        """
        if hasattr(other_node, 'data'):
            if self.data is None or other_node.data is None:
                data = self.data is other_node.data
            else:
                data = self.data == other_node.data
        else:
            return False
        if hasattr(other_node, 'next'):
            if self.next is None or other_node.next is None:
                next = self.next is other_node.next
            else:
                next = self.next == other_node.next
        else:
            return False
        return data and next

    def eq_data(self, other_node):
        """Another node is equal to this one if it contains the same data but
        isn't the same node.
        """
        return (self.data == other_node.data) \
            and self != other_node

    def __str__(self):
        if self.next is None:
            return 'SNode({}).X'.format(self.data)
        else:
            return 'SNode({}).{}'.format(self.data, str(self.next))

    def __len__(self):
        # for constant-time len, should keep track of it as we
        # append/delete
        if not self.next:
            return int(self.data is not None)
        else:
            return 1 + len(self.next)

    def __getitem__(self, index):
        if index < 0:
            raise Exception
        counter = 0
        node = self
        while counter != index:
            node = node.next
            counter += 1
        return node.data

    def __iter__(self):
        node = self
        while node:
            yield node.data
            node = node.next

    def append(self, node):
        """Append the given node to this linked list in-place."""
        if not self.data:
            self.data = node.data
        elif not self.next:
            self.next = node
        else:
            self.next.append(node)
        return

    def delete_inplace(self, data):
        """Remove the node containing the first match to the given data
        in-place. Always keep a null node at the end.
        """
        if self.data == data:
            if self.next:
                self.data = self.next.data
                self.next.shift()
            else:
                self.data = None
        else:
            if self.next:
                self.next.delete_inplace(data)
            else:
                pass
        self.tidy()
        return

    def tidy(self):
        """Remove None nodes from the list."""
        if self.next is not None and self.next.data is None:
            if self.next.next is not None:
                self.next = self.next.next
                self.tidy()
            else:
                self.next = None
        elif self.next is not None:
            self.next.tidy()
        return

    def shift(self):
        """Shift the data in the linked list up one level, overwriting the
        data at this node.
        """
        if self.next:
            self.data = self.next.data
            self.next.shift()
        else:
            self.data = None

    def sort(self):
        """'In-place' sort."""
        items = sorted([x for x in self])
        self.data = None
        self.next = None
        for item in items:
            self.append(SNode(item))
        return



class SLinkedList(object):
    """This singly-linked list is a slight convenience wrapper for
    SNode.
    """

    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        if not self.head:
            return 0
        else:
            return len(self.head)

    def __getitem__(self, index):
        if index < 0:
            raise Exception
        counter = 0
        node = self.head
        while counter != index:
            node = node.next
            counter += 1
        return node.data

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def append(self, data):
        node = SNode(data)
        if not self.head:
            self.head = node
        else:
            self.head.append(node)

    def _delete(self, data, node):
        if node.data == data:
            return node.next
        else:
            return self._delete(data, node.next)

    def delete(self, data):
        return self._delete(data, self.head)


def delete(head, data):
    """This is the solution from page 93."""
    n = head

    if n.data == data:
        return head.next

    while n.next:
        if n.next.data == d:
            n.next = n.next.next
            return head
        n = n.next

    return head


def test_snode_append():
    values = [2, 4, 8, 9, 10]
    head = SNode()
    for value in values:
        node = SNode(value)
        head.append(node)
    assert len(head) == len(values)
    assert head.data == values[0]
    assert head.next.data == values[1]
    return True


def test_slinkedlist_append():
    values = [2, 4, 8, 9, 10]
    ll = SLinkedList()
    for value in values:
        ll.append(value)
    assert len(ll) == len(values)
    return True


def test_snode_iter():
    values = [2, 4, 8, 9, 10]
    head = SNode()
    for value in values:
        node = SNode(value)
        head.append(node)
    assert len(head) == len(values)
    assert head.data == values[0]
    assert head.next.data == values[1]
    # __iter__
    for data, value in zip(head, values):
        assert data == value
    # __getitem__
    for i in range(len(values)):
        assert head[i] == values[i]
    return True


def test_slinkedlist_iter():
    values = [2, 4, 8, 9, 10]
    ll = SLinkedList()
    for value in values:
        ll.append(value)
    assert len(ll) == len(values)
    # __iter__
    for data, value in zip(ll, values):
        assert data == value
    # __getitem__
    for i in range(len(values)):
        assert ll[i] == values[i]
    return True


def test_snode_tidy():
    # [2, None] -> [2]
    head = SNode(2)
    head.next = SNode()
    assert head.data == 2
    assert head.next is not None
    assert head.next.data is None
    assert head.next.next is None
    head.tidy()
    assert head.data == 2
    assert head.next is None
    # [2, None, 4] -> [2, 4]
    head.next = SNode()
    head.next.next = SNode(4)
    assert head.data == 2
    assert head.next.data == None
    assert head.next.next.data == 4
    assert head.next.next.next == None
    head.tidy()
    assert head.data == 2
    assert head.next.data == 4
    assert head.next.next == None
    # [2, None, None, None, 4] -> [2, 4]
    head = SNode(2)
    head.next = SNode(None)
    head.next.next = SNode(None)
    head.next.next.next = SNode(None)
    head.next.next.next.next = SNode(4)
    head.tidy()
    assert head.data == 2
    assert head.next.data == 4
    assert head.next.next == None
    return True


def test_snode_shift():
    values = [2, 4]
    head = SNode()
    for value in values:
        node = SNode(value)
        head.append(node)
    assert len(head) == len(values)
    head.next.data = None
    head.shift()
    # shift() doesn't tidy()
    assert head.data is None
    assert head.next is not None
    assert head.next.data is None
    assert head.next.next is None
    # Can't delete the current object, so the empty linked list
    # contains a single node with no data and no next.
    head.tidy()
    assert head.data is None
    assert head.next is None
    return True


def test_snode_delete_inplace():
    values = [2, 4, 8, 9, 10]
    head = SNode()
    for value in values:
        node = SNode(value)
        head.append(node)
    head.delete_inplace(values[1])
    assert len(head) == len(values) - 1
    assert head.data == values[0]
    assert head.next.data == values[2]
    assert head.next.next.data == values[3]
    assert head.next.next.next.data == values[4]
    assert head.next.next.next.next is None
    return True


def test_snode_delete_head_inplace():
    values = [2, 4, 8, 9, 10]
    head = SNode()
    for value in values:
        node = SNode(value)
        head.append(node)
    head.delete_inplace(values[0])
    assert len(head) == len(values) - 1
    assert head.data == values[1]
    assert head.next.data == values[2]
    assert head.next.next.data == values[3]
    assert head.next.next.next.data == values[4]
    assert head.next.next.next.next is None
    return True


# def test_slinkedlist_delete_head()


def remove_duplicates(node):
    """Implementation for 2.1 (with buffer)"""
    buf = set()
    if node.data is None:
        return
    current_node = node
    while current_node is not None:
        buf.add(current_node.data)
        if current_node.next is not None:
            # if current_node.next.data in buf:
            #     current_node.next = current_node.next.next
            while current_node.next is not None and current_node.next.data in buf:
                current_node.next = current_node.next.next
        current_node = current_node.next
    return


def test_remove_duplicates():
    """Test for 2.1"""
    values = [10, 9, 9, 9, 10, 8, 4, 2, 2, 2]
    ref = [10, 9, 8, 4, 2]
    head = SNode()
    for value in values:
        head.append(SNode(value))
    remove_duplicates(head)
    ret = [data for data in head]
    assert ret == ref
    return True


# Can't do this: the resulting list shouldn't necessarily be sorted.
#
# def remove_duplicates_nobuffer(node):
#     """Implementation for 2.1"""
#     node.sort()
#     current_node = node
#     while current_node is not None:
#         if current_node.next is not None:
#             # look ahead: if the next node is a match...
#             if current_node.data == current_node.next.data:
#                 # ...replace the next node with _its_ next node
#                 current_node.next = current_node.next.next
#         current_node = current_node.next
#     return


def test_snode_eq():
    # base case
    n0 = SNode()
    assert n0 == SNode()
    # simple cases
    n1 = SNode(3)
    n2 = SNode(3)
    n3 = SNode(4)
    assert id(n1) != id(n2)
    assert n1 is not n2
    assert n1 == n2
    assert id(n1) != id(n3)
    assert n1 is not n3
    assert n1 != n3
    # sublevels
    n1.append(SNode(4))
    n1.append(SNode(5))
    n2.append(SNode(4))
    n2.append(SNode(5))
    assert id(n1) != id(n2)
    assert n1 is not n2
    assert n1 == n2
    assert n1.next == n2.next
    return True


def test_snode_eq_data():
    values = [10, 9, 9, 9, 10, 8, 4, 2, 2, 2]
    head = SNode()
    for value in values:
        head.append(SNode(value))
    assert not head.next.eq_data(head.next)
    assert head.next.eq_data(head.next.next)
    assert head.next.eq_data(head.next.next.next)
    assert head.next.next.next.eq_data(head.next)
    return True


def remove_duplicates_nobuffer(node):
    """Implementation for 2.1 (without buffer)"""
    if node.data is None:
        return
    current_node = node
    # for each element in the list with index i
    while current_node is not None:
        if current_node.next is not None:
            # start the inner node loop at 0
            inner_node = node
            # print('=' * 70)
            # print('current_node: {} '.format(current_node))
            # print('current_node.next: {} '.format(current_node.next))
            # print('start inner loop')
            while inner_node is not None and inner_node != current_node.next:
                # print('-' * 70)
                # print(inner_node)
                # print(current_node)
                # look at the next element i+1;
                # if i+1 occurs anywhere in [0..i], remove i+1
                while current_node.next is not None and current_node.next.eq_data(inner_node):
                    current_node.next = current_node.next.next
                inner_node = inner_node.next
        # make sure we didn't miss the current node
        inner_node = node
        while inner_node is not None and inner_node != current_node:
            if current_node.eq_data(inner_node):
                current_node.shift()
            inner_node = inner_node.next
        current_node = current_node.next
    return


def test_remove_duplicates_nobuffer():
    """Test for 2.1"""
    tests = [
        [
            [],
            [],
        ],
        [
            [10],
            [10],
        ],
        [
            [10, 9, 10],
            [10, 9],
        ],
        [
            [10, 9, 9, 9, 10, 8],
            [10, 9, 8],
        ],
        [
            [10, 9, 9, 9, 10, 8, 4, 2, 2, 2],
            [10, 9, 8, 4, 2],
        ],
        [
            list([10 for _ in range(100)]),
            [10],
        ],
    ]
    for values, ref in tests:
        head = SNode()
        for value in values:
            head.append(SNode(value))
        remove_duplicates_nobuffer(head)
        ret = [data for data in head]
        assert ret == ref
    return True


if __name__ == '__main__':
    test_snode_append()
    test_slinkedlist_append()
    test_snode_iter()
    test_slinkedlist_iter()
    test_snode_tidy()
    test_snode_shift()
    test_snode_delete_inplace()
    test_snode_delete_head_inplace()
    # test_slinkedlist_delete_head()
    test_remove_duplicates()
    test_snode_eq()
    test_snode_eq_data()
    test_remove_duplicates_nobuffer()
