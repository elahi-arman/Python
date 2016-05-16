from DataLoader import DataLoader
from BoundedHeapq import BoundedHeapq
#load initial training data
# data = DataLoader('train.txt')

q = BoundedHeapq()
q.push((10, 'e'))
q.push((14, 'f'))
q.push((1, 'a'))
q.push((12, 'q'))
q.push((5, 'z'))
q.push((8, 'p'))

print(q)
