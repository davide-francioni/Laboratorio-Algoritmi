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

        while current is not None:
            if current.priority > max_node.priority:
                max_node = current
            current = current.next
        return max_node.value

    def extract_max(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            x=self.head.value
            y=self.head.priority
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
            max_prev.next.prev = max_prev

        return max_node.priority, max_node.value

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

if __name__ == '__main__':
    #genera un array casuale
    arr = genera_array_casuale(10)
    print(arr)

    list=Lista_Concatenata()
    i=0
    while i<len(arr):
        list.insert(arr[i])
        i += 1
    i=0

    #heap.increase_value(heap.get_random_node(), 17)

    while i<len(arr):
        x=list.list_max()
        y=list.extract_max()
        print(x,y)
        i += 1