class SNode(object):

    def __init__(self, data=None):

        self.data = data
        self.next = None

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
            self.next = SNode()
        elif not self.next:
            self.next = node
        else:
            self.next.append(node)
        return

    def delete_inplace(self, data):
        """Remove the node containing the first match to the given data
        in-place. Always keep a null node at the end.
        """
        if not self.next:
            if self.data == data:
                self.data = None
            else:
                # don't need to do anything, this is the null node
                pass
        else:
            if self.data == data:
                # shift all data upward; need to remove the last node
                # with no data? no, this is handled below
                self.data = self.next.data
                self.next.shift()
            if self.next.data == data:
                if self.next.next:
                    self.next = self.next.next
                else:
                    self.next = None
            else:
                self.next.delete_inplace(data)
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

    # def delete(self, data):
    #     """Remove the node containing the first match to the given data."""
    #     pass


class SLinkedList(object):

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
    # print(len(head), len(values))
    assert len(head) == len(values) - 1
    assert head.data == values[1]
    assert head.next.data == values[2]
    assert head.next.next.data == values[3]
    assert head.next.next.next.data == values[4]
    assert head.next.next.next.next is None
    return True


# def test_slinkedlist_delete_head()


if __name__ == '__main__':
    test_snode_append()
    test_slinkedlist_append()
    test_snode_iter()
    test_slinkedlist_iter()
    # test_snode_delete_inplace()
    # test_snode_delete_head_inplace()
