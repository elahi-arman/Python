from DataLoader import DataLoader
from BoundedHeapq import BoundedHeapq
from User import User
import rankingAlgorithms as rank
from sys import argv
import numpy as np

dataSet = argv[1]
#load initial training data
data = DataLoader('train.txt')

dat = dict()
users = []      #need this to preserve order
with open('result'+dataSet+'.txt', 'w') as log:

    with open('test' + dataSet + '.txt') as test:
        for line in test:
            u, m, r = line.split()
            if u not in dat.keys():
                users.append(u)
                dat[u] = {'notrated': [], 'rated': [], 'features': np.zeros(1000)}
            if r == '0':
                dat[u]['notrated'].append(int(m))
            else:
                dat[u]['rated'].append((int(m), int(r)))
                dat[u]['features'][int(m)] = int(r)

    for usr in users:
        neighbors = data.kNN(dat[usr]['rated'])
        var = data.calculateVariance(dat[usr]['rated'])
        user = User(usr,dat[usr]['rated'], dat[usr]['notrated'],neighbors, var)
        predictedRatings = data.predict(user, rank.pearson)

        # forest = data.forestPredictor(dat[usr]['features'].reshape(1, -1), user._average)
        # for i in range(len(user._notrated)):
            # log.write("{} {} {}\n".format(usr, user._notrated[i], int(predictedRatings[i])))
