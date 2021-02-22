from collections import defaultdict

class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()

    def add_edge(self, frm, to):
        self.graph[frm].append(to)
        self.vertices.add(frm)
        self.vertices.add(to)

    def breadth_first(self):
        pass

    def depth_first(self):
        pass


def return_graph():
    """
    Returns the following graph.
    10---30---50
     |\   |   /
     | \  |  /
     |  \ |/
    20---40
    :return: DefaultDict of the graph.
    """
    G = Graph()
    G.add_edge(10, 30)
    G.add_edge(30, 10)
    G.add_edge(10, 20)
    G.add_edge(20, 10)
    G.add_edge(10, 40)
    G.add_edge(40, 10)
    G.add_edge(30, 40)
    G.add_edge(40, 30)
    G.add_edge(20, 40)
    G.add_edge(40, 20)
    G.add_edge(40, 50)
    G.add_edge(50, 40)
    return G

