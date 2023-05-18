import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def main():
    # read given data
    data = pd.read_csv("C://Users//-//Downloads//data_sets_PHW5//decision_tree_data.csv")
    # try with three cases
    decision_tree(data, 0.9)
    decision_tree(data, 0.8)
    decision_tree(data, 0.7)


def decision_tree(data, n):
    # reform categorical data
    categorical_cols = ['level', 'lang', 'tweets', 'phd']
    data_encoded = pd.get_dummies(data, columns=categorical_cols)
    # get target var
    X = data_encoded.drop('interview', axis=1)
    y = data_encoded['interview']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1-n, shuffle=True, stratify=y)
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    # print the predicted result
    y_pred = model.predict(X_test)
    print("The original data : ")
    print(y_test.values.reshape(1, -1))
    print("The predicted data : ")
    print(y_pred)
    print("Accuracy : ",  accuracy_score(y_test, y_pred).__round__(2))
    print("----------------------------------------------------------------------------------")


if __name__ == "__main__":
    main()
