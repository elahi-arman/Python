import numpy as np
from BoundedHeapq import BoundedHeapq
import rankingAlgorithms as rank

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

        aggregate_ratings = [0] * (len(user._notrated)+1)
        for weight, neighbor in user._kNN:
            print(neighbor)
            for movie in user._notrated:
                print(movie, self.trainingData[neighbor, movie])
