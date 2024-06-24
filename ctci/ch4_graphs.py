"""There are two ways to represent (un)directed (a)cyclic graphs:
- adjacency matrix
- adjacency list
with variations of each, in particular regarding how weights are handled.
"""

from collections import namedtuple
from random import choice

import numpy as np
from ch3 import Queue
from ch4_common import Container


class AdjacencyMatrix(Container):
    """Represent a graph as a matrix. Matrix elements signify both
    connectivity and weight.
    """

    def __init__(self, edges=None, is_undirected=False):

        self.edges = edges
        self.is_undirected = is_undirected

        self._repr = []
        self._len = 0

        # edges must be a list of pairs
        if self.edges is not None:
            # figure out the dimensionality; can't just count total
            # number of elements, because there may be duplicates
            tmp1 = {x[0] for x in edges}
            tmp2 = {x[1] for x in edges}
            dim = max(tmp1.union(tmp2)) + 1
            # create placeholders
            self._repr = []
            for _ in range(dim):
                self._repr.append([0 for _ in range(dim)])
            self._form_adjacency_matrix(self.is_undirected)

    # todo __setitem__

    def _form_adjacency_matrix(self, is_undirected):
        """Form the adjacency matrix from a list of edges."""
        if self.edges is None:
            raise SyntaxError
        for (start, end, weight) in self.edges:
            self._repr[start][end] = weight
            if is_undirected:
                self._repr[end][start] = weight
        # todo
        self._len = len(self._repr[0])

    def vertices(self):
        return list(range(len(self)))

    def neighbors(self, u):
        # i -> counter for node id
        # n -> connectivity/weight from u to i
        # self[u] -> list of connectivities/weights from u to all other nodes
        return [i for (i, n) in zip(range(len(self)), self[u])
                if n >= 1]

    def distance(self, u, v):
        """Find the distance between vertices with labels u and v."""
        # TODO Does this handle direction properly?
        # alt = dist[u] + graph[u][v]
        return self._repr[u][v]


def test_adjacency_matrix():
    blank = AdjacencyMatrix()
    try:
        blank._form_adjacency_matrix(False)  # pylint: disable=protected-access
    except SyntaxError:
        pass
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
    am_ref._repr = matrix # pylint: disable=protected-access
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
    am_ref._repr = matrix # pylint: disable=protected-access
    am = AdjacencyMatrix(edges)
    assert am == am_ref


def is_path(start, end, graph):
    """Problem 4.1: Is there a path between the given start and end nodes
    of a directed graph?

    Implemented using breadth-first search.
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
        neighbors = graph.neighbors(next_node)
        for neighbor in neighbors:
            if not marked[neighbor]:
                marked[neighbor] = True
                queue.add(neighbor)
    return False


def test_is_path_matrix():
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


def min_distance(vertices, distances):
    """Given a collection of indices corresponding to (neighboring)
    vertices, and an indexable collection of distances to all
    vertices, return the index into the distance collection that
    matches the shortest distance.
    """
    # Randomly choose a starting point. Not sure if this matters or if
    # it can be tuple(vertices)[0].
    min_index = choice(tuple(vertices))
    min_distance = distances[min_index] # pylint: disable=redefined-outer-name
    for i in vertices:
        distance = distances[i]
        if distance < min_distance:
            min_distance = distance
            min_index = i
    return min_index


def test_min_distance():
    test_cases = [
        (
            {4, 2, 7, 5},
            [0, 1, 2, 3, 4, 5, 6, 7, 8],
            (2, ),
        ),
        (
            {4, 2, 7, 5},
            [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            (7, ),
        ),
        (
            {2, 3},
            {0: 0, 1: 3, 2: 8, 3: 8, 4: 1},
            (2, 3),
        ),
        (
            {2, 3},
            {0: 0, 1: 3, 2: 7, 3: 8, 4: 1},
            (2, ),
        ),
        # Should work with string labels as well.
        (
            {'b', 'c'},
            {'a': 0, 'b': 3, 'c': 7, 'd': 8, 'e': 1},
            ('b', ),
        ),
    ]
    for vertices, distances, min_index in test_cases:
        assert min_distance(vertices, distances) in min_index


# pylint: disable=invalid-name
def dijkstras_algorithm(graph, source):
    """This is the original version that does not use a minimum priority
    queue.
    """
    vertices = graph.vertices()
    Q = set()
    dist = dict()
    prev = dict()
    # Initalization
    for v in vertices:
        # Unknown distance from source to v
        dist[v] = np.inf
        # Previous node in optimal path from source
        prev[v] = None
        # All nodes initially in Q (unvisited nodes)
        Q.add(v)
    dist[source] = 0
    while Q:
        # Node with the least distance will be selected first
        u = min_distance(Q, dist)
        Q.remove(u)
        neighbors = graph.neighbors(u)
        for v in neighbors:
            alt = dist[u] + graph.distance(u, v)
            # A shorter path to v has been found
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    return dist, prev


def test_dijkstras_algorithm_matrix():
    # example taken from https://youtu.be/pVfj6mxhdMw
    edges = [
        (0, 1, 6),
        (0, 3, 1),
        (1, 0, 6),
        (1, 2, 5),
        (1, 3, 2),
        (1, 4, 2),
        (2, 1, 5),
        (3, 0, 1),
        (3, 1, 2),
        (3, 4, 1),
        (4, 1, 2),
        (4, 2, 5),
        (4, 3, 1),
    ]
    graph = AdjacencyMatrix(edges)
    # print(graph)
    dist, prev = dijkstras_algorithm(graph, 0)
    # print(dist)
    # print(prev)
    assert dist == {
        0: 0,
        1: 3,
        2: 7,
        3: 1,
        4: 2,
    }
    assert prev == {
        0: None,
        1: 3,
        2: 4,
        3: 0,
        4: 3,
    }

    edges = [
        # ('a', 'e', 1),
        # ('a', 'b', 3),
        # ('b', 'e', 4),
        # ('b', 'c', 5),
        # ('c', 'e', 6),
        # ('c', 'd', 2),
        # ('e', 'd', 7),
        (0, 4, 1),
        (0, 1, 3),
        (1, 4, 4),
        (1, 2, 5),
        (2, 4, 6),
        (2, 3, 2),
        (4, 3, 7),
    ]
    graph_undirected = AdjacencyMatrix(edges, True)
    # print(np.array(graph_undirected))
    graph_directed = AdjacencyMatrix(edges, False)
    # print(np.array(graph_directed))
    dist_undirected, prev_undirected = dijkstras_algorithm(graph_undirected, 0)
    dist_directed, prev_directed = dijkstras_algorithm(graph_directed, 0)
    assert dist_undirected == {
        0: 0,
        1: 3,
        2: 7,
        3: 8,
        4: 1,
    }
    assert dist_directed == {
        0: 0,
        1: 3,
        2: 8,
        3: 8,
        4: 1,
    }
    assert prev_undirected == {
        0: None,
        1: 0,
        2: 4,
        3: 4,
        4: 0,
    }
    assert prev_directed == {
        0: None,
        1: 0,
        2: 1,
        3: 4,
        4: 0,
    }


class AdjacencyList(Container):

    def __init__(self, edges=None, is_undirected=False):

        self.edges = edges
        self.is_undirected = is_undirected

        self._repr = dict()
        # edges must be a list of pairs
        if self.edges is not None:
            self._form_adjacency_list(is_undirected=self.is_undirected)

    def __getitem__(self, index, alt=None):
        return self._repr.get(index, alt)

    # todo __setitem__

    def _form_adjacency_list(self, is_undirected):
        if self.edges is None:
            raise SyntaxError
        for (start, end, weight) in self.edges:
            if start not in self._repr:
                self._repr[start] = set()
            self._repr[start].add((end, weight))
            if end not in self._repr:
                self._repr[end] = set()
            if is_undirected:
                self._repr[end].add((start, weight))

    def vertices(self):
        return list(self._repr.keys())

    def neighbors(self, u):
        # self[u] -> sparse list of (node id, weight) connected to u
        return [n for (n, _) in self[u]]

    def distance(self, u, v):
        """Find the distance between vertices with labels u and v."""
        dist = [node[1] for node in list(self[u])
                if node[0] == v]
        assert len(dist) == 1
        dist = dist[0]
        return dist


def test_adjacency_list():
    blank = AdjacencyList()
    try:
        blank._form_adjacency_list(False)  # pylint: disable=protected-access
    except SyntaxError:
        pass
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
    repr = {
        0: {(1, 1)},
        1: {(2, 1)},
        2: {(0, 1), (3, 1)},
        3: {(2, 1)},
        4: {(6, 1)},
        5: {(4, 1)},
        6: {(5, 1)},
    }
    al_ref = AdjacencyList()
    al_ref._repr = repr  # pylint: disable=protected-access
    al = AdjacencyList(edges)
    assert al == al_ref


def test_is_path_list():
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
    graph = AdjacencyList(edges)
    assert is_path(0, 0, graph)
    assert is_path(0, 1, graph)
    assert is_path(5, 6, graph)
    assert is_path(6, 4, graph)
    assert not is_path(6, 3, graph)
    assert not is_path(6, 0, graph)
    assert not is_path(0, 6, graph)


# this is the minimum spanning tree example from Wikipedia
MST_BASE_MAT = [
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

MST_BASE_LIST = {
}

MST_BASE_EDGES = [
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

# MST_RESULT = {
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
#     pass


# def test_adjacency_matrix_to_list():
#     pass


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

EDGES_CLAY_BIG = [
    ('A', 'J', 91),
    ('A', 'H', 86),
    ('A', 'B', 38),
    ('A', 'N', 37),
    ('A', 'L', 100),
    ('A', 'V', 64),
    ('A', 'S', 84),
    ('A', 'M', 9),
    ('A', 'W', 54),
    ('A', 'K', 46),
    ('B', 'J', 27),
    ('B', 'V', 93),
    ('B', 'H', 40),
    ('B', 'G', 49),
    ('B', 'F', 94),
    ('B', 'N', 95),
    ('B', 'C', 45),
    ('B', 'Z', 42),
    ('B', 'L', 15),
    ('C', 'Q', 14),
    ('C', 'W', 10),
    ('C', 'L', 87),
    ('C', 'R', 77),
    ('C', 'N', 92),
    ('C', 'S', 79),
    ('C', 'T', 3),
    ('C', 'D', 60),
    ('C', 'J', 43),
    ('D', 'P', 26),
    ('D', 'W', 12),
    ('D', 'K', 21),
    ('D', 'Q', 5),
    ('D', 'V', 75),
    ('D', 'T', 59),
    ('D', 'J', 2),
    ('D', 'R', 11),
    ('F', 'J', 63),
    ('F', 'X', 72),
    ('F', 'L', 88),
    ('F', 'G', 51),
    ('F', 'V', 61),
    ('F', 'P', 39),
    ('F', 'M', 69),
    ('F', 'W', 65),
    ('G', 'N', 76),
    ('G', 'X', 13),
    ('G', 'Z', 56),
    ('G', 'H', 82),
    ('G', 'Q', 32),
    ('G', 'W', 20),
    ('G', 'V', 18),
    ('H', 'Z', 74),
    ('H', 'P', 85),
    ('H', 'L', 62),
    ('H', 'M', 44),
    ('H', 'K', 25),
    ('H', 'J', 98),
    ('H', 'R', 19),
    ('J', 'V', 31),
    ('J', 'M', 50),
    ('J', 'S', 57),
    ('J', 'Q', 17),
    ('J', 'T', 22),
    ('J', 'P', 68),
    ('K', 'T', 67),
    ('K', 'L', 81),
    ('K', 'M', 55),
    ('K', 'P', 52),
    ('K', 'S', 83),
    ('K', 'X', 41),
    ('L', 'R', 36),
    ('L', 'N', 30),
    ('L', 'T', 53),
    ('L', 'S', 23),
    ('L', 'Q', 66),
    ('M', 'S', 6),
    ('M', 'Q', 29),
    ('M', 'N', 71),
    ('M', 'R', 8),
    ('M', 'T', 96),
    ('N', 'T', 16),
    ('N', 'R', 78),
    ('N', 'Q', 73),
    ('N', 'V', 24),
    ('P', 'Z', 28),
    ('P', 'W', 48),
    ('P', 'Q', 7),
    ('P', 'T', 47),
    ('Q', 'W', 99),
    ('Q', 'S', 1),
    ('Q', 'Z', 89),
    ('R', 'V', 70),
    ('R', 'X', 35),
    ('R', 'S', 33),
    ('S', 'T', 34),
    ('S', 'X', 90),
    ('T', 'X', 4),
    ('T', 'W', 58),
    ('V', 'X', 80),
    ('W', 'Z', 97),
]


def test_dijkstras_algorithm_list():
    graph_d = AdjacencyList(EDGES_CLAY_BIG, False)
    graph_u = AdjacencyList(EDGES_CLAY_BIG, True)
    dist_d, prev_d = dijkstras_algorithm(graph_d, 'M')
    dist_u, prev_u = dijkstras_algorithm(graph_u, 'M')
    assert dist_d['T'] == 40
    assert dist_u['T'] == 24
