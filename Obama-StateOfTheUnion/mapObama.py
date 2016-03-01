import os
import re

file_out = open('out.txt', 'w')
histogram = {};

for speech in os.listdir(os.getcwd()):
    if speech.endswith(".obama"):
        file_in = open(speech, 'r')
        for line in file_in:
            for word in line.split():
                regex = re.compile('[^a-zA-Z]')
                word = regex.sub('', word)
                if (histogram.has_key(word)):
                    histogram[word] += 1;
                else:
                    histogram[word] = 1;
        file_in.close();

for (word, count) in histogram.iteritems():
    file_out.write(word + '\t' + str(count) + '\n')

file_out.close()
