#!/usr/bin/env python3
import numpy as np
import re
import sys

for line in sys.stdin:
    vals = line.split()
    for val in vals[1]:
        values = vals[1].split(';')
        dl =[]
        for i in values:
            vd = []
            if len(i)>0:
                j = i.split(',')
                for x in j:
                    vd.append(float(x))
                dl.append(vd)
            else:
                pass
    dl = np.asarray(dl)
    labels = dl[::,-1]
    labels = labels.astype("int64")
    counts = np.bincount(labels)
    label = np.argmax(counts)
    print(vals[0], "\t", label)

        
    
