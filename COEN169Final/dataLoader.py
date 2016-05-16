import numpy as np
from sklearn.cluster import KMeans

class DataLoader():
    """

    """

    def __init__(self, training_set):
        self.trainingData = np.loadtxt(training_set)
        self.__lenTraining__ = len(self.trainingData)
        self.clusterer = KMeans()
        self.clusterer.fit(self.trainingData)

    def __len__(self):
        return self.__lenTraining__

    def predictClusters(self, test):
        labels = self.cluseterer.predict(test).labels_
        print(labels)
