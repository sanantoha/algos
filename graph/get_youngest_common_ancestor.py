
# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


class AncestralTree(AncestralTree):
    def addDescendants(self, *descendants):
        for descendant in descendants:
            descendant.ancestor = self


def new_trees():
    ancestralTrees = {}
    for letter in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        ancestralTrees[letter] = AncestralTree(letter)
    return ancestralTrees


# O(h) time | O(1) space
def get_youngest_common_ancestor(top_ancestor, descendant_one, descendant_two):

    curr_one = descendant_one
    curr_two = descendant_two

    while curr_one != curr_two:
        curr_one = curr_one.ancestor if curr_one.ancestor is not None else descendant_two
        curr_two = curr_two.ancestor if curr_two.ancestor is not None else descendant_one

    return curr_one


if __name__ == '__main__':
    trees = new_trees()
    trees["A"].addDescendants(trees["B"], trees["C"])
    trees["B"].addDescendants(trees["D"], trees["E"])
    trees["D"].addDescendants(trees["H"], trees["I"])
    trees["C"].addDescendants(trees["F"], trees["G"])

    yca = get_youngest_common_ancestor(trees["A"], trees["E"], trees["I"])
    assert yca == trees["B"]
