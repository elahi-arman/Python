import os
import re

from math import log
from sets import Set

#Calculates the Rawr Term Frequency + the Inverse Document Frequency as a measure
#of how important a word is to a document

def tf_idf_raw():

    file_out = open('histogram.txt', 'w')
    tf_raw = {};
    idf = {};

    for speech in os.listdir(os.getcwd()):
        if speech.endswith(".obama"):

            file_in = open(speech, 'r')
            bool_df = Set()

            for line in file_in:
                for word in line.split():
                    regex = re.compile('[^a-zA-Z]')
                    word = regex.sub('', word)
                    if tf_raw.has_key(word):
                        tf_raw[word] += 1
                    else:
                        tf_raw[word] = 1
                        bool_df.add(word)
            file_in.close();

        for word in bool_df:
            if idf.has_key(word):
                idf[word] += 1
            else:
                idf[word] = 1

    for (word, count) in idf.iteritems():
        file_out.write(word + '\t' + str(count) + '\n')

    file_out.write('\n\n TF \n\n')

    for (word, count) in tf_raw.iteritems():
        file_out.write(word + '\t' + str(log(8/idf[word]) * count) + '\n')

    file_out.close()

tf_idf_raw()
