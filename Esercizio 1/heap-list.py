class PriorityQueueHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def max_heapify(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.heap) and self.heap[left] < self.heap[index]:
            max_node = left
        else:
            max_node = index
        if right < len(self.heap) and self.heap[left] < self.heap[index]:
            max_node=right
        if max_node != index:
            self.max_heapify(max_node)

    def increase_value(self, index, value):
        if value < self.heap[index]:

        self.heap[index] = value
        self.max_heapify(index)

    def insert(self, value):
        self.heap[len(self.heap)-1]=value
        self.max_heapify(len(self.heap) - 1)

    def find_min(self):
        if self.is_empty():
            return None
        index = len(self.heap)//2+1
        min_node = self.heap[index]
        while index+1 < len(self.heap):
            if min_node > self.heap[index]:
                min_node = self.heap[index]
        return min_node

    def heap_max(self):
        if not self.heap:
            return None
        return self.heap[0]

    def heap_min(self):
        if not self.heap:
            return None
        min_ind=self.heap.find_min()
        min_node=self.heap[min_ind]
        return min_node

    def extract_max(self):
        if not self.heap:
            return None
        max_node = self.heap[0]
        if len(self.heap) == 1:
            self.heap.pop()
            return max_node
        # Sposta l'ultimo elemento in cima e rimuovi la radice
        self.heap[0] = self.heap[len(self.heap)-1]
        self.heap.pop(len(self.heap) - 1)
        self.max_heapify(self.heap[0])
        return max_node

    def extract_min(self):
        if not self.heap:
            return None
        min_node = self.heap[0]
        if len(self.heap) == 1:
            self.heap.pop()
            return min_node
        min_ind=self.heap.find_min()
        min_node = self.heap[min_ind]
        self.heap[min_ind]=self.heap[len(self.heap)-1]
        self.heap.pop(len(self.heap) - 1)
        self.max_heapify(min_ind)
        return min_node