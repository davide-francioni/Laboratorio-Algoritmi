import time
import random

class Node:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value
        self.next = None
        self.prev = None

class Lista_Concatenata:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, priority, value):
        new_node = Node(priority, value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def list_max(self):
        max_node = self.head
        current = self.head

        while current:
            if current.priority > max_node.priority:
                max_node = current
            current = current.next
        return max_node.value

    def extract_max(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            x=self.head.priority
            y=self.head.value
            self.head = None
            self.tail = None
            return x, y

        # Trova il nodo con la priorità massima
        max_prev = None
        max_node = self.head
        prev = None
        current = self.head

        while current is not None:
            if current.priority > max_node.priority:
                max_node = current
                max_prev = prev
            prev = current
            current = current.next
        if max_prev is None:
            self.head = self.head.next
            self.head.prev = None
        else:
            max_prev.next = max_node.next
            if max_prev.next is None:
                self.tail = max_prev
            else:
                max_prev.next.prev = max_prev

        return max_node.priority, max_node.value

    def increase_priority(self, node, priority):
        if priority < node.priority:
            raise ValueError(f"{priority} is lower than {node.priority}")
        node.priority = priority


    def get_random_node(self):
        i = random.randint(1, 10)
        j=0
        if self.head is None:
            return None
        node = self.head
        while j<i:
            node = node.next
            j+=1
        return node

def genera_array_casuale(dimensione, minimo=0, massimo=100):
    return [random.randint(minimo, massimo) for _ in range(dimensione)]

def genera_priorita_casuale(dimensione, minimo=0, massimo=10):
    return [random.randint(minimo, massimo) for _ in range(dimensione)]

def operations_times(n):
    arr = genera_array_casuale(n)
    pri = genera_priorita_casuale(n)

    print("Elementi da inserire nella lista:", arr, "priorita:", pri)

    print("Creazione Coda di priorità con Lista concatenata...")
    start_time = time.time()
    print(arr)
    print(pri)

    lista = Lista_Concatenata()
    i = 0
    while i < len(arr):
        lista.insert(pri[i], arr[i])
        i += 1
    i = 0

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Coda di priorità creata")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

    print("Inserimento dell'elemento 51 con priorità 7 nella lista...")
    start_time = time.time()

    lista.insert(7, 51)

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Elemento Inserito")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

    x = lista.get_random_node()
    y = x.value
    print("Incremento la priorita di :", y, "a", 1001, "...")
    start_time = time.time()

    lista.increase_priority(x, 1001)

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Incremento dell'elemento completato")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

    print("Estrazione dell'elemento massimo...")
    start_time = time.time()

    y = lista.extract_max()

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Estrazione di", y, "completata")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

    print("Stampa dell'elemento massimo...")
    start_time = time.time()

    x = lista.list_max()

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Stampa di", x, "completata")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

def operation_best_list(A, P):
    print("Elementi da inserire nella lista:", A, "priorita:", P)

    print("Creazione Coda di priorità con Lista concatenata...")
    start_time = time.time()
    print(A)
    print(P)

    lista = Lista_Concatenata()
    i = 0
    while i < len(A):
        lista.insert(P[i], A[i])
        i += 1
    i = 0

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Coda di priorità creata")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

    print("Inserimento dell'elemento 51 con priorità 7 nella lista...")
    start_time = time.time()

    lista.insert(7, 51)

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Elemento Inserito")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

    x = lista.get_random_node()
    y = x.value
    print("Incremento la priorita di :", y, "a", x.priority+1, "...")
    start_time = time.time()

    lista.increase_priority(x, x.priority+1)

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Incremento dell'elemento completato")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

    print("Estrazione dell'elemento massimo...")
    start_time = time.time()

    y = lista.extract_max()

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Estrazione di", y, "completata")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

    print("Stampa dell'elemento massimo...")
    start_time = time.time()

    x = lista.list_max()

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Stampa di", x, "completata")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

def operation_worst_list(A, P):
    print("Elementi da inserire nella lista:", A, "priorita:", P)

    print("Creazione Coda di priorità con Lista concatenata...")
    start_time = time.time()
    print(A)
    print(P)

    lista = Lista_Concatenata()
    i = 0
    while i < len(A):
        lista.insert(P[i], A[i])
        i += 1
    i = 0

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Coda di priorità creata")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

    print("Inserimento dell'elemento 51 con priorità 101 nella lista...")
    start_time = time.time()

    lista.insert(101, 51)

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Elemento Inserito")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

    x = lista.get_random_node()
    y = x.value
    print("Incremento la priorita di :", y, "a", x.priority+1, "...")
    start_time = time.time()

    lista.increase_priority(x, x.priority+1)

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Incremento dell'elemento completato")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

    print("Estrazione dell'elemento massimo...")
    start_time = time.time()

    y = lista.extract_max()

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Estrazione di", y, "completata")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

    print("Stampa dell'elemento massimo...")
    start_time = time.time()

    x = lista.list_max()

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

    A = genera_array_casuale(100)
    P = [0] * 100
    for i in range(0, 100):
        P[i] = 100 - i

    print("Test con lista ideale con 100 elementi:")
    print(" ")
    operation_best_list(A, P)

    P = [0] * 100
    for i in range(0, 100):
        P[i] = i + 1

    print("Test con lista peggiore con 100 elementi:")
    print(" ")
    operation_best_list(A, P)