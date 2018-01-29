import math


class _Node(object):

    def __init__(self, data=None):
        self.data = data
        self.visited = False
        self.marked = False

    def visit(self):
        print(self.data)
        self.visited = True
        return self.data


class Node(_Node):

    def __init__(self, data=None):

        super().__init__(data)

        self.children = []


class BinaryNode(_Node):

    def __init__(self, data=None):

        super().__init__(data)

        self.left = None
        self.right = None

    def size(self):
        """Calculate the size of the tree."""
        _size = 1 if self.data is not None else 0
        if self.left is not None:
            _size += self.left.size()
        if self.right is not None:
            _size += self.right.size()
        return _size

    def min(self):
        """Brute-force find the smallest element in the tree. Works if the
        tree is not a binary search tree.
        """
        if self.data is None:
            # TypeError?
            raise Exception
        _min = self.data
        if self.left is not None:
            _min = min(_min, self.left.min())
        if self.right is not None:
            _min = min(_min, self.right.min())
        return _min

    def max(self):
        """Brute-force find the largest element in the tree. Works if the tree
        is not a binary search tree.
        """
        if self.data is None:
            # TypeError?
            raise Exception
        _max = self.data
        if self.left is not None:
            _max = max(_max, self.left.max())
        if self.right is not None:
            _max = max(_max, self.right.max())
        return _max

    def insert_complete(self, element):
        """Insert the given element into the binary tree, ensuring that the
        tree is complete, by finding the rightmost (?) empty
        spot. Assume that the current tree is already complete.
        """
        if self.left is None:
            assert self.right is None
            self.left = type(self)(element)
        elif self.right is None:
            self.right = type(self)(element)
        else:
            assert (self.left is not None) and (self.right is not None)
            # lsize = self.left.size()
            rsize = self.right.size()
            # loglsize = math.log2(lsize + 1)
            logrsize = math.log2(rsize + 1)
            # lcomplete = (loglsize - math.floor(loglsize)) < 1.0e-10
            rcomplete = (logrsize - math.floor(logrsize)) < 1.0e-10
            # print(lsize, rsize, loglsize, logrsize, lcomplete, rcomplete)
            if not rcomplete:
                self.right.insert_complete(element)
            else:
                self.left.insert_complete(element)
        return


complete_1 = BinaryNode(4)

complete_2 = BinaryNode(4)
complete_2.left = BinaryNode(2)

complete_3 = BinaryNode(10)
complete_3.left = BinaryNode(20)
complete_3.right = BinaryNode(30)

complete_4 = BinaryNode(10)
complete_4.left = BinaryNode(20)
complete_4.left.left = BinaryNode(40)
complete_4.right = BinaryNode(30)

is_bst = BinaryNode(8)
is_bst.left = BinaryNode(4)
is_bst.left.left = BinaryNode(2)
is_bst.left.right = BinaryNode(6)
is_bst.right = BinaryNode(10)
is_bst.right.right = BinaryNode(20)

is_not_bst = BinaryNode(8)
is_not_bst.left = BinaryNode(4)
is_not_bst.left.left = BinaryNode(2)
is_not_bst.left.right = BinaryNode(12)
is_not_bst.right = BinaryNode(10)
is_not_bst.right.right = BinaryNode(20)

bst_small_1 = BinaryNode(4)
bst_small_1.left = BinaryNode(2)

bst_small_2 = BinaryNode(4)
bst_small_2.left = BinaryNode(2)
bst_small_2.right = BinaryNode(6)


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
        (is_bst, 20),
        (is_not_bst, 20),
        (bst_small_1, 4),
        (bst_small_2, 6),
    ]
    for (tree, outcome) in tests:
        assert tree.max() == outcome
    return True


binarynode_unfixed = BinaryNode(4)
binarynode_unfixed.left = BinaryNode(50)
binarynode_unfixed.left.left = BinaryNode(55)
binarynode_unfixed.left.right = BinaryNode(90)
binarynode_unfixed.right = BinaryNode(7)
binarynode_unfixed.right.left = BinaryNode(87)
binarynode_unfixed.right.right = BinaryNode(2)


def test_binary_tree_insert_complete():
    element = 27
    binarynode_unfixed.insert_complete(element)
    assert binarynode_unfixed.left.left.left is not None
    assert binarynode_unfixed.left.left.left.data == element
    element = 28
    binarynode_unfixed.insert_complete(element)
    assert binarynode_unfixed.left.left.right is not None
    assert binarynode_unfixed.left.left.right.data == element
    return True


def is_binary_search_tree(node):
    """Return True if the given binary tree is actually a binary search
    tree (BST), otherwise return False.
    """
    # base case: empty nodes are BSTs
    if node is None:
        return True
    has_left = node.left is not None
    has_right = node.right is not None
    if has_left and (not node.left.max() <= node.data):
        return False
    if has_right and (not node.data < node.right.min()):
        return False
    return is_binary_search_tree(node.left) \
        and is_binary_search_tree(node.right)


def test_is_binary_search_tree():
    assert is_binary_search_tree(bst_small_1)
    assert is_binary_search_tree(bst_small_2)
    assert is_binary_search_tree(is_bst)
    assert not is_binary_search_tree(is_not_bst)
    return True


# class Tree(object):

#     def __init__(self):

#         self.root = None

# class MinHeap(BinaryNode):

#     def __init__(self):
#         super().__init__()

#     def extract_min(self):
#         pass

#     def insert(self):
#         pass


# class Graph(object):

#     def __init__(self):

#         self.nodes = []


# def dfs(root):
#     if root.data is None:
#         return
#     root.visit()
#     for node in root.children:
#         if not node.visited:
#             dfs(node)
#     return


# def bfs(root):
#     from ch3 import Queue
#     queue = Queue()
#     # why not root.visit()?
#     root.marked = True
#     queue.add(root)
#     while not queue.is_empty():
#         r = queue.remove()
#         r.visit()
#         for node in r.adjacent:
#             if not node.marked:
#                 node.marked = True
#                 queue.add(node)
#     return


# def test_graph_1():
#     # digraph {
#     #   0 -> 1
#     #   1 -> 2
#     #   2 -> 0
#     #   3 -> 2
#     # }
#     edges = [
#         (0, 1),
#         (1, 2),
#         (2, 0),
#         (3, 2),
#     ]
#     parents = set([start for (start, end) in edges])
#     graph = Graph()
#     for edge_start, edge_end in edges:
#         start_node = Node(edge_start)
#         end_node = Node(edge_end)
#         start_node.children.append(end_node)
#         graph.nodes.append(start_node)
#     dfs(graph.nodes[0])
#     return True


# def test_graph_2():
#     # digraph {
#     #   0 -> 1
#     #   0 -> 4
#     #   0 -> 5
#     #   1 -> 3
#     #   1 -> 4
#     #   2 -> 1
#     #   3 -> 2
#     #   3 -> 4
#     # }
#     edges = [
#         (0, 1),
#         (0, 4),
#         (0, 5),
#         (1, 3),
#         (1, 4),
#         (2, 1),
#         (3, 2),
#         (3, 4),
#     ]
#     return True
