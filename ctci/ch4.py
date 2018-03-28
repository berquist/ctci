import math

import numpy as np

from ch3 import Queue
from ch4_array import Container


class _Node(object):

    def __init__(self, data=None):
        self.data = data
        self.visited = False
        self.marked = False

    def visit(self):
        print(self.data)
        if hasattr(self, 'children'):
            print([child.data for child in self.children])
        self.visited = True
        return self.data


class Node(_Node):

    def __init__(self, data=None, name=None, children=None):

        super().__init__(data)

        assert isinstance(name, (int, str, ))
        self.name = name

        if children is None:
            self.children = []
        else:
            assert isinstance(children, (set, list, tuple, ))
            self.children = children


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
    tree (BST), otherwise return False. (4.5)
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
    """Test for 4.5"""
    assert is_binary_search_tree(bst_small_1)
    assert is_binary_search_tree(bst_small_2)
    assert is_binary_search_tree(is_bst)
    assert not is_binary_search_tree(is_not_bst)
    return True


# class Tree(object):

#     def __init__(self):

#         self.root = None

class MinHeap(BinaryNode):

    def __init__(self, data=None):
        super().__init__(data)

    def extract_min(self):
        """Pop off the minimum (top) element of the heap, replace it with the
        rightmost element, then do swaps on the correct side of the heap to
        maintain minimum ordering.
        """
        pass

    def insert(self, element):
        """Insert the element at the rightmost position to ensure the heap is
        complete, then fix it by bubbling the new minimum up to the top.
        """
        self.insert_complete(element)
        # TODO should take an argument?
        self.bubble()

    def bubble(self):
        """Find the location of the minimum element (not necessarily at the
        top) and bubble it up to the top.
        """
        pass

minheap_unfixed = MinHeap(4)
minheap_unfixed.left = MinHeap(50)
minheap_unfixed.left.left = MinHeap(55)
minheap_unfixed.left.right = MinHeap(90)
minheap_unfixed.right = MinHeap(7)
minheap_unfixed.right.left = MinHeap(87)
minheap_unfixed.right.right = MinHeap(2)

minheap_fixed = MinHeap(2)
minheap_fixed.left = MinHeap(50)
minheap_fixed.left.left = MinHeap(55)
minheap_fixed.left.right = MinHeap(90)
minheap_fixed.right = MinHeap(4)
minheap_fixed.right.left = MinHeap(87)
minheap_fixed.right.right = MinHeap(7)


# def test_minheap_insert():
#     minheap_unfixed.insert(2)
#     assert minheap_unfixed.data == 2
#     return True


class AdjacencyMatrix(Container):

    def __init__(self, edges=None):

        self.edges = edges
        self._repr = []
        self._len = 0

        # edges must be a list of pairs
        if edges is not None:
            # figure out the dimensionality; can't just count total
            # number of elements, because there may be duplicates
            tmp1 = set(x[0] for x in edges)
            tmp2 = set(x[1] for x in edges)
            dim = len(tmp1.union(tmp2))
            # create placeholders
            self._repr = []
            for _ in range(dim):
                self._repr.append([0 for _ in range(dim)])
            self._form_adjacency_matrix(is_undirected=False)

    def _form_adjacency_matrix(self, is_undirected=False):
        if self.edges is None:
            raise Exception
        for (start, end, weight) in self.edges:
            self._repr[start][end] = weight
        if is_undirected:
            self._repr[end][start] = weight
        # todo
        self._len = len(self._repr[0])
        return

    # todo __setitem__

def test_adjacency_matrix():
    # pg 107, 1
    edges = [
        (0, 1, 1),
        (1, 2, 1),
        (2, 0, 1),
        (3, 2, 1),
    ]
    matrix = [[0, 1, 0, 0],
              [0, 0, 1, 0],
              [1, 0, 0, 0],
              [0, 0, 1, 0]]
    am_ref = AdjacencyMatrix()
    am_ref._repr = matrix
    am = AdjacencyMatrix(edges)
    assert am == am_ref
    # pg 107, 2
    edges = [
        (0, 1, 1),
        (0, 4, 1),
        (0, 5, 1),
        (1, 3, 1),
        (1, 4, 1),
        (2, 1, 1),
        (3, 2, 1),
        (3, 4, 1),
    ]
    matrix = [[0, 1, 0, 0, 1, 1],
              [0, 0, 0, 1, 1, 0],
              [0, 1, 0, 0, 0, 0],
              [0, 0, 1, 0, 1, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]]
    am_ref = AdjacencyMatrix()
    am_ref._repr = matrix
    am = AdjacencyMatrix(edges)
    assert am == am_ref
    return True


def is_path(start, end, graph):
    """Problem 4.1: Is there a path between the given start and end nodes
    of a directed graph?

    Implemented using breadth-first search on a graph implemented as
    an adjacency matrix.
    """
    if start == end:
        return True
    queue = Queue()
    graphlen = len(graph)
    marked = [False for _ in range(graphlen)]
    marked[start] = True
    queue.add(start)
    while not queue.is_empty():
        next_node = queue.remove()
        if next_node == end:
            return True
        neighbors = [i for (i, n) in zip(range(graphlen), graph[next_node])
                     if n == 1]
        for neighbor in neighbors:
            if not marked[neighbor]:
                marked[neighbor] = True
                queue.add(neighbor)
    return False


def test_is_path():
    edges = [
        (0, 1, 1),
        (1, 2, 1),
        (2, 0, 1),
        (2, 3, 1),
        (3, 2, 1),
        (4, 6, 1),
        (5, 4, 1),
        (6, 5, 1),
    ]
    graph = AdjacencyMatrix(edges)
    assert is_path(0, 0, graph)
    assert is_path(0, 1, graph)
    assert is_path(5, 6, graph)
    assert is_path(6, 4, graph)
    assert not is_path(6, 3, graph)
    assert not is_path(6, 0, graph)
    assert not is_path(0, 6, graph)
    return True


class AdjacencyList(Container):

    def __init__(self, edges=None):
        self.edges = edges
        self._repr = dict()
        # edges must be a list of pairs
        if edges is not None:
            self._form_adjacency_list(is_undirected=False)

    def _form_adjacency_list(self, is_undirected=False):
        if self.edges is None:
            raise Exception
        for (start, end, weight) in self.edges:
            if start not in self._repr:
                self._repr[start] = set()
            self._repr[start].add((end, weight))
        if is_undirected:
            if end not in self._repr:
                self._repr[end] = set()
            self._repr[end].add((start, weight))
        return


def test_adjacency_list():
    # pg 106, 1
    edges = [
        (0, 1, 1),
        (1, 2, 1),
        (2, 0, 1),
        (2, 3, 1),
        (3, 2, 1),
        (4, 6, 1),
        (5, 4, 1),
        (6, 5, 1),
    ]
    l = {
        0: {(1, 1)},
        1: {(2, 1)},
        2: {(0, 1), (3, 1)},
        3: {(2, 1)},
        4: {(6, 1)},
        5: {(4, 1)},
        6: {(5, 1)},
    }
    al_ref = AdjacencyList()
    al_ref._repr = l
    al = AdjacencyList(edges)
    assert al == al_ref
    return True


class Graph(object):

    def __init__(self, nodes=None):

        if nodes is None:
            self.nodes = []
        else:
            assert isinstance(nodes, (set, list, tuple, np.ndarray, ))
            self.nodes = nodes


def adjacency_list_to_matrix(graph):
    assert isinstance(graph, Graph)
    dim = len(graph.nodes)
    adjmat = np.zeros(shape=(dim, dim), dtype=int)
    for node in graph.nodes:
        # assume it's an int, otherwise will need to map string to a
        # unique id
        idx_from = node.name
        for (idex_to, weight) in node.children:
            adjmat[idx_from][idx_to] = weight
    return adjmat


def adjacency_matrix_to_list(adjmat, data=None):
    if data is not None:
        assert isinstance(data, (set, list, tuple, np.ndarray, ))
    assert isinstance(adjmat, (list, tuple, np.ndarray, ))
    dim = len(adjmat)
    assert dim > 0
    assert len(adjmat[0]) == dim
    nodes = []
    for idx_from in range(dim):
        children
        if data is not None:
            element = data[idx_from]
        else:
            element = None
        node = Node(data=element, name=idx_from, children=children)
        nodes.append(node)
    return Graph(nodes)


# def test_adjacency_list_to_matrix():
#     return True


# def test_adjacency_matrix_to_list():
#     return True


# def dfs(root):
#     if root.data is None:
#         return
#     root.visit()
#     for node in root.children:
#         if not node.visited:
#             dfs(node)
#     return


# def bfs(root):
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
#     # edges = [
#     #     (0, 1),
#     #     (1, 2),
#     #     (2, 0),
#     #     (3, 2),
#     # ]
#     edges = [
#         (0, 1),
#         (1, 2),
#         (2, 0),
#         (2, 3),
#         (3, 2),
#         (4, 6),
#         (5, 4),
#         (6, 5),
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

if __name__ == '__main__':
    pass
