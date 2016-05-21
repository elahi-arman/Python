from DataLoader import DataLoader
from BoundedHeapq import BoundedHeapq
from User import User

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

neighbors = data.kNN(test10['301']['rated'])
avg = data.averageRating(test10['301']['rated'])
print(avg)
user = User('301',test10['301']['rated'], test10['301']['notrated'],neighbors, avg)
print(test10['301']['notrated'])
print(neighbors)
data.cosine(user)

# data.rateMovies(neighbors, test10['301']['notrated'])
