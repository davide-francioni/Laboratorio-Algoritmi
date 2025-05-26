class MaxHeap:
    def __init__(self, A):
        self.heap= [len(A)]
        print(len(self.heap))
        self.build_max_heap()

    def build_max_heap(self):
        #print(len(self.heap))
        i = (len(self.heap)/2)+1
        #print(i)
        while i >= 0:
            #print(self.heap[i])
            self.max_heapify(i)
            i -= 1

    def is_empty(self):
        return len(self.heap) == 0

    def max_heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(self.heap) and self.heap[left] > self.heap[i]:
            max_node = left
        else:
            max_node = i
        if right < len(self.heap) and self.heap[right] > self.heap[i]:
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
    def __init__(self, A):
        self.heap = [len(A)]
        self.build_max_heap()

    def build_max_heap(self):
        i = len(self.heap) // 2
        while i > 0:
            self.min_heapify(i)
            i -= 1

    def is_empty(self):
        return len(self.heap) == 0

    def min_heapify(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.heap) and self.heap[left] < self.heap[index]:
            min_node = left
        else:
            min_node = index
        if right < len(self.heap) and self.heap[right] < self.heap[index]:
            min_node = right
        if min_node != index:
            self.min_heapify(min_node)

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

if __name__ == '__main__':
    #genera un array casuale
    b=[5,6,9,12,3]
    arr = MaxHeap(b)
    for i in range(len(b)):
        x=arr.extract_max()
        print(x)
