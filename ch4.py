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


def test_binary_tree_min():
    assert is_bst.min() == 2
    assert is_not_bst.min() == 2
    return True


def test_binary_tree_max():
    assert is_bst.max() == 20
    assert is_not_bst.max() == 20
    return True


# def is_binary_search_tree(node):
#     if node.left:
#         nmin = node.left.data
#     else:
#         nmin = None
#     if node.right:
#         nmax = node.right.data
#     else:
#         nmax = None
#     return _is_binary_search_tree(node, nmin, nmax)


# def _is_binary_search_tree(node, nmin, nmax):
#     """A binary search tree is a binary tree in which every node fits a
#     specific ordering property: all left descendents <= n < all right
#     descendents. This must be true for each node n.
#     """
#     # base case: the null and empty nodes are BSTs
#     if node is None:
#         return True
#     else:
#         assert isinstance(node, BinaryNode)
#     left, right, condmin, condmax = True, True, True, True
#     # check ordering
#     if node.left is not None:
#         left = (node.left.data <= node.data)
#     if node.right is not None:
#         right = (node.data < node.right.data)
#     # check BST condition: everything on the left must be smaller than
#     # nmax, and everything on the right must be larger than nmin
#     if nmin is not None:
#         condmin = nmin <= node.data
#     if nmax is not None:
#         condmax = node.data < nmax
#     print(node.data, nmin, condmin, nmax, condmax)
#     return left and right and condmin and condmax \
#         and _is_binary_search_tree(node.left, nmin, nmin) \
#         and _is_binary_search_tree(node.right, nmax, nmax)

# def test_is_binary_search_tree():
#     # create the binary search tree
#     is_bst = BinaryNode(8)
#     is_bst.left = BinaryNode(4)
#     is_bst.left.left = BinaryNode(2)
#     is_bst.left.right = BinaryNode(6)
#     is_bst.right = BinaryNode(10)
#     is_bst.right.right = BinaryNode(20)
#     # create the binary (not search) tree
#     is_not_bst = BinaryNode(8)
#     is_not_bst.left = BinaryNode(4)
#     is_not_bst.left.left = BinaryNode(2)
#     is_not_bst.left.right = BinaryNode(12)
#     is_not_bst.right = BinaryNode(10)
#     is_not_bst.right.right = BinaryNode(20)
#     assert is_binary_search_tree(is_bst)
#     assert not is_binary_search_tree(is_not_bst)
#     return True


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
