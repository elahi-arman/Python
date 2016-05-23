from DataLoader import DataLoader
from BoundedHeapq import BoundedHeapq
from User import User
import rankingAlgorithms as rank

#load initial training data
data = DataLoader('train.txt')

test10 = dict()
users = []

with open('result5.txt', 'w') as log:

    with open('test5.txt') as test:
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

    for usr in users:
        neighbors = data.kNN(test10[usr]['rated'])
        avg = data.averageRating(test10[usr]['rated'])
        user = User(usr,test10[usr]['rated'], test10[usr]['notrated'],neighbors, avg)
        predictedRatings = data.predict(user, rank.pearson)

        for i in range(len(predictedRatings)):
            log.write("{} {} {}\n".format(usr, user._notrated[i], predictedRatings[i]))



# data.rateMovies(neighbors, test10['301']['notrated'])
