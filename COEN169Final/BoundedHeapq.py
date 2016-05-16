import heapq

class BoundedHeapq():

    def __init__(self, maxSize=5, maxHeap=True):
        self._maxHeap = maxHeap
        self._maxSize = maxSize
        self._len = 0
        self._q = []

    def __len__(self):
        return self._len

    def __str__(self):
        return "{}".format(self._q)

    def push(self, value):

        val = value[0]

        if self._maxHeap:
            val = val * -1

        #we've reached the end of our bound
        if self._len == self._maxSize:
            heapq.heappushpop(self._q, value)
        else:
            heapq.heappush(self._q, value)
            self._len = self._len + 1

    def pop(self):
        return heapq.heappop(self._q)
