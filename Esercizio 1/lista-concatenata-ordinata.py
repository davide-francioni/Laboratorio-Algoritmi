class Node:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value
        self.next = None

class PriorityQueueSortedLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, priority, value):
        new_node = Node(priority, value)

        # Inserisci in posizione ordinata (dal più piccolo al più grande)
        if self.head is None or self.head.priority > priority:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next and current.next.priority <= priority:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def extract_min(self):
        if self.head is None:
            return None
        min_node = self.head
        self.head = self.head.next
        return (min_node.priority, min_node.value)