
# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # average: O(log(n)) time | O(log(n)) space
    # worst: O(n) time | O(n) space
    def insert_rec(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert_rec(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert_rec(value)
        return self

    # average: O(log(n)) time | O(1) space
    # worst: O(n) time | O(1) space
    def insert(self, value):
        curr = self

        while curr is not None:
            if value < curr.value:
                if curr.left is None:
                    curr.left = BST(value)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = BST(value)
                    break
                else:
                    curr = curr.right

        return self

    # average: O(log(n)) time | O(1) space
    # worst: O(n) time | O(1) space
    def contains(self, value):
        curr = self

        while curr is not None:
            if curr.value == value:
                return True
            elif curr.value < value:
                curr = curr.right
            else:
                curr = curr.left

        return False

    # average: O(log(n)) time | O(log(n)) space
    # worst: O(n) time | O(n) space
    def contains_rec(self, value):
        if self.value == value:
            return True
        elif self.value < value:
            if self.right is None:
                return False
            return self.right.contains_rec(value)
        else:
            if self.left is None:
                return False
            return self.left.contains_rec(value)

    # average: O(log(n)) time | O(1) space
    # worst: O(n) time | O(1) space
    def remove(self, value, parent_node=None):
        curr = self
        while curr is not None:
            if value < curr.value:
                parent_node = curr
                curr = curr.left
            elif value > curr.value:
                parent_node = curr
                curr = curr.right
            else:
                if curr.left is not None and curr.right is not None:
                    curr.value = curr.right.get_min_value()
                    curr.right.remove(curr.value, curr)
                elif parent_node is None:
                    if curr.left is not None:
                        curr.value = curr.left.value
                        curr.right = curr.left.right
                        curr.left = curr.left.left
                    elif curr.right is not None:
                        curr.value = curr.right.value
                        curr.left = curr.right.left
                        curr.right = curr.right.right
                    else:
                        pass

                elif parent_node.left == curr:
                    parent_node.left = curr.left if curr.left is not None else curr.right
                elif parent_node.right == curr:
                    parent_node.right = curr.left if curr.left is not None else curr.right
                break
        return self

    # average: O(log(n)) time | O(log(n)) space
    # worst: O(n) time | O(n) space
    def remove_rec(self, value, parent_node=None):
        if value < self.value:
            self.left.remove_rec(value, self)
        elif value > self.value:
            self.right.remove_rec(value, self)
        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.get_min_value()
                self.right.remove_rec(self.value, self)
            elif parent_node is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    pass

            elif parent_node.left == self:
                parent_node.left = self.left if self.left is not None else self.right
            elif parent_node.right == self:
                parent_node.right = self.left if self.left is not None else self.right

        return self

    def get_min_value(self):
        if self.left is None:
            return self.value
        else:
            return self.left.get_min_value()
