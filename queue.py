import heapq


class PriorityQueue:

    def __init__(self):
        self.elements = []

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def empty(self):
        return len(self.elements) == 0
