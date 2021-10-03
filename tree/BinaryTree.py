class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.__dict__ == other.__dict__

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self

    def inverted_insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
        self.inverted_insert(values, i + 1)
        return self
