import rankingAlgorithms

class User():

    """Container class for a User"""

    def __init__(self, uid, ratings, notrated, kNN, averageRatings):
        self._id = uid
        self._ratings = ratings
        self._notrated = notrated
        self._kNN = kNN
        print("Ratings", ratings)
        self._average = rankingAlgorithms.mean([rating[1] for rating in ratings])
        self._averageRatings = averageRatings
