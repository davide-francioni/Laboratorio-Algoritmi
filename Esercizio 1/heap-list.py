class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class MaxHeap:
    def __init__(self, A):
        self.heap = [len(A)]

    def buid_max_heap(self):
        for i in range(len(self.heap) - 1, -1, -1):
            self.max_heapify(i)


    def is_empty(self):
        return len(self.heap) == 0

    def max_heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(self.heap) and self.heap[left] < self.heap[i]:
            max_node = left
        else:
            max_node = i
        if right < len(self.heap) and self.heap[right] < self.heap[i]:
            max_node=right
        if max_node != i:
            self.max_heapify(max_node)

    def increase_value(self, index, value):
        if value < self.heap[index]:
            raise ValueError(f"{value} is lower than {value}")
        self.heap[index] = value
        while index > 0 and self.heap[(index//2)-1] < self.heap[index]:
            app=self.heap[(index//2)-1]
            self.heap[index//2-1]=self.heap[index]
            self.heap[index]=app
            index=index//2-1

    def insert(self, value):
        self.heap.append(value-1)
        self.increase_value(len(self.heap) - 1, value)

    def heap_max(self):
        if not self.heap:
            return None
        return self.heap[0]

    def extract_max(self):
        if not self.heap:
            return None
        max_node = self.heap[0]
        if len(self.heap) == 1:
            self.heap.pop()
            return max_node
        self.heap[0] = self.heap[len(self.heap)-1]
        self.heap.pop(len(self.heap) - 1)
        self.max_heapify(self.heap[0])
        return max_node

class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def min_heapify(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.heap) and self.heap[left] > self.heap[index]:
            max_node = left
        else:
            max_node = index
        if right < len(self.heap) and self.heap[right] > self.heap[index]:
            max_node = right
        if max_node != index:
            self.min_heapify(max_node)

    def decrease_value(self, index, value):
        if value > self.heap[index]:
            raise ValueError(f"{value} is greater than {value}")
        self.heap[index] = value
        while index > 0 and self.heap[(index // 2) - 1] > self.heap[index]:
            app = self.heap[(index // 2) - 1]
            self.heap[index // 2 - 1] = self.heap[index]
            self.heap[index] = app
            index = index // 2 - 1

    def insert(self, value):
        self.heap.append(value +1)
        self.decrease_value(len(self.heap) - 1, value)

    def heap_min(self):
        if not self.heap:
            return None
        return self.heap[0]

    def extract_min(self):
        if not self.heap:
            return None
        min_node = self.heap[0]
        if len(self.heap) == 1:
            self.heap.pop()
            return min_node
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap.pop(len(self.heap) - 1)
        self.min_heapify(self.heap[0])
        return min_node

