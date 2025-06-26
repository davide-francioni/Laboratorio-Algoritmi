import time
import random

class Node:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value
        self.next = None
        self.prev = None

class Lista_Concatenata_Ordinata:
    def __init__(self):
        self.head = None
        self.tail = None

    def sort(self, node):
        if self.head.priority < node.priority:
            self.head.prev = node
            node.next = self.head
            self.head = node
            return
        current = self.head
        while current.next and current.next.priority > node.priority:
            current = current.next

        node.next = current.next
        node.prev = current
        current.next = node
        if node.next:
            node.next.prev = node
        else:
            self.tail = node

    def insert(self, priority, value):
        new_node = Node(priority, value)
        #print("Inserisco:", new_node.value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if self.tail.priority > new_node.priority:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
                return
            self.sort(new_node)

    def list_max(self):
        if self.head is None:
            return None
        return self.head.value

    def extract_max(self):
        if self.head is None:
            return None
        x = self.head.value
        y = self.head.priority
        if self.head == self.tail:
            self.tail = None
        self.head = self.head.next
        return x, y

    def increase_priority(self, node, priority):
        if priority < node.priority:
            raise ValueError(f"{priority} is lower than {node.priority}")
        node.priority = priority
        if node.prev is None or node.prev.priority > node.priority:
            return node.priority
        else:
            node.prev.next = node.next
            self.sort(node)

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

    lista = Lista_Concatenata_Ordinata()
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
    print("Incremento la priorita di :", y, "a", 1, "...")
    start_time = time.time()

    lista.increase_priority(x, 11)

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

    lista = Lista_Concatenata_Ordinata()
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

    lista.insert(0, 51) #0 così da inserirlo in coda, si poteva scegliere di inserire in testa ma così non entriamo neanche nellafunzione sort

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Elemento Inserito")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

    x = lista.get_random_node()
    y = x.value
    print("Incremento la priorita di :", y, "a", x.priority+1, "...")
    start_time = time.time()

    lista.increase_priority(x, x.priority+1) #priorità +1 perchè in questo modo non viene cambiato di posto

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

    lista = Lista_Concatenata_Ordinata()
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

    print("Inserimento dell'elemento 51 con priorità 1 nella lista...")
    start_time = time.time()

    lista.insert(1, 51) #si sceglie di inserire un nodo che andrà nella penultima posizione, così da scorrerre tutta la lista ed evitare il controllo sulla coda

    end_time = time.time()
    tempo_impiegato = end_time - start_time
    print("Elemento Inserito")
    print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")

    print(" ")

    x = lista.tail
    y = x.value
    print("Incremento la priorita di :", y, "a", x.priority+2, "...")
    start_time = time.time()

    lista.increase_priority(x, x.priority+2) #si sceglie l'ultimo elemento della lista e si aumenta di poco la sua priorità,così si scorrerà tutta la lista per posizionarlo avanti di una posizione

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
        P[i] = 100-i

    print("Test con lista ideale con 100 elementi:")
    print(" ")
    operation_best_list(A, P)

    P = [0] * 100
    for i in range(0, 100):
        P[i] = i+1

    print("Test con lista peggiore con 100 elementi:")
    print(" ")
    operation_best_list(A, P)