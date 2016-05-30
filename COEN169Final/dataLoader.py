import math
import numpy as np
import rankingAlgorithms as rank
from BoundedHeapq import BoundedHeapq


from sklearn import svm
np.set_printoptions(threshold=np.nan)

class DataLoader():
    """

    """

    def __init__(self, training_set, testing_set=None):
        self.trainingData =  np.loadtxt(training_set)
        self.__lenTraining__ = len(self.trainingData)

        for i in range(1000):
            nonzero = np.count_nonzero(self.trainingData[:, i]) + 1
            self._movieAverages = np.sum(self.trainingData, axis=0) / nonzero
        self._movieAverages = [round(rating) for rating in self._movieAverages]
        print(self._movieAverages)

        self._nClusters = 8

    def __len__(self):
        return self.__lenTraining__
        self.__lenTraining__ = self.trainingData.shape
        self._nClusters = 13

        averageRatings = []
        similarItems = []

        for i in range(0, self.__lenTraining__[1]):
            averageRatings.append(np.sum(self.trainingData[:,i])/np.count_nonzero(self.trainingData[:, i]))

        self._averageRatings = [0 if np.isnan(rating) else round(rating) for rating in averageRatings]
        # self._similarItems = [self.KNN_Item(item) for item in similarItems]


    def __len__(self):
        return self.__lenTraining__

    def kNN_Row(self, user_ratings, algorithm, IUF=True):

        '''
        Determine the nearest neighbors for a user based on the ratings they have already given

        Returns:
            List of ints containing the userNumbers

        '''

        neighbors = BoundedHeapq(15)
        ratings, rated_movies = [], []
        # possible_neighbors = []
        iuf = [0] * self.__lenTraining__[0]

        #parse out the new user data
        for movie, rating in user_ratings:
            ratings.append(rating)
            rated_movies.append(movie)

        #apply IUF
        if IUF == True:
            iuf = rank.IUF(self.trainingData, rated_movies, self.__lenTraining__[0])

        #contains only the columns we actually want to look at
        extracted = self.trainingData[:, rated_movies]

        for i in range(len(extracted)):
            nz = np.count_nonzero(extracted[i])
            # need to have at least 2 similar movies
            if nz > 2:
                similarity = algorithm(ratings, extracted[i])
                if IUF == True:
                    similarity = similarity * iuf[i]
                # possible_neighbors.append((similarity, i))
                neighbors.push((similarity, i))

        np.append(self.trainingData, user_ratings)
        return neighbors

    def averageRating(self, movies):
        return [np.mean(self.trainingData[:, movie]) for movie in movies]

    def calculateVariance(self, movies):
        s = 0
        for movie in movies:
            s += (self._averageRatings[movie[0]] - movie[1])
        return (s/len(movies))

    def predict(self, user, algorithm, caseMod=True):
        length = len(user._notrated)
        predictions = []


        neighbors_ratings = self.trainingData[[n[1] for n in user._kNN], :]
        neighbors_ratings = neighbors_ratings[:,user._notrated]

        for i in range(neighbors_ratings.shape[0]):
            if caseMod == True:
                weighted_ratings = np.multiply(neighbors_ratings[i, :], rank.caseMod(user._kNN[i][0]))
            else:
                weighted_ratings = np.multiply(neighbors_ratings[i, :], user._kNN[i][0])

        print(weighted_ratings)

        for i in range(neighbors_ratings.shape[1]):
            col = neighbors_ratings[:, i]
            predictions.append(np.sum(col)/np.count_nonzero(col))

        predictions = [int(round(p)) if p > 0 else 0 for p in predictions]

        # print(predictions)
        # for i in range(length):
        #     if predictions[i] == 0:
        #         predictions[i] = int(round((self._averageRatings[user._notrated[i]]-user._variance) * .4 + user._average * .6))
        #     if predictions[i] < 1 or predictions[i] > 5:
        #         predictions[i] = user._average

        return predictions

        # for neighbor in user._kNN:
        #
        #     #set up the data needed for this neighbor
        #     neighbor_ratings = self.trainingData[neighbor, notrated].tolist()
        #     weight = algorithm(ratings, neighbor_ratings)
        #
        #     for i in range(length):
        #         if neighbor_ratings[i] >= 0:
        #             aggregate_ratings[i] += neighbor_ratings[i] * weight

        return aggregate_ratings


    ''' Scikit-Learn based Predictors '''

    # MAE of GIVEN 5 : 1.12742278354383
    # MAE of GIVEN 10 : 1.09116666666667
    # MAE of GIVEN 20 : 1.10494839394232
    # OVERALL MAE : 1.10893120998194

    def svmPredictor(self, testData, average):
        '''SVM Based Predictor with KMeans Clustering'''
        clusterer =
        classifer = svm.SVC().fit(self._training)
        predictedClusters = classifier.predict(testData)
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
