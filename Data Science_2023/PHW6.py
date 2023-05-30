import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# read dataset row = 150
iris = pd.read_csv("C://Users//-//Downloads//archive//iris.csv")
label_encoder = LabelEncoder()
X = iris.drop("species", axis=1)
# encode the target value from String to Integer
y = pd.DataFrame(label_encoder.fit_transform(iris["species"]))

# form subsets with bagging
subsets = []
for _ in range(10):
    # form subsets with np.random, has 30 rows
    indices = np.random.choice(len(X), size=30, replace=True)
    subset_X = X.loc[indices]
    subset_y = y.loc[indices]
    subsets.append((subset_X, subset_y))

# calculate predictions with subsets
predictions = []
for subset_X, subset_y in subsets:
    dt = DecisionTreeClassifier()
    dt.fit(subset_X, subset_y)
    predictions.append(dt.predict(X))

# get final prediction through vote
final_pred = np.mean(predictions, axis=0).round().astype(int)

# calculate confusion matrix
confusion_mat = confusion_matrix(y, final_pred)
print("Confusion Matrix:")
print(confusion_mat)

# calculate accuracy
print("Accuracy:", accuracy_score(y, final_pred))
