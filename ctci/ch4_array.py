import math
import operator
import random

from ch3 import Queue


class Container(object):

    def __init__(self, data=None):

        if data is not None:
            self._repr = data.copy()
        else:
            self._repr = []

    def __str__(self):
        return str(self._repr)

    def __len__(self):
        # if hasattr(self, '_len'):
        #     return self._len
        # else:
        #     # return len(self._repr) - self._repr.count(None)
        #     return len(self._repr)
        return len(self._repr)

    def count(self):
        return len(self) - self._repr.count(None)

    def __eq__(self, other):
        return self._repr == other._repr

    def __getitem__(self, index):
        return self._repr[index]

    def _index_parent(self, i):
        return math.floor((i - 1) / 2)


class MinHeap(Container):

    def __init__(self, data=None):
        super().__init__(data)

    def extract(self):
        if not self._repr:
            raise Exception
        val = self._repr[0]
        if len(self) >= 2:
            self._repr[0], self._repr[-1] = self._repr[-1], self._repr[0]
            self._repr.pop()
            self._bubble_down(0)
        else:
            self._repr.pop()
        return val

    def insert(self, element):
        self._repr.append(element)
        self._bubble_up()
        return

    def _bubble_down(self, i=None):
        if i is None:
            i = 0
        if i >= len(self):
            raise IndexError
        left = 2*i + 1
        right = 2*i + 2
        smallest = i
        if left < len(self) and self._repr[left] < self._repr[smallest]:
            smallest = left
        if right < len(self) and self._repr[right] < self._repr[smallest]:
            smallest = right
        if smallest != i:
            self._repr[i], self._repr[smallest] = self._repr[smallest], self._repr[i]
            self._bubble_down(smallest)
        return

    def _bubble_up(self, i=None):
        if i is None:
            i = len(self) - 1
        if i >= len(self):
            raise IndexError
        parent = self._index_parent(i)
        if parent >= 0:
            if self._repr[i] < self._repr[parent]:
                self._repr[i], self._repr[parent] = self._repr[parent], self._repr[i]
                self._bubble_up(parent)
        return


class BinaryTree(Container):

    def __init__(self, data=None):
        super().__init__(data)

    def _make_lr_indices(self, index):
        return (2*index + 1, 2*index + 2)

    def _has_children(self, index):
        left, right = self._make_lr_indices(index)
        left_is_indexable = left < len(self)
        right_is_indexable = right < len(self)
        has_left = left_is_indexable and (self._repr[left] is not None)
        has_right = right_is_indexable and (self._repr[right] is not None)
        return (has_left, has_right)

    def size(self):
        return self.count()

    def min(self, i=0, return_index=False):
        """Brute-force find the smallest element in the tree. Works if the
        tree is not a binary search tree.
        """
        if not self._repr:
            raise Exception
        acc, index = self._repr[i], i
        left = 2*i + 1
        right = 2*i + 2
        has_left = left < len(self) and self._repr[left] is not None
        has_right = right < len(self) and self._repr[right] is not None
        if has_left:
            _acc, _index = self.min(left, True)
            if _acc < acc:
                acc = _acc
                index = _index
        if has_right:
            _acc, _index = self.min(right, True)
            if _acc < acc:
                acc = _acc
                index = _index
        if return_index:
            return acc, index
        return acc

    def max(self, i=0, return_index=False):
        """Brute-force find the largest element in the tree. Works if the tree
        is not a binary search tree.
        """
        if not self._repr:
            raise Exception
        acc, index = self._repr[i], i
        left = 2*i + 1
        right = 2*i + 2
        has_left = left < len(self) and self._repr[left] is not None
        has_right = right < len(self) and self._repr[right] is not None
        if has_left:
            _acc, _index = self.max(left, True)
            if _acc > acc:
                acc = _acc
                index = _index
        if has_right:
            _acc, _index = self.max(right, True)
            if _acc > acc:
                acc = _acc
                index = _index
        if return_index:
            return acc, index
        return acc

    def _pad(self, nlen):
        """Extend the underlying representation of the tree so that elements
        can be added into None nodes.
        """
        if nlen <= len(self._repr):
            return
        while len(self._repr) < nlen:
            self._repr.append(None)
        return

    def insert(self, element, i=0):
        """Insert into a binary search tree."""
        # grow the containter to ensure we can insert into it; when
        # combined with the fact that we match above when the current
        # node is none, it is no longer necessary to check has_left or
        # has_right
        if i >= len(self._repr):
            self._pad(i + 1)
        if self._repr[i] is None:
            self._repr[i] = element
            return
        left = 2*i + 1
        right = 2*i + 2
        if element < self._repr[i]:
            self.insert(element, left)
        else:
            self.insert(element, right)
        return

    def subtree(self, i=0):
        """Return the subtree starting at the given index."""
        if i >= len(self):
            return BinaryTree([])
        indices_q = Queue()
        indices_q.add(i)
        indices = []
        while not indices_q.is_empty():
            current_index = indices_q.remove()
            left, right = self._make_lr_indices(current_index)
            if left < len(self):
                indices_q.add(left)
            if right < len(self):
                indices_q.add(right)
            indices.append(current_index)
        elements = [self._repr[index] for index in indices]
        return BinaryTree(elements)

    # def _replace_node_in_parent(self, new_value=None, i=0):
    #     parent = self._index_parent(i)
    #     if parent >= 0:
    #         parent_left, parent_right = self._make_lr_indices(parent)
    #         parent_has_left, parent_has_right = self._has_children(parent)

    def delete(self, element, i=0, replacement_choice='predecessor'):
        """Delete an element from a binary search tree."""
        assert replacement_choice in ('predecessor', 'successor')
        left, right = self._make_lr_indices(i)
        has_left_child, has_right_child = self._has_children(i)
        if has_left_child and element < self._repr[i]:
            self.delete(element, left)
            return
        if has_right_child and element > self._repr[i]:
            self.delete(element, right)
            return
        assert element == self._repr[i]
        if has_left_child and has_right_child:
            # choose either in-order predecessor or successor as
            # replacement:
            # - predecessor: max of left subtree (rightmost child)
            # - successor: min of right subtree (leftmost child)
            if replacement_choice == 'predecessor':
                predecessor, predecessor_index = self.max(left, return_index=True)
                self._repr[i] = predecessor
                self._repr[predecessor_index] = None
                # what if the predecessor has children?
            elif replacement_choice == 'successor':
                successor, successor_index = self.min(right, return_index=True)
                self._repr[i] = successor
                self._repr[successor_index] = None
                # what if the successor has children?
        elif has_left_child:
            self._repr[i] = self._repr[left]
            self._repr[left] = None
        elif has_right_child:
            self._repr[i] = self._repr[right]
            self._repr[right] = None
        else:
            self._repr[i] = None
        return

    def is_binary_search_tree(self, i=0):
        # base case: going past the length of the array means we
        # haven't failed, so must be a BST
        if i >= len(self):
            return True
        left = 2*i + 1
        right = 2*i + 2
        has_left = left < len(self) and self._repr[left] is not None
        has_right = right < len(self) and self._repr[right] is not None
        if has_left and (not self.max(left) <= self._repr[i]):
            return False
        if has_right and (not self._repr[i] < self.min(right)):
            return False
        return self.is_binary_search_tree(left) \
            and self.is_binary_search_tree(right)

    def search_recursively(self, value, i=0):
        if self._repr[i] == value:
            return i
        left = 2*i + 1
        right = 2*i + 2
        has_left = left < len(self) and self._repr[left] is not None
        has_right = right < len(self) and self._repr[right] is not None
        if has_left and value < self._repr[i]:
            return self.search_recursively(value, left)
        elif has_right and value > self._repr[i]:
            return self.search_recursively(value, right)
        else:
            return None

    def search_iteratively(self, value, i=0):
        current_node = i
        while current_node is not None:
            if value == self._repr[current_node]:
                return current_node
            left = 2*current_node + 1
            right = 2*current_node + 2
            has_left = left < len(self) and self._repr[left] is not None
            has_right = right < len(self) and self._repr[right] is not None
            if has_left and value < self._repr[current_node]:
                current_node = left
            elif has_right and value > self._repr[current_node]:
                current_node = right
            else:
                current_node = None
        return current_node


def test_minheap_extract():
    data_start = [2, 50, 23, 88, 90, 32, 74, 80]
    data_ref = [23, 50, 32, 88, 90, 80, 74]
    heap = MinHeap(data_start)
    val = heap.extract()
    assert val == 2
    assert heap._repr == data_ref
    heap_ref = MinHeap(data_ref)
    assert heap == heap_ref
    return True


def test_minheap_insert():
    data_start = [4, 50, 7, 55, 90, 87]
    data_ref = [2, 50, 4, 55, 90, 87, 7]
    heap = MinHeap(data_start)
    heap.insert(2)
    assert heap._repr == data_ref
    heap_ref = MinHeap(data_ref)
    assert heap == heap_ref
    return True


complete_1 = BinaryTree([4])
complete_2 = BinaryTree([4, 2])
complete_3 = BinaryTree([10, 20, 30])
complete_4 = BinaryTree([10, 20, 30, 40])
is_bst = BinaryTree([8, 4, 10, 2, 6, 9])
is_not_bst = BinaryTree([8, 4, 10, 2, 12, 9])
bst_small_1 = BinaryTree([4, 2])
bst_small_2 = BinaryTree([4, 2, 6])

is_bst_2 =      BinaryTree([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, None, None, 13, None])
is_not_bst_2 =  BinaryTree([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, None, None, None, 13])
is_bst_3 =      BinaryTree([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, None, None, 13, None, None, None, None, None, None, 5])
is_not_bst_3 =  BinaryTree([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, None, None, 13, None, None, None, None, None, 5])
is_not2_bst_3 = BinaryTree([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, None, None, 13, None, None, None, None, None, None, None, 5])

bst_big = BinaryTree([
    8,
    3, 10,
    1, 6, None, 14,
    None, None, 4, 7, None, None, 13, 19,
    None, None, None, None, None, None, None, None, None, None, None, None, 12, None, 15, 20,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 11, None, None, None, None, None, None, None,
])


def test_binary_tree_size():
    tests = [
        (complete_1, 1),
        (complete_2, 2),
        (complete_3, 3),
        (complete_4, 4),
        (is_bst, 6),
        (is_not_bst, 6),
        (bst_small_1, 2),
        (bst_small_2, 3),
    ]
    for (tree, outcome) in tests:
        assert tree.size() == outcome
    return True


def test_binary_tree_min():
    tests = [
        (is_bst, 2),
        (is_not_bst, 2),
        (bst_small_1, 2),
        (bst_small_2, 2),
        (is_bst_2, 1),
        (is_bst_3, 1),
    ]
    for (tree, outcome) in tests:
        assert tree.min() == outcome
    tests = [
        (is_bst, (2, 3)),
        (is_not_bst, (2, 3)),
        (bst_small_1, (2, 1)),
        (bst_small_2, (2, 1)),
        (is_bst_2, (1, 3)),
        (is_bst_3, (1, 3)),
    ]
    for (tree, outcome) in tests:
        assert tree.min(return_index=True) == outcome
    return True


def test_binary_tree_max():
    tests = [
        (is_bst, 10),
        (is_not_bst, 12),
        (bst_small_1, 4),
        (bst_small_2, 6),
        (is_bst_2, 14),
        (is_bst_3, 14),
    ]
    for (tree, outcome) in tests:
        assert tree.max() == outcome
    tests = [
        (is_bst, (10, 2)),
        (is_not_bst, (12, 4)),
        (bst_small_1, (4, 0)),
        (bst_small_2, (6, 2)),
        (is_bst_2, (14, 6)),
        (is_bst_3, (14, 6)),
    ]
    for (tree, outcome) in tests:
        assert tree.max(return_index=True) == outcome
    return True


def test_binary_tree_insert():
    _complete_1 = BinaryTree([])
    _complete_1.insert(4)
    assert _complete_1 == complete_1
    _complete_2 = BinaryTree(complete_1._repr.copy())
    _complete_2.insert(2)
    assert _complete_2 == complete_2
    _is_bst_3 = BinaryTree(is_bst_2._repr.copy())
    _is_bst_3.insert(5)
    assert _is_bst_3 == is_bst_3
    return True


t = BinaryTree([3, 1, 6, None, None, 4, 7, None, None, None, None, None, 5, None, None])
u = BinaryTree([6, 4, 7, None, 5, None, None])
v = BinaryTree([3, 1, 6, None, None, 4, 7])
w = BinaryTree([10, None, 14, None, None, 13, None])


def test_binary_tree_subtree():
    assert t.is_binary_search_tree()
    _u = t.subtree(2)
    assert _u == u
    _v = is_bst_2.subtree(1)
    assert _v.is_binary_search_tree()
    assert _v == v
    _w = is_bst_2.subtree(2)
    assert _w.is_binary_search_tree()
    assert _w == w
    return True


def test_binary_tree_replace_node_in_parent():
    return True


def test_binary_search_tree_delete():
    _complete_1 = BinaryTree(complete_1._repr)
    _complete_1.delete(4)
    assert _complete_1 == BinaryTree([None])
    _is_bst_2 = BinaryTree(is_bst_2._repr)
    _is_bst_2.delete(8, replacement_choice='predecessor')
    assert _is_bst_2.is_binary_search_tree()
    assert _is_bst_2 == BinaryTree([7, 3, 10, 1, 6, None, 14, None, None, 4, None, None, None, 13, None])
    _is_bst_2 = BinaryTree(is_bst_2._repr)
    _is_bst_2.delete(8, replacement_choice='successor')
    assert _is_bst_2.is_binary_search_tree()
    assert _is_bst_2 == BinaryTree([10, 3, 14, 1, 6, 13, None, None, None, 4, 7, None, None, None, None])
    return True


def test_is_binary_search_tree():
    tests = [
        (complete_1, True),
        (complete_2, True),
        (complete_3, False),
        (complete_4, False),
        (bst_small_1, True),
        (bst_small_2, True),
        (is_bst, True),
        (is_not_bst, False),
        (is_bst_2, True),
        (is_not_bst_2, False),
        (is_bst_3, True),
        (is_not_bst_3, False),
        (is_not2_bst_3, False),
        (bst_big, True),
    ]
    for (tree, outcome) in tests:
        assert tree.is_binary_search_tree() == outcome
    return True


def test_binary_tree_search_recursively():
    tests = {
        4: [
            (complete_1, 0),
            (complete_2, 0),
            (complete_3, None),
            (complete_4, None),
            (is_bst, 1),
            # (is_not_bst, 1),
            (bst_small_1, 0),
            (bst_small_2, 0),
            (is_bst_2, 9),
            # (is_not_bst_2, 9),
        ],
        13: [
            (complete_1, None),
            (complete_2, None),
            (complete_3, None),
            (complete_4, None),
            (is_bst, None),
            # (is_not_bst, None),
            (bst_small_1, None),
            (bst_small_2, None),
            (is_bst_2, 13),
            # (is_not_bst_2, 14),
        ],
    }
    for value in tests:
        for (tree, outcome) in tests[value]:
            assert tree.search_recursively(value) == outcome
    return True


def test_binary_tree_search_iteratively():
    tests = {
        4: [
            (complete_1, 0),
            (complete_2, 0),
            (complete_3, None),
            (complete_4, None),
            (is_bst, 1),
            # (is_not_bst, 1),
            (bst_small_1, 0),
            (bst_small_2, 0),
            (is_bst_2, 9),
            # (is_not_bst_2, 9),
        ],
        13: [
            (complete_1, None),
            (complete_2, None),
            (complete_3, None),
            (complete_4, None),
            (is_bst, None),
            # (is_not_bst, None),
            (bst_small_1, None),
            (bst_small_2, None),
            (is_bst_2, 13),
            # (is_not_bst_2, 14),
        ],
    }
    for value in tests:
        for (tree, outcome) in tests[value]:
            assert tree.search_iteratively(value) == outcome
    return True


if __name__ == '__main__':
    test_minheap_extract()
    test_minheap_insert()
    test_binary_tree_size()
    test_binary_tree_min()
    test_binary_tree_max()
    test_binary_tree_insert()
    test_binary_tree_subtree()
    test_binary_tree_replace_node_in_parent()
    test_binary_tree_delete()
    test_is_binary_search_tree()
    test_binary_tree_search_recursively()
    test_binary_tree_search_iteratively()
