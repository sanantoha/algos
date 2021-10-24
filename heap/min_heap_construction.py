
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    # O(n) time | O(1) space
    def buildHeap(self, array):
        end_idx = len(array) - 1
        for idx in reversed(range(len(array) // 2)):
            self.siftDown(idx, end_idx, array)

        return array

    # O(log(n)) time | O(1) space
    def siftDown(self, curr_idx, end_idx, heap):

        while curr_idx <= end_idx:
            l = self.left(curr_idx)
            r = self.right(curr_idx)

            min_idx = curr_idx
            if l <= end_idx and heap[l] < heap[min_idx]:
                min_idx = l
            if r <= end_idx and heap[r] < heap[min_idx]:
                min_idx = r

            if min_idx != curr_idx:
                self.swap(min_idx, curr_idx, heap)
                curr_idx = min_idx
            else:
                return

    # O(log(n)) time | O(1) space
    def siftUp(self, idx, heap):
        p = self.parent(idx)
        while p >= 0 and heap[p] > heap[idx]:
            self.swap(p, idx, heap)
            idx = p
            p = self.parent(idx)

    # O(1) time | O(1) space
    def peek(self):
        return self.heap[0]

    # O(log(n)) time | O(1) space
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        value = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return value

    # O(log(n)) time | O(1) space
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

    def left(self, i):
        return i * 2 + 1

    def right(self, i):
        return i * 2 + 2

    def parent(self, i):
        return (i - 1) // 2


def isMinHeapPropertySatisfied(array):
    for currentIdx in range(1, len(array)):
        parentIdx = (currentIdx - 1) // 2
        if array[parentIdx] > array[currentIdx]:
            return False
    return True


if __name__ == '__main__':
    minHeap = MinHeap([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41])
    minHeap.insert(76)
    assert isMinHeapPropertySatisfied(minHeap.heap)
    assert minHeap.peek() == -5
    assert minHeap.remove() == -5
    assert isMinHeapPropertySatisfied(minHeap.heap)
    assert minHeap.peek() == 2
    assert minHeap.remove() == 2
    assert isMinHeapPropertySatisfied(minHeap.heap)
    assert minHeap.peek() == 6
    minHeap.insert(87)
    assert isMinHeapPropertySatisfied(minHeap.heap)