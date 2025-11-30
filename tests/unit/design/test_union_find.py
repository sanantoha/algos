from design.union_find import UnionFind


def test_union_find():
    unionFind = UnionFind()
    assert unionFind.find(1) == None
    unionFind.createSet(1)
    assert unionFind.find(1) == 1
    unionFind.createSet(5)
    assert unionFind.find(1) == 1
    assert unionFind.find(5) == 5
    unionFind.union(5, 1)
    assert unionFind.find(5) == unionFind.find(1)