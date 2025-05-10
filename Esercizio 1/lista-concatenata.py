class Node:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value
        self.next = None

class PriorityQueueLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, priority, value):
        new_node = Node(priority, value)
        new_node.next = self.head
        self.head = new_node

    def extract_min(self):
        if self.head is None:
            return None

        # Trova il nodo con la priorità minima
        min_prev = None
        min_node = self.head
        prev = None
        current = self.head

        while current is not None:
            if current.priority < min_node.priority:
                min_node = current
                min_prev = prev
            prev = current
            current = current.next

        # Rimuovi il nodo minimo dalla lista
        if min_prev is None:
            self.head = self.head.next
        else:
            min_prev.next = min_node.next

        return (min_node.priority, min_node.value)
