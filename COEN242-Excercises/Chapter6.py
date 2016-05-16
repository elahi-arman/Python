#With 100 items, numbered 1 to 100 and 100 baskets, also 1 to 100
#Item i is in  basket b if and ony if i divides b with no remainder (all factors)
#currently super naive implementation
#TODO: once you have a factor, add all subfactors to basket -> dynamic programming
def generateFactors():
    baskets = [[]]          #we don't take into account 0, so it'll always be empty
    for i in range(1, 101):
        baskets.append([])  #create empty sublist
        for j in range(1, i+1):
            if i % j == 0:
                baskets[i].append(j)

    return baskets

#given a support threshold and a list of baskets, find which single items are frequent

def frequentItems(threshold, baskets):
    #For specific case in the book, all numbers up to max/threshold will appear at least threshold times
    return [i for i in range(1, (max(baskets)[1]/threshold) + 1)]

def frequentPairs(threshold, baskets):
    #for a pair to be frequent, both items in the pair must also be frequen
    frequentItems = frequentItems(threshold, baskets)
    # frequentPairs =

if __name__ == '__main__':
    baskets = generateFactors()
    print(frequentItems(5, baskets))
