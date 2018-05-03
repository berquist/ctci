from collections import namedtuple

from ch4 import Queue
from ch4_common import Container


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


# this is the minimum spanning tree example from Wikipedia
mst_base_mat = [
    [0, 3, 0, 6, 0, 0, 0, 0, 0, 9],
    [3, 0, 2, 4, 0, 0, 0, 0, 9, 9],
    [0, 2, 0, 2, 9, 0, 0, 0, 8, 0],
    [6, 4, 2, 0, 9, 0, 0, 0, 0, 0],
    [0, 0, 9, 9, 0, 4, 5, 0, 7, 0],
    [0, 0, 0, 0, 4, 0, 1, 4, 0, 0],
    [0, 0, 0, 0, 5, 1, 0, 3, 9, 0],
    [0, 0, 0, 0, 0, 4, 3, 0, 10, 18],
    [0, 9, 8, 0, 7, 0, 9, 10, 0, 8],
    [9, 9, 0, 0, 0, 0, 0, 18, 8, 0],
]

mst_base_list = {
}

mst_base_edges = [
    (0, 1, 3),
    (0, 3, 6),
    (0, 9, 9),
    (1, 0, 3),
    (1, 2, 2),
    (1, 3, 4),
    (1, 8, 9),
    (1, 9, 9),
    (2, 1, 2),
    (2, 3, 2),
    (2, 4, 9),
    (2, 8, 8),
    (3, 0, 6),
    (3, 1, 4),
    (3, 2, 2),
    (3, 4, 9),
    (4, 2, 9),
    (4, 3, 9),
    (4, 5, 4),
    (4, 6, 5),
    (4, 8, 7),
    (5, 4, 4),
    (5, 6, 1),
    (5, 7, 4),
    (6, 4, 5),
    (6, 5, 1),
    (6, 7, 3),
    (6, 8, 9),
    (7, 5, 4),
    (7, 6, 3),
    (7, 8, 10),
    (7, 9, 18),
    (8, 1, 9),
    (8, 2, 8),
    (8, 4, 7),
    (8, 6, 9),
    (8, 7, 10),
    (8, 9, 8),
    (9, 0, 9),
    (9, 1, 9),
    (9, 7, 18),
    (9, 8, 8),
]

Edge = namedtuple('Edge', ['vertices', 'weight'])

# mst_result = {
#     Edge({0, 1}, 3),
#     Edge({1, 2}, 2),
#     Edge({2, 3}, 2),
#     Edge({2, 8}, 8),
#     Edge({8, 9}, 8),
#     Edge({8, 4}, 7),
#     Edge({4, 5}, 4),
#     Edge({5, 6}, 1),
#     Edge({6, 7}, 3),
# }

def boruvkas_algorithm():
    """
     Input: A graph G whose edges have distinct weights
     Initialize a forest F to be a set of one-vertex trees, one for each vertex of the graph.
     While F has more than one component:
       Find the connected components of F and label each vertex of G by its component
       Initialize the cheapest edge for each component to "None"
       For each edge uv of G:
         If u and v have different component labels:
           If uv is cheaper than the cheapest edge for the component of u:
             Set uv as the cheapest edge for the component of u
           If uv is cheaper than the cheapest edge for the component of v:
             Set uv as the cheapest edge for the component of v
        For each component whose cheapest edge is not "None":
          Add its cheapest edge to F
      Output: F is the minimum spanning forest of G.
    """
    # return msf

# class Graph(object):

#     def __init__(self, nodes=None):

#         if nodes is None:
#             self.nodes = []
#         else:
#             assert isinstance(nodes, (set, list, tuple, np.ndarray, ))
#             self.nodes = nodes


# def adjacency_list_to_matrix(graph):
#     assert isinstance(graph, Graph)
#     dim = len(graph.nodes)
#     adjmat = np.zeros(shape=(dim, dim), dtype=int)
#     for node in graph.nodes:
#         # assume it's an int, otherwise will need to map string to a
#         # unique id
#         idx_from = node.name
#         for (idex_to, weight) in node.children:
#             adjmat[idx_from][idx_to] = weight
#     return adjmat


# def adjacency_matrix_to_list(adjmat, data=None):
#     if data is not None:
#         assert isinstance(data, (set, list, tuple, np.ndarray, ))
#     assert isinstance(adjmat, (list, tuple, np.ndarray, ))
#     dim = len(adjmat)
#     assert dim > 0
#     assert len(adjmat[0]) == dim
#     nodes = []
#     for idx_from in range(dim):
#         children
#         if data is not None:
#             element = data[idx_from]
#         else:
#             element = None
#         node = Node(data=element, name=idx_from, children=children)
#         nodes.append(node)
#     return Graph(nodes)


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
    test_adjacency_matrix()
    test_is_path()
    test_adjacency_list()
