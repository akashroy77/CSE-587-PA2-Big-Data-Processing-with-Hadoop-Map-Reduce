#!/usr/bin/env python3
import numpy as np
import sys
import pandas as pd



df_train = pd.read_csv("~/data_traintest/Train.csv", delimiter = ",")
labels = df_train.iloc[:,-1]
df_train = df_train.iloc[:,:-1]
df_train = df_train.to_numpy()
value_index = 0
k = 6
for line in sys.stdin:
    values = line.strip().split(",")
    values  = list( map(float, values))
    values = np.asarray(values).astype("float32")
    distances = np.linalg.norm(df_train - values, axis = 1)
    distances = np.column_stack((distances, labels))
    distances = sorted(distances, key = (lambda x:x[0]))
    distances = np.asarray(distances)
    distances = distances[0:k]
    output = ""
    for x in distances:
        output = output + str(x[0]) + "," + str(x[1])+";"
    print(value_index,"\t",output)
    value_index += 1

