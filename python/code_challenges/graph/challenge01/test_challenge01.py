import pytest
from challenge01 import Graph

def test_graph_breadth_first_search():
    g = Graph()
    node1 = g.add_node(1)
    node2 = g.add_node(2)
    node3 = g.add_node(3)
    node4 = g.add_node(4)
    g.add_edge(node1, node2)
    g.add_edge(node1, node3)
    g.add_edge(node2, node3)
    g.add_edge(node3, node4)
    actual = [1, 2, 3, 4]
    expected = g.breadth_first_search(node1)
    assert actual == expected


def test2_graph_breadth_first_search():
    g = Graph()
    node1 = g.add_node(1)
    node2 = g.add_node(2)
    node3 = g.add_node(3)
    node4 = g.add_node(4)
    g.add_edge(node1, node2)
    g.add_edge(node1, node3)
    g.add_edge(node2, node3)
    g.add_edge(node3, node4)
    actual = [3, 1, 2, 4]
    expected = g.breadth_first_search(node3)
    assert actual == expected

def test3_graph_breadth_first_search():
    g = Graph()
    node_a = g.add_node("a")
    node_b = g.add_node("b")
    node_c = g.add_node("c")
    node_d = g.add_node("d")
    node_e = g.add_node("e")
    node_f = g.add_node("f")
    node_g = g.add_node("g")
    g.add_edge(node_a, node_b)
    g.add_edge(node_a, node_c)
    g.add_edge(node_b, node_c)
    g.add_edge(node_c, node_d)
    g.add_edge(node_c, node_e)
    g.add_edge(node_d, node_f)
    g.add_edge(node_e, node_f)
    g.add_edge(node_f, node_g)
    actual = g.breadth_first_search(node_c)
    expected = ["c", "a", "b", "d", "e", "f", "g"]
    assert actual == expected

def test4_graph_breadth_first_search():
    g = Graph()
    node_a = g.add_node("a")
    node_b = g.add_node("b")
    node_c = g.add_node("c")
    node_d = g.add_node("d")
    node_e = g.add_node("e")
    node_f = g.add_node("f")
    node_g = g.add_node("g")
    g.add_edge(node_a, node_b)
    g.add_edge(node_a, node_c)
    g.add_edge(node_b, node_c)
    g.add_edge(node_c, node_d)
    g.add_edge(node_c, node_e)
    g.add_edge(node_d, node_f)
    g.add_edge(node_e, node_f)
    g.add_edge(node_f, node_g)
    actual = g.breadth_first_search(node_g)
    expected = ["g", "f", "d", "e", "c", "a", "b"]
    assert actual == expected