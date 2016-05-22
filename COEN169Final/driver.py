from DataLoader import DataLoader
from BoundedHeapq import BoundedHeapq
from User import User

#load initial training data
data = DataLoader('train.txt')

test10 = dict()
users = []

with open('10.log', 'w') as log:

    with open('test10.txt') as test:
        for line in test:
            u, m, r = line.split()
            if u not in users:
                users.append(u)
            if u not in test10.keys():
                test10[u] = {'notrated': [], 'rated': []}
            if r == '0':
                test10[u]['notrated'].append(int(m))
            else:
                test10[u]['rated'].append((int(m), int(r)))

    for u in users:
        neighbors = data.kNN(test10[u]['rated'])
        avg = data.averageRating(test10[u]['rated'])
        user = User(u,test10[u]['rated'], test10[u]['notrated'],neighbors, avg)
        predictedRatings = data.cosine(user)

        print(u, user._average)
        for i in range(len(predictedRatings)):
            log.write("{} {} {}\n".format(u, user._notrated[i], predictedRatings[i]))



# data.rateMovies(neighbors, test10['301']['notrated'])
