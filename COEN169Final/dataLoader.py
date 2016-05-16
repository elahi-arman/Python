import numpy as np
from BoundedHeapq import BoundedHeapq

class DataLoader():
    """

    """

    def __init__(self, training_set):
        self.trainingData =  np.loadtxt(training_set)
        self.__lenTraining__ = len(self.trainingData)


    def __len__(self):
        return self.__lenTraining__

    def determineNearestNeighbors(self, rated_movies, ratings):
        ''' Add training data for a new user '''
        neighbors = BoundedHeapQ()
        extracted = self.trainingData[:, rated_movies]

        for e in extracted:
            s = np.sum(np.subtract(rated_movies, e))
            print(s)
            neighbors.push((s, e))

        print(neighbors)
