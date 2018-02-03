import math
import operator


class Container(object):

    def __init__(self, data=None):

        if data is not None:
            self._repr = data.copy()
        else:
            self._repr = []

    def __len__(self):
        if hasattr(self, '_len'):
            return self._len
        else:
            return len(self._repr)

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
        return len(self)

    def min(self, i=0):
        """Brute-force find the smallest element in the tree. Works if the
        tree is not a binary search tree.
        """
        if not self._repr:
            raise Exception
        acc = self._repr[i]
        left = 2*i + 1
        right = 2*i + 2
        if left < len(self):
            acc = min(acc, self.min(left))
        if right < len(self):
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
        if left < len(self):
            acc = max(acc, self.max(left))
        if right < len(self):
            acc = max(acc, self.max(right))
        return acc

    def insert_complete(self, element):
        self._repr.append(element)
        return

    def is_binary_search_tree(self, i=0):
        # base case: going past the length of the array means we
        # haven't failed, so must be a BST
        if i >= self.size():
            return True
        left = 2*i + 1
        right = 2*i + 2
        has_left = left < len(self)
        has_right = right < len(self)
        if has_left and (not self.max(left) <= self._repr[i]):
            return False
        if has_right and (not self._repr[i] < self.min(right)):
            return False
        return self.is_binary_search_tree(left) \
            and self.is_binary_search_tree(right)


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
    ]
    for (tree, outcome) in tests:
        assert tree.max() == outcome
    return True


def test_is_binary_search_tree():
    assert bst_small_1.is_binary_search_tree()
    assert bst_small_2.is_binary_search_tree()
    assert is_bst.is_binary_search_tree()
    assert not is_not_bst.is_binary_search_tree()
    return True


if __name__ == '__main__':
    test_minheap_extract()
    test_minheap_insert()
    test_binary_tree_size()
    test_binary_tree_min()
    test_binary_tree_max()
    test_is_binary_search_tree()
