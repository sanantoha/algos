import pytest

from design.serialize_and_deserialize_n_ary_tree import Node, Codec, Codec1

TEST_CASES_SERIALIZE = [
    (Node(11, [Node(33, [Node(55), Node(6666)]), Node(22), Node(30)]), "1;N2Q13g24ᨺ25F16N1")
]

TEST_CASES_SERIALIZE1 = [
    (Node(11, [Node(33, [Node(55), Node(6666)]), Node(22), Node(30)]), ";3Q2g0ᨺ0F0N0")
]

TEST_CASES_DESERIALIZE = [
    ("1;N2Q13g24ᨺ25F16N1", Node(11, [Node(33, [Node(55, []), Node(6666, [])]), Node(22, []), Node(30, [])]))
]

TEST_CASES_DESERIALIZE1 = [
    (";3Q2g0ᨺ0F0N0", Node(11, [Node(33, [Node(55, []), Node(6666, [])]), Node(22, []), Node(30, [])]))
]

def nodes_equal(node1, node2):
    if node1 is node2:
        return True
    if node1.val != node2.val:
        return False
    if len(node1.children or []) != len(node2.children or []):
        return False
    # Recursively compare children in order
    for child1, child2 in zip(node1.children or [], node2.children or []):
        if not nodes_equal(child1, child2):
            return False
    return True

@pytest.fixture(scope="class")
def codec():
    return Codec()


@pytest.fixture(scope="class")
def codec1():
    return Codec1()

class TestCode:

    @pytest.mark.parametrize("node, exp", TEST_CASES_SERIALIZE)
    def test_serialize(self, codec, node, exp):
        print(node)
        str = codec.serialize(node)
        print(str)
        assert str == exp

    @pytest.mark.parametrize("input, exp", TEST_CASES_DESERIALIZE)
    def test_deserialize(self, codec, input, exp):
        node = codec.deserialize(input)
        print(node)
        assert nodes_equal(node, exp)


class TestCode1:

    @pytest.mark.parametrize("node, exp", TEST_CASES_SERIALIZE1)
    def test_serialize(self, codec1, node, exp):
        print(node)
        str = codec1.serialize(node)
        print(str)
        assert str == exp

    @pytest.mark.parametrize("input, exp", TEST_CASES_DESERIALIZE1)
    def test_deserialize(self, codec1, input, exp):
        node = codec1.deserialize(input)
        print(node)
        assert nodes_equal(node, exp)