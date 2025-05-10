import heapq

class PriorityQueueHeap:
    def __init__(self):
        self.heap = []

    def insert(self, priority, value):
        heapq.heappush(self.heap, (priority, value))

    def extract_min(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None

    def is_empty(self):
        return len(self.heap) == 0
