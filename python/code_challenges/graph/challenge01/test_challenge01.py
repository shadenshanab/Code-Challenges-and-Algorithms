import pytest
from challenge01 import Graph

def test_graph_breadth_first_search():
    # Create a graph and add some nodes and edges
    graph = Graph()
    a = graph.add_node('A')
    b = graph.add_node('B')
    c = graph.add_node('C')
    d = graph.add_node('D')
    e = graph.add_node('E')
    f = graph.add_node('F')
    g = graph.add_node('G')
    h = graph.add_node('H')
    i = graph.add_node('I')
    k = graph.add_node('K')
    graph.add_edge(a, c)
    graph.add_edge(a, e)
    graph.add_edge(a, b)
    graph.add_edge(e, f)
    graph.add_edge(e, g)
    graph.add_edge(e, d)
    graph.add_edge(f, i)
    graph.add_edge(h, k)
    graph.add_edge(b, d)
    graph.add_edge(g, h)
    graph.add_edge(i, k)
    graph.add_edge(c, f)
    graph.add_edge(f, h)

    # Test the breadth-first search function
    assert graph.breadth_first_search(c) == ['C', 'A', 'E', 'F', 'B', 'D', 'G', 'I', 'H', 'K']
    assert graph.breadth_first_search(a) == ['A', 'C', 'E', 'B', 'F', 'D', 'G', 'I', 'H', 'K']
    assert graph.breadth_first_search(h) == ['H', 'G', 'E', 'A', 'C', 'F', 'I', 'B', 'D', 'K']

def test_graph_add_node():
    # Test adding a node to the graph
    graph = Graph()
    node = graph.add_node('A')
    assert isinstance(node, Node)
    assert node.value == 'A'
    assert graph.adj_list == {node: []}

def test_graph_add_edge():
    # Test adding an edge to the graph
    graph = Graph()
    a = graph.add_node('A')
    b = graph.add_node('B')
    c = graph.add_node('C')
    graph.add_edge(a, b)
    assert graph.adj_list == {a: [Edge(b)], b: [Edge(a)]}
    graph.add_edge(a, c, weight=5)
    assert graph.adj_list == {a: [Edge(b), Edge(c, 5)], b: [Edge(a)], c: [Edge(a, 5)]}

def test_graph_add_invalid_edge():
    # Test adding an edge with a non-existent node
    graph = Graph()
    a = graph.add_node('A')
   
# Write your test here
