import rankingAlgorithms as rank

class User():

    """Container class for a User"""

    def __init__(self, uid, ratings, notrated, kNN, averageRatings):
        self._id = uid
        self._ratings = ratings
        self._notrated = notrated
        self._kNN = kNN
        self._average = rank.mean([rating[1] for rating in ratings])
        self._averageRatings = averageRatings

    def __str__(self):
        return '{0}, {1}'.format(self._id, self._average)
