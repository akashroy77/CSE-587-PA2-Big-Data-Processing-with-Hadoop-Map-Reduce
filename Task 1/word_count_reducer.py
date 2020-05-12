#!/usr/bin/env python3

import sys
from operator import itemgetter
from itertools import groupby

for line in sys.stdin:
    line = line.strip().split("\t",1)
    for current_word,group in groupby(line, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)

            print(current_word, "\t", total_count)
        except ValueError:
            pass

    

