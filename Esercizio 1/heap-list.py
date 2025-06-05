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

def max_heapify(arr, index):
    if len(arr) == 1:
        return
    left = 2 * index+1
    right = 2 * index+2
    if left < len(arr) and arr[left] > arr[index]:
        max_node = left
    else:
        max_node = index
    if right < len(arr) and arr[right] > arr[index]:
        max_node=right
    if max_node != index:
        app=arr[max_node]
        arr[max_node]=arr[index]
        arr[index]=app
        max_heapify(arr, max_node)

def build_max_heap(arr):
    if len(arr) == 0:
        return
    index = len(arr)-1
    while index >= (len(arr)/2)-1:
        max_heapify(arr, index)
        index -= 1

def increase_value(arr, index, value):
    if value < arr[index]:
        raise ValueError(f"{value} is lower than {value}")
    arr[index] = value
    while index > 1 and arr[(index/2)-1] < arr[index]:
        app=arr[(index/2)-1]
        arr[(index/2)-1]=arr[index]
        arr[index]=app
        index=(index/2)-1

def insert(arr, value):
    arr[len(arr)]=-1000000
    increase_value(arr, len(arr)-1, value)

def heap_max(arr):
    return arr[0]

def extract_max(arr):
    if len(arr) <1:
        raise ValueError(f"Empty array")
    max_node = arr[0]
    arr[0] = arr[len(arr)-1]
    arr.pop(len(arr) - 1)
    max_heapify(arr, 0)
    return max_node

if __name__ == '__main__':
    #genera un array casuale
    arr=[5,6,9,12,3]
    build_max_heap(arr)
    for i in range(len(arr)):
        x=extract_max(arr)
        print(x)
