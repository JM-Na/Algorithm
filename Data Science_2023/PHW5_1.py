import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


def main():
    # read given data
    data = pd.read_csv("C://Users//-//Downloads//data_sets_PHW5//linear_regression_data.csv")
    linear_regression(data, 0.8)
    linear_regression(data, 0.6)


def linear_regression(data, n):
    # seperate data
    X = data.loc[:, 'Distance']
    y = data.loc[:, 'Delivery Time']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1-n, shuffle=True)
    # set model
    model = LinearRegression()
    X_train = X_train.values.reshape(-1, 1)
    y_train = y_train.values.reshape(-1, 1)
    model.fit(X_train, y_train)
    # print the result
    y_pred = model.predict(X_test.values.reshape(-1, 1))
    print("The original data : ")
    print(y_test.values.reshape(1, -1))
    print("The predicted data : ")
    print(y_pred.reshape(1, -1).round(2))
    print("Mean squared error : ",  mean_squared_error(y_test, y_pred).__round__(3))
    print("----------------------------------------------------------------------------------")


if __name__ == "__main__":
    main()
