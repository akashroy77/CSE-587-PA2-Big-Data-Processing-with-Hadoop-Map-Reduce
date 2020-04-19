#!/usr/bin/env python3
import sys
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import download, RegexpTokenizer
download("stopwords")
download("punkt")

stopWords = set(stopwords.words("english"))

for line in sys.stdin:
    #line = line.strip()
    #words = re.split('[\[\]\s,.;:!--_+?\']', line)
    words = word_tokenize(line)
    for word in words:
        if word.isalnum() == True:
            print(word,"\t",1)
        else:
            continue



