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

    def sort(self, node):
        if self.head.priority < node.priority:
            print("Scambio in testa:", node.value, self.head.value)
            self.head.prev = node
            node.next = self.head
            self.head = node
            return
        current = self.head
        while current.next and current.next.priority > node.priority:
            current = current.next

        if current.next:
            print("Scambio:", node.value, current.next.value)

        node.next = current.next
        node.prev = current
        current.next = node
        if node.next:
            node.next.prev = node
        else:
            self.tail = node
        print("Scambio fatto:",node.prev.value, node.value, node.next.value)

    def insert(self, priority, value):
        new_node = Node(priority, value)
        print("Inserisco:", new_node.value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if self.tail.priority > new_node.priority:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
                current = self.head
                print("Lista aggiornata:")
                while current:
                    print(current.value, current.priority)
                    current = current.next
                return
            self.sort(new_node)
        current = self.head
        print("Lista aggiornata:")
        while current:
            print(current.value, current.priority)
            current = current.next



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