import math
import operator


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
        parent = math.floor((i - 1) / 2)
        if parent >= 0:
            if self._repr[i] < self._repr[parent]:
                self._repr[i], self._repr[parent] = self._repr[parent], self._repr[i]
                self._bubble_up(parent)
        return


class BinaryTree(Container):

    def __init__(self, data=None):
        super().__init__(data)

    def size(self):
        return self.count()

    def min(self, i=0):
        """Brute-force find the smallest element in the tree. Works if the
        tree is not a binary search tree.
        """
        if not self._repr:
            raise Exception
        acc = self._repr[i]
        left = 2*i + 1
        right = 2*i + 2
        has_left = left < len(self) and self._repr[left] is not None
        has_right = right < len(self) and self._repr[right] is not None
        if has_left:
            acc = min(acc, self.min(left))
        if has_right:
            acc = min(acc, self.min(right))
        return acc

    def max(self, i=0):
        """Brute-force find the largest element in the tree. Works if the tree
        is not a binary search tree.
        """
        if not self._repr:
            raise Exception
        acc = self._repr[i]
        left = 2*i + 1
        right = 2*i + 2
        has_left = left < len(self) and self._repr[left] is not None
        has_right = right < len(self) and self._repr[right] is not None
        if has_left:
            acc = max(acc, self.max(left))
        if has_right:
            acc = max(acc, self.max(right))
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
    test_is_binary_search_tree()
    test_binary_tree_search_recursively()
    test_binary_tree_search_iteratively()
