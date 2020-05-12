#!/usr/bin/env python3

import pandas as pd
import numpy as np
import os

def normalize_dataframe(df):
    df_normalized = (df - df.min())/(df.max() - df.min())

    return df_normalized

def normalize_write(filename , pathdata = '~/data_traintest'):
    df = pd.read_csv(os.path.join(pathdata,filename), delimiter = ',')
    if filename == "Train.csv" :
        labels = df.iloc[:,-1]
        df = df.iloc[:,:-1]
        labels = labels.to_numpy()
        labels = labels.reshape(labels.shape[0], 1)
        df_normalized = normalize_dataframe(df)
        df_normalized = df_normalized.to_numpy()
        df_normalized = np.append(df_normalized, labels, axis = 1)
        df_normalized = pd.DataFrame(df_normalized)
        df_normalized.to_csv("Normalized_train.csv", header = None)
    else:
        df_normalize = normalize_dataframe(df)
        df_normalize.to_csv("Normalized_test.csv", header = None)

if __name__ == "__main__":
    normalize_write("Train.csv")
    normalize_write("Test.csv")
