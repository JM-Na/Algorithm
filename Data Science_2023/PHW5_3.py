import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV, KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score
import warnings

warnings.filterwarnings(action='ignore')


def main():
    # given dataset
    data = pd.read_csv("C://Users//-//Downloads//data_sets_PHW5//knn_data.csv")
    X = data[['longitude', 'latitude']]
    y = data['lang']
    k_nearest(X, y)


def k_nearest(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    knn = KNeighborsClassifier()
    param_grid = {'n_neighbors': [3, 5, 7]}

    # set initial base model
    base_model = knn.fit(X_train, y_train)
    base_pred = base_model.predict(X_test)
    print("Initial model testing :", base_pred)
    print("Base model's Score: ", kfold_evaluation(base_model, X, y))

    # set grid search model
    grid_model = GridSearchCV(knn, param_grid, cv=5)
    print("Grid search model's Score: ", kfold_evaluation(grid_model, X, y))

    # set randomized search model
    rand_model = RandomizedSearchCV(knn, param_grid, cv=5)
    print("Randomized search model's Score: ", kfold_evaluation(rand_model, X, y))


def kfold_evaluation(model, X, y):
    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    scores = []
    # test model with 5 folds
    for train_idx, test_idx in kf.split(X):
        X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
        y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        score = accuracy_score(y_test, y_pred)
        scores.append(score)

    avg_score = np.mean(scores)
    return avg_score.round(2)


if __name__ == "__main__":
    main()
