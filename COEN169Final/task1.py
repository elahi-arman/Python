def mean(distribution):
    mean = 0

    for point in distribution:
        mean += point

    mean = mean / len(distribution)
    return mean

def variance(distribution):

    mn = mean(distribution)
    variance = 0

    #for small number, multiplication is faster than squaring
    for val in distribution:
        variance += (val-mn) * (val-mn)

    return variance

def standardDeviation(distribution):
    return math.sqrt(variance(distribution)/len(distribution))

''' Correlation Algorithms

    Covariance -> cov(x, y) = sum (xi - mean(x), yi - mean(y))/size
    Cosine -> cos(x, y) = (x dot y)/(magniteud(x) * magnitude(y))
    Pearson ->
'''

def covariance (pDistribution, qDistribution):
    #currently doesn't interpolate points, but points should be interpolated
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
