import rankingAlgorithms as rank

class User():

    """Container class for a User"""

    def __init__(self, uid, ratings, notrated, kNN, variance):
        self._id = uid
        self._ratings = ratings
        self._notrated = [index-1 for index in notrated]
        self._kNN = kNN
        self._average = int(round(rank.mean([rating[1] for rating in ratings])))
        self._variance = variance

    def __str__(self):
        return '{0}, {1}'.format(self._id, self._average)
