class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def __repr__(self):
        return f"Node({self.val} {self.children})"


class Index:
    def __init__(self, i):
        self.idx = i

    def increment(self):
        self.idx += 1

class Codec:

    def serialize(self, root):

        def helper(root, identity, res, parentIdx):
            if not root:
                return

            res.append(chr(identity.idx + 48))
            res.append(chr(root.val + 48))
            res.append(chr(parentIdx + 48) if parentIdx else 'N')

            parentIdx = identity.idx
            for child in root.children if root.children else []:
                identity.increment()
                helper(child, identity, res, parentIdx)

        if not root:
            return ""

        res = []
        helper(root, Index(1), res, None)

        return ''.join(res)


    def deserialize(self, data):

        def helper(data):

            nodesAndParents = {}

            for i in range(0, len(data), 3):
                idx = ord(data[i]) - 48
                val = ord(data[i + 1]) - 48
                parentIdx = ord(data[i + 2]) - 48
                nodesAndParents[idx] = (parentIdx, Node(val, []))

            for i in range(3, len(data), 3):
                idx = ord(data[i]) - 48
                node = nodesAndParents[idx][1]

                parentIdx = ord(data[i + 2]) - 48
                parentNode = nodesAndParents[parentIdx][1]
                parentNode.children.append(node)


            return nodesAndParents[ord(data[0]) - 48][1]

        if not data:
            return None

        return helper(data)


class Codec1:

    def serialize(self, root):

        def helper(root, res):
            if not root:
                return

            res.append(chr(root.val + 48))
            size = len(root.children) if root.children else 0
            res.append(chr(size + 48))
            for i in range(size):
                helper(root.children[i], res)


        res = []
        helper(root, res)
        return ''.join(res)


    def deserialize(self, data):

        def helper(data, index):
            if index.idx == len(data):
                return None

            node = Node(ord(data[index.idx]) - 48, [])
            index.increment()
            size = ord(data[index.idx]) - 48
            for i in range(size):
                index.increment()
                node.children.append(helper(data, index))

            return node

        if not data:
            return None

        return helper(data, Index(0))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    root = Node(11, [Node(33, [Node(55), Node(6666)]), Node(22), Node(30)])
    print(root)
    codec = Codec()
    str = codec.serialize(root)
    print(str)

    tree = codec.deserialize(str)
    print(tree)

    codec1 = Codec1()
    str = codec1.serialize(root)
    print(str)

    tree = codec1.deserialize(str)
    print(tree)