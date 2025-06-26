import random
import time

class HeapNode:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class MaxHeap:
    def __init__(self):
        self.root = None
        self.size = 0

    def max_heapify(self, node):
        if node.left is not None and node.left.priority > node.priority:
            max_node = node.left
        else:
            max_node = node
        if node.right is not None and node.right.priority > max_node.priority:
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

    def insert(self, priority, value):
        new_node = HeapNode(priority-1, value)
        self.size += 1
        if self.size == 1:
            self.root = new_node
            self.increase_priority(self.root, priority)
            return
        parent = self.find_path(self.size//2)
        if self.size % 2 == 0:
            parent.left=new_node
        else:
            parent.right=new_node
        new_node.parent = parent
        self.increase_priority(new_node, priority)

    def increase_priority(self, node, priority):
        if priority < node.priority:
            raise ValueError(f"{priority} is lower than {node.priority}")
        node.priority = priority
        while node.parent and node.parent.priority < node.priority:
            self.swap_node(node, node.parent)
            node = node.parent

    def list_max(self):
        if self.is_empty():
            return None
        return self.root.priority

    def extract_max(self):
        if self.root is None:
            return None
        max_priority = self.root.priority
        if self.size == 1:
            self.root = None
            self.size = 0
            return max_priority
        current = self.find_path(self.size)
        parent = current.parent
        self.swap_node(self.root, current)
        if parent.left==current:
            parent.left = None
        else:
            parent.right = None
        self.size -= 1
        self.max_heapify(self.root)
        return max_priority

    def is_empty(self):
        return self.size == 0

    def swap_node(self, a, b):
        a.priority, b.priority = b.priority, a.priority

    def get_random_node(self):
        if self.size == 0:
            return None
        i = random.randint(1, self.size)
        return self.find_path(i)

def genera_array_casuale(dimensione, minimo=0, massimo=100):
    return [random.randint(minimo, massimo) for _ in range(dimensione)]

def operations_times(n):
    arr = genera_array_casuale(n)
    pri = genera_array_casuale(n)
    print("Elementi da inserire nell'heap", arr)

    print("Creazione Coda di priorità con Heap...")
    start_time = time.time()

    heap = MaxHeap()
    i = 0
    while i < len(arr):
        heap.insert(pri[i], arr[i])
        i += 1

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Coda di priorità creata")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

    print("Inserimento dell'elemento 51 nel Heap...")
    start_time = time.time()

    heap.insert(51, 0)

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Elemento Inserito")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

    x = heap.get_random_node()
    y = x.priority
    print("Incremento:", y, "a", 101, "...")
    start_time = time.time()

    heap.increase_priority(x, 101)

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Incremento dell'elemento completato")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

    print("Estrazione dell'elemento massimo...")
    start_time = time.time()

    x = heap.extract_max()

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Estrazione di", x, "completata")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

    print("Stampa dell'elemento massimo...")
    start_time = time.time()

    x = heap.heap_max()

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Stampa di", x, "completata")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

def operation_best_list(A):
    arr = genera_array_casuale(100)
    print("Elementi da inserire nell'heap", arr)

    print("Creazione Coda di priorità con Heap...")
    start_time = time.time()

    heap = MaxHeap()
    i = 0
    while i < len(A):
        heap.insert(A[i], arr[i])
        i += 1

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Coda di priorità creata")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

    print("Inserimento dell'elemento 0 nel Heap...")
    start_time = time.time()

    heap.insert(0, 0)

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Elemento Inserito")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

    x = heap.get_random_node()
    y = x.priority
    print("Incremento:", y, "a", y+1, "...")
    start_time = time.time()

    heap.increase_priority(x, y+1)

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Incremento dell'elemento completato")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

    print("Estrazione dell'elemento massimo...")
    start_time = time.time()

    x = heap.extract_max()

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Estrazione di", x, "completata")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

    print("Stampa dell'elemento massimo...")
    start_time = time.time()

    x = heap.heap_max()

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Stampa di", x, "completata")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

def operation_worst_list(A):
    arr = genera_array_casuale(100)
    print("Elementi da inserire nell'heap", arr)

    print("Creazione Coda di priorità con Heap...")
    start_time = time.time()

    heap = MaxHeap()
    i = 0
    while i < len(A):
        heap.insert(A[i], arr[i])
        i += 1

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Coda di priorità creata")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

    print("Inserimento dell'elemento 101 nel Heap...")
    start_time = time.time()

    heap.insert(101, 0)

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Elemento Inserito")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

    x = heap.find_path(heap.size)
    y = x.priority
    print("Incremento:", y, "a", 102, "...")
    start_time = time.time()

    heap.increase_priority(x, 102)

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Incremento dell'elemento completato")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

    print("Estrazione dell'elemento massimo...")
    start_time = time.time()

    x = heap.extract_max()

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Estrazione di", x, "completata")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

    print("Stampa dell'elemento massimo...")
    start_time = time.time()

    x = heap.heap_max()

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Stampa di", x, "completata")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")



if __name__ == '__main__':
    for i in range(1, 4):
        print("Test", i, "con 10 elementi:")
        print(" ")
        operations_times(10)
    for i in range(1, 4):
        print("Test", i, "con 100 elementi:")
        print(" ")
        operations_times(100)
    for i in range(1, 4):
        print("Test", i, "con 1000 elementi:")
        print(" ")
        operations_times(1000)

    A = [0] * 100
    for i in range(0, 100):
        A[i] = 100 - i

    print("Test con lista ideale con 100 elementi:")
    print(" ")
    operation_best_list(A)

    A= [0] * 100
    for i in range(0, 100):
        A[i] = i + 1

    print("Test con lista peggiore con 100 elementi:")
    print(" ")
    operation_best_list(A)