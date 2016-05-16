import re
from WordGraph import WordGraph

'''
Running Analyses on the State of the Union addresses given by Obama
'''

def createWordGraph(file, wg=None):
    regex = re.compile('[^a-zA-Z\W]')
    if wg is None:
        wg = WordGraph()

    with open(file, 'r') as speech:
        for line in speech:
            # line = regex.sub('', line)


    return wg

graph = createWordGraph('Obama-StateOfTheUnion/2009.obama')
print(graph)
