import heapq

class BoundedHeapq():

    def __init__(self, maxSize=5, maxHeap=True):
        self._maxHeap = maxHeap
        self._maxSize = maxSize
        self._len = 0
        self._q = []
        self._curr = 0

    def __len__(self):
        return self._len

    def __str__(self):
        return "{}".format(self._q)

    def __iter__(self):
        return self

    def __next__(self):
        if self._curr < self._len:
            temp = self._q[self._curr]
            self._curr += 1
            return temp
        else:
            raise StopIteration()

    def __getitem__(self, key):
        return self._q[key]

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
