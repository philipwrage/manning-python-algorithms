import pytest
import trees.nary_tree as nt

def test_manning_tree():
    root = nt.NaryNode("Root")
    a_node = nt.NaryNode("A")
    b_node = nt.NaryNode("B")
    c_node = nt.NaryNode("C")
    root.add_child(a_node).add_child(b_node).add_child(c_node)
    d_node = nt.NaryNode("D")
    e_node = nt.NaryNode("E")
    a_node.add_child(d_node).add_child(e_node)
    f_node = nt.NaryNode("F")
    c_node.add_child(f_node)
    g_node = nt.NaryNode("G")
    d_node.add_child(g_node)
    h_node = nt.NaryNode("H")
    i_node = nt.NaryNode("I")
    f_node.add_child(h_node).add_child(i_node)
    assert str(root) == "Root: A B C"
    assert str(a_node) == "A: D E"
    assert str(b_node) == "B: "
    assert str(c_node) == "C: F"
    assert str(d_node) == "D: G"
    assert str(e_node) == "E: "
    assert str(f_node) == "F: H I"
    assert str(g_node) == "G: "
    assert str(h_node) == "H: "
    assert str(i_node) == "I: "

