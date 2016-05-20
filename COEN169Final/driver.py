from DataLoader import DataLoader
from BoundedHeapq import BoundedHeapq

#load initial training data
data = DataLoader('train.txt')

test10 = dict()

with open('test10.txt') as test:
    for line in test:
        u, m, r = line.split()
        if u not in test10.keys():
            test10[u] = {'notrated': [], 'rated': []}
        if r == '0':
            test10[u]['notrated'].append(int(m))
        else:
            test10[u]['rated'].append((int(m), int(r)))

neighbors = data.determineNearestNeighbors(test10['301']['rated'])
print(neighbors)
# data.rateMovies(neighbors, test10['301']['notrated'])
