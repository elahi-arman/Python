import math
import numpy as np
import rankingAlgorithms as rank
from BoundedHeapq import BoundedHeapq

from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import spearmanr
from sklearn.neighbors

np.set_printoptions(threshold=np.nan)

class DataLoader():
    """

    """

    def __init__(self, training_set, testing_set=None):
        self.trainingData =  np.loadtxt(training_set)
        self.__lenTraining__ = len(self.trainingData)
        self._nClusters = 13
        self._clusters = AgglomerativeClustering(n_clusters=self._nClusters).fit(self.trainingData)
        self._classifer = RandomForestClassifier(n_estimators=10).fit(self.trainingData, self._clusters.labels_)

    def __len__(self):
        return self.__lenTraining__

#      MAE of GIVEN 5 : 1.12742278354383
# MAE of GIVEN 10 : 1.09116666666667
# MAE of GIVEN 20 : 1.10494839394232
# OVERALL MAE : 1.10893120998194

    def forestPredictor(self, testData, average):
        predictedClusters = self._classifer.predict(testData)
        predictedRatings = []

        for j in range(len(testData)):
            #each cluster corresponds to a user
            for cluster in predictedClusters:
                #filter out and only get the users with the same cluster number
                neighbors = [i for i in range(self.__lenTraining__) if self._clusters.labels_[i] == cluster]

                #each row contains the weight for a neighbor
                weights = rank.weight(spearmanr, testData[j], self.trainingData[neighbors, :])

                #scale the weight because it's often super small due to how sparse data is
                weights = np.array(list(map(lambda x: x[0] * x[1] * 1000, weights))).reshape(-1, 1)

                #each row represents a neighbors's ratings
                extracted = self.trainingData[neighbors, :]
                extracted = extracted.transpose()

                predictions = []
                for movie in extracted:
                    predictions.append(round(np.sum(movie)/(np.count_nonzero(movie) +1 )))


                # account for 0 values
                predictions = [average if np.isnan(prediction) or prediction == 0 else prediction for prediction in predictions]
                predictedRatings.append(predictions)

        return predictedRatings


    def kNNRegressor(self):
        clusterer = neighbors.KNeighborsClustering(n_clusters=self._nClusters).fit(self.trainingData)
        regressor = neighbors.KNeighborsRegressor(self._nClusters, weights='distance')

        knn = regressor.fit(self.trainingData, clusterer.labels_)

        print(knn)

    def kNN(self, user_ratings, IUF=True):

        '''
        Determine the nearest neighbors for a user based on the ratings they have already given

        Returns:
            List of ints containing the userNumbers

        '''

        neighbors = BoundedHeapq(40)
        ratings, rated_movies = [], []
        iuf = [0] * self.__lenTraining__
        for movie, rating in user_ratings:
            ratings.append(rating)
            rated_movies.append(movie)

        if IUF == True:
            iuf = rank.IUF(self.trainingData, rated_movies, self.__lenTraining__)
        # print(rated_movies)
        extracted = self.trainingData[:, rated_movies]

        possible_neighbors = []
        for i in range(len(extracted)):
            nz = np.count_nonzero(extracted[i])
            if nz > 2:
                # print(i, ratings, extracted[i])
                subtracted = np.subtract(ratings, extracted[i])
                s = np.sum(np.absolute(subtracted))
                if IUF == True:
                    s = s * iuf[i]
                possible_neighbors.append((s, i))
                neighbors.push((s, i))


        return [n[1] for n in neighbors]

    def averageRating(self, movies):
        return [np.mean(self.trainingData[:, movie]) for movie in movies]

    def predict(self, user, algorithm, caseMod=True):
        #apply cosine to every movie that's in the neighbors and then average them all to be under 1

        length = len(user._notrated)

        aggregate_weights = [0] * (length)
        aggregate_ratings = [0] * (length)

        rated = [x[0] for x in user._ratings]
        ratings = [x[1] for x in user._ratings]

        for neighbor in user._kNN:

            neighbor_ratings = self.trainingData[neighbor, rated].tolist()
            weight = algorithm(ratings, neighbor_ratings)

            lgt = min(length, len(neighbor_ratings))
            for i in range(lgt):
                if neighbor_ratings[i] >= 1:
                    aggregate_weights[i] += weight
                    aggregate_ratings[i] += neighbor_ratings[i]

            aggregate_weights = [1 if aggregate_weights[i] < 1 else aggregate_weights[j] for j in range(length)]

            if caseMod == True:
                aggregate_weights = list(map(rank.caseMod, aggregate_weights))

            for i in range(length):
                temp = round(aggregate_ratings[i]/aggregate_weights[i])

                if temp == 0:
                    temp = user._average

                aggregate_ratings[i] = int(temp)

        for i in range(len(aggregate_ratings)):
            if aggregate_ratings[i] > 5:
                aggregate_ratings[i] = user._average

        return aggregate_ratings
