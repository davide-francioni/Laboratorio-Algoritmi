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
        print("Inserisco:", new_node.value)
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
        # Rimuovi il nodo minimo dalla lista
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
        return node.priority


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

if __name__ == '__main__':
    #genera un array casuale
    arr = genera_array_casuale(10)
    pri = genera_priorita_casuale(10)
    print(arr)
    print(pri)

    lista=Lista_Concatenata()
    i=0
    while i<len(arr):
        lista.insert(pri[i], arr[i])
        i += 1
    i=0

    x=lista.get_random_node()
    y=x.priority
    inc=lista.increase_priority(x, 11)
    print("Aumento la priorità di:",x.value, "da", y, "a", inc)

    while i<len(arr):
        x=lista.list_max()
        y=lista.extract_max()
        print(x,y)
        i += 1