import numpy as np
import pandas as pd

global height
global weight


def main():
    global height
    global weight
    # given data
    data = pd.read_excel("C://Users//-//Downloads//archive//size_data.xlsx")
    # sample data
    height = 161
    weight = 61
    normalize(data)
    calDistance(height, weight, data)
    print(data)
    kNearest(data)


def normalize(df):
    global height
    global weight
    # calculate mean, std_dev
    mean_h = np.mean(df["HEIGHT(cm)"], axis=0)
    std_dev_h = np.std(df["HEIGHT(cm)"], axis=0)
    mean_w = np.mean(df["WEIGHT(kg)"], axis=0)
    std_dev_w = np.std(df["WEIGHT(kg)"], axis=0)
    # standard normalize the data
    df["HEIGHT(cm)"] = (df["HEIGHT(cm)"]-mean_h) / std_dev_h
    df["WEIGHT(kg)"] = (df["WEIGHT(kg)"]-mean_w) / std_dev_w
    height = (height - mean_h) / std_dev_h
    weight = (weight - mean_w) / std_dev_w


def calDistance(h, w, df):
    # add Distance column by calculating the distance from (h, w) to each spot
    df["Distance"] = ((df["HEIGHT(cm)"]-h)**2 + (df["WEIGHT(kg)"]-w)**2)**0.5


def kNearest(df):
    # when k = 3
    sample = df.nsmallest(3, "Distance")
    # print(sample)
    print("When k = 3, the predicted size is ", sample["T SHIRT SIZE"].mode()[0])
    # when k = 5
    sample = df.nsmallest(5, 'Distance')
    # print(sample)
    print("When k = 5, the predicted size is ", sample["T SHIRT SIZE"].mode()[0])


if __name__ == "__main__":
    main()
