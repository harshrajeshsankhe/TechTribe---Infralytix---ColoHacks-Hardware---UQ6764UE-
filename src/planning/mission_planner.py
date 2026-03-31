import heapq

class MissionPlanner:

    def __init__(self):
        self.heap = []

    def add(self, victim):
        heapq.heappush(self.heap, (-victim.confidence, victim))

    def get(self):
        return heapq.heappop(self.heap)[1] if self.heap else None
