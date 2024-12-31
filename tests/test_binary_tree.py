import pytest
import trees.binary_tree as bt


@pytest.fixture()
def single_node() -> bt.BinaryNode:
    return bt.BinaryNode(42)

@pytest.fixture()
def simple_tree() -> bt.BinaryNode:
    root = bt.BinaryNode("ROOT")
    root.add_left(bt.BinaryNode("LEFT"))
    root.add_right(bt.BinaryNode("RIGHT"))
    return root

@pytest.fixture()
def manning_sample_tree() -> dict[str, bt.BinaryNode]:
    root = bt.BinaryNode("Root")
    a_node = bt.BinaryNode("A")
    b_node = bt.BinaryNode("B")
    c_node = bt.BinaryNode("C")
    d_node = bt.BinaryNode("D")
    e_node = bt.BinaryNode("E")
    f_node = bt.BinaryNode("F")
    root.add_left(a_node).add_right(b_node)
    a_node.add_left(c_node).add_right(d_node)
    b_node.add_right(e_node)
    e_node.add_left(f_node)
    return {
        "root": root,
        "a": a_node,
        "b": b_node,
        "c": c_node,
        "d": d_node,
        "e": e_node,
        "f": f_node
    }

def test_leaf_node_to_string(single_node):
    assert str(single_node) == "42: None None"

def test_tree_of_nodes_to_string(simple_tree):
    assert str(simple_tree) == "ROOT: LEFT RIGHT"

def test_manning_sample_tree(manning_sample_tree):
    assert str(manning_sample_tree.get("root")) == "Root: A B"
    assert str(manning_sample_tree.get("a")) == "A: C D"
    assert str(manning_sample_tree.get("b")) == "B: None E"
    assert str(manning_sample_tree.get("c")) == "C: None None"
    assert str(manning_sample_tree.get("d")) == "D: None None"
    assert str(manning_sample_tree.get("e")) == "E: F None"
    assert str(manning_sample_tree.get("f")) == "F: None None"

