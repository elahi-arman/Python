import numpy as np
from BoundedHeapq import BoundedHeapq
import rankingAlgorithms as rank
import math

class DataLoader():
    """

    """

    def __init__(self, training_set, testing_set=None):
        self.trainingData =  np.loadtxt(training_set)
        self.__lenTraining__ = len(self.trainingData)

    def __len__(self):
        return self.__lenTraining__

    def kNN(self, user_ratings):

        '''
        Determine the nearest neighbors for a user based on the ratings they have already given

        Returns:
            BoundedHeapq of tuples(similarity, userNumber)

        '''

        neighbors = BoundedHeapq(8)
        ratings, rated_movies = [], []
        for movie, rating in user_ratings:
            ratings.append(rating)
            rated_movies.append(movie)

        # print(rated_movies)
        extracted = self.trainingData[:, rated_movies]

        possible_neighbors = []
        for i in range(len(extracted)):
            nz = np.count_nonzero(extracted[i])
            if nz > 2:
                # print(i, ratings, extracted[i])
                subtracted = np.subtract(ratings, extracted[i])
                s = np.sum(np.absolute(subtracted))
                possible_neighbors.append((s, i))
                neighbors.push((s, i))
        return neighbors

    def averageRating(self, movies):
        return [np.mean(self.trainingData[:, movie]) for movie in movies]

    def cosine(self, user):
        #apply cosine to every movie that's in the neighbors and then average them all to be under 1

        length = len(user._notrated)

        aggregate_weights = [0] * (length)
        aggregate_ratings = [0] * (length)

        rated = [x[0] for x in user._ratings]
        ratings = [x[1] for x in user._ratings]

        for weight, neighbor in user._kNN:
            neighbor_ratings = [self.trainingData[neighbor][i] for i in rated]
            weight = rank.cosine(ratings, neighbor_ratings)
            for i in range(length):
                if self.trainingData[neighbor, i] != 0:
                    aggregate_weights[i] += weight
                aggregate_ratings[i] += self.trainingData[neighbor, i] * weight

        for i in range(length):
            aggregate_weights = [1 if aggregate_weights[i] == 0 else aggregate_weights[i] for j in range(length)]
            temp = (aggregate_ratings[i]/aggregate_weights[i])
            if temp == 0:
                temp = user._average

            aggregate_ratings[i] = temp

        for i in range(length):
            if predictedRatings[i] == 0:
                print(u, user._notrated[i], aggregate_ratings[i])

        return [int(round(r)) for r in aggregate_ratings]
