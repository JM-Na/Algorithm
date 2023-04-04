import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing(data_home=None, download_if_missing=True,
                                return_X_y=False, as_frame=False)
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target.astype(int)
df['Longitude'] = df['Longitude'].abs()

X = df.iloc[:, 0:8]
y = df.iloc[:, -1]

# ---------------------------------------------------------------
bestfeatures = SelectKBest(score_func=chi2, k=8)
fit = bestfeatures.fit(X, y)
dfcolumns = pd.DataFrame(X.columns)
dfscores = pd.DataFrame(fit.scores_)
featureScores = pd.concat([dfcolumns, dfscores], axis=1)
featureScores.columns = ['Features', 'Score']
print(featureScores.nlargest(10, 'Score'))

# --------------------------------------------------------------------
model = ExtraTreesClassifier()
model.fit(X, y)
print(model.feature_importances_)
feat_importances = pd.Series(model.feature_importances_, index=X.columns)
feat_importances.nlargest(10).plot(kind='barh')
plt.show()

# -----------------------------------------------------------------
corrmat = df.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(20, 20))
g = sns.heatmap(df[top_corr_features].corr(), annot=True, cmap="RdYlGn")
plt.show()
