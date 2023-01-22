
class UnionFind:
    def __init__(self):
        self.parents = {}
        self.ranks = {}

    # O(1) time | O(1) space
    def createSet(self, value):
        self.parents[value] = value
        self.ranks[value] = 0

    # O(1) time | O(1) space - approximate O(1) for both time and space complexity
    def find(self, value):
        if value not in self.parents:
            return None

        if self.parents[value] != value:
            self.parents[value] = self.find(self.parents[value])

        return self.parents[value]

    # O(1) time | O(1) space - approximate O(1) for both time and space complexity
    def union(self, valueOne, valueTwo):
        if valueOne not in self.parents or valueTwo not in self.parents:
            return

        pOne = self.find(valueOne)
        pTwo = self.find(valueTwo)

        if self.ranks[pOne] < self.ranks[pTwo]:
            self.parents[pOne] = pTwo
        elif self.ranks[pOne] > self.ranks[pTwo]:
            self.parents[pTwo] = pOne
        else:
            self.parents[pTwo] = pOne
            self.ranks[pOne] += 1


if __name__ == '__main__':
    unionFind = UnionFind()
    assert unionFind.find(1) == None
    unionFind.createSet(1)
    assert unionFind.find(1) == 1
    unionFind.createSet(5)
    assert unionFind.find(1) == 1
    assert unionFind.find(5) == 5
    unionFind.union(5, 1)
    assert unionFind.find(5) == unionFind.find(1)