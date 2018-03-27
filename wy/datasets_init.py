import numpy as np
import pandas as pd

train = pd.read_csv("../../wy_private/walmart-trip-classification/dataset/train.csv", dtype={'Upc' : object, 'FinelineNumber' : object})
print("train data successfully imported as train")
test = pd.read_csv("../../wy_private/walmart-trip-classification/dataset/test.csv", dtype={'Upc' : object, 'FinelineNumber' : object})
print("train data successfully imported as test")
print("you may now begin")
