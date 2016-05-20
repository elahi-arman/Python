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

    def determineNearestNeighbors(self, user_ratings):

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

    def customRanking(self, neighbors, movies):
        ''' Determine the ratings for movies given the nearest neighbors '''

        extractedNeighbors = np.array([self.trainingData[x[1]] for x in neighbors])
        neighborRatings = extractedNeighbors[:, movies]

        # print(neighbors)
        # print(neighborRati`ngs)

        ratings = []

        for i in range(len(movies)):
            currentWeight = 1
            totalWeight = 1

            for rating in neighborRatings:
                if rating[i] != 0:
                    # print(neighbors[i][0])
                    # print(neighborRatings[i])
                    weight = neighbors[i][0]
                    totalWeight += weight
                    currentWeight += neighborRatings[i] * weight

            ratings.append(round(np.sum(currentWeight/totalWeight)/2))

        ratings = [1 if r < 1 else int(r) for r in ratings ]

        print(ratings)

    # def cosine(self, neighbors, movies, weights):
