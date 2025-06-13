import random

class HeapNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class MaxHeap:
    def __init__(self):
        self.root = None
        self.size = 0

    def max_heapify(self, node):
        if node.left is not None and node.left.value > node.value:
            max_node = node.left
        else:
            max_node = node

        if node.right is not None and node.right.value > max_node.value:
            max_node=node.right
        if max_node != node:
            self.swap_node(max_node, node)
            self.max_heapify(max_node)

    def find_path(self, i):
        if i==1:
            return self.root
        else:
            node = self.find_path(i//2)
            if i%2==0:
                return node.left
            else:
                return node.right

    def insert(self, value):
        new_node = HeapNode(value-1)
        self.size += 1
        if self.root is None:
            self.root = new_node
            self.increase_value(self.root, value)
            return
        parent = self.find_path(self.size//2)
        if self.size % 2 == 0:
            parent.left=new_node
        else:
            parent.right=new_node
        new_node.parent = parent
        self.increase_value(new_node, value)
        self.max_heapify(new_node)

    def increase_value(self, node, value):
        if value < node.value:
            raise ValueError(f"{value} is lower than {node.value}")
        node.value = value
        while node!=self.root and node.parent.value < node.value:
            self.swap_node(node, node.parent)
            node=node.parent

    def heap_max(self):
        if self.is_empty():
            return None
        return self.root.value

    def extract_max(self):
        if self.root is None:
            return None
        max_value = self.root.value
        if self.size == 1:
            self.root = None
            self.size = 0
            return max_value
        # Trova ultimo nodo (BFS tramite path binario)
        current = self.find_path(self.size)
        parent = current.parent
        # Sposta l'ultimo nodo alla radice
        self.swap_node(self.root, current)
        # Rimuove l'ultimo nodo
        if self.size % 2 == 0:
            parent.left = None
        else:
            parent.right = None
        self.size -= 1
        self.max_heapify(self.root)
        return max_value

    def is_empty(self):
        return self.size == 0

    def swap_node(self, a, b):
        a.value, b.value = b.value, a.value

    def get_random_node(self):
        if self.size == 0:
            return None
        i = random.randint(1, self.size)
        return self.find_path(i)

def genera_array_casuale(dimensione, minimo=0, massimo=100):
    return [random.randint(minimo, massimo) for _ in range(dimensione)]


if __name__ == '__main__':
    #genera un array casuale
    arr = genera_array_casuale(10)
    print(arr)

    heap=MaxHeap()
    i=0
    while i<len(arr):
        heap.insert(arr[i])
        i += 1
    i=0

    #heap.increase_value(heap.get_random_node(), 17)

    while i<len(arr):
        x=heap.heap_max()
        y=heap.extract_max()
        print(x,y)
        i += 1