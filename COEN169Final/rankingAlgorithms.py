import math

''' Basic Statistics Algorithms

    Mean -> calculates the average value for the distribution
    Variance -> calculates the distance away from the mean over the distribution
    StandardDeviation -> normalize the variance

'''

def mean(distribution):
    mean = 0

    for point in distribution:
        mean += point

    mean = mean / len(distribution)
    return mean

def variance(distribution):

    mn = mean(distribution)
    variance = 0

    for val in distribution:
        variance += (val-mn) * (val-mn)

    return variance

def standardDeviation(distribution):
    return math.sqrt(variance(distribution)/len(distribution))

''' Correlation Algorithms

    Covariance -> cov(x, y) = sum (xi - mean(x), yi - mean(y))/size
    Cosine -> cos(x, y) = (x dot y)/(magniteud(x) * magnitude(y))
    Pearson -> covariance(x, y)/(stdDev(x) * stdDev(y))
'''

def covariance (pDistribution, qDistribution):
    size = min (len(pDistribution), len(qDistribution))
    pMean = 0
    qMean = 0
    covariance = 0

    for i in range(0, size):
        pMean += pDistribution[i]
        qMean += qDistribution[i]

    pMean /= size
    qMean /= size

    for i in range(0, size):
        covariance += ((qDistribution[i]-qMean) * (pDistribution[i]-pMean))

    covariance /= size

    covariance = round(covariance, 3)
    return covariance

def cosine(pDistribution, qDistribution):

    xReduce = 0;
    yReduce = 0;
    similarity = 0;

    size = min(len(pDistribution), len(qDistribution))

    for i in range(0, size):
        similarity += pDistribution[i] * qDistribution[i];
        xReduce += pDistribution[i] * pDistribution[i];
        yReduce += qDistribution[i] * qDistribution[i];

    return (similarity)/(math.sqrt(xReduce) * math.sqrt(yReduce))

def pearson(pDistribution, qDistribution):

    cov = covariance(pDistribution, qDistribution)
    stdDevX = standardDeviation(pDistribution)
    stdDevY = standardDeviation(qDistribution)

    return (cov/(stdDevY*stdDevX))

''' Weighting Algorithms

    CaseMod -> amplify and weight the values closer to 1
    IUF -> check for how rare it is that a person watched a certain movie, just like IDF for term frequencies
'''

def caseMod(weight):
    amplification = 2.5
    return (weight * pow(weight, amplification -1))

def IUF(column, totalNumberUsers):
    return math.log(np.count_nonzero(column)/totalNumberUsers)
