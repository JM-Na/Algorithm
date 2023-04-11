import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df = pd.read_csv('C://Users//-//Downloads//archive//housing.csv')
print(df.head(5))
print('----------------------------------------------------------------------------')
features = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population',
            'households', 'median_income', 'median_house_value']
# Separate out the features
x = df.loc[:, features].values
# Separate out the target
y = df.loc[:, ['ocean_proximity']].values
# Standardize the features
x = StandardScaler().fit_transform(x)
standardDf = pd.DataFrame(x, columns=features)
print(standardDf.head(5))
print('----------------------------------------------------------------------------')
pca = PCA(n_components=2)
for a in features:
    standardDf[a].fillna(standardDf[a].mean(), inplace=True)
x = standardDf.loc[:, features].values

principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data=principalComponents,
                           columns=['principal component 1', 'principal component 2'])
print(principalDf.head(5))
print('----------------------------------------------------------------------------')
finalDf = pd.concat([principalDf, df[['ocean_proximity']]], axis=1)
print(finalDf.head(5))
print('----------------------------------------------------------------------------')
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Principal Component 1', fontsize=15)
ax.set_ylabel('Principal Component 2', fontsize=15)
ax.set_title('2 component PCA', fontsize=20)
ocean_proximity = ['NEAR BAY', 'INLAND', '<1H OCEAN']
colors = ['r', 'g', 'b']
for proximity, color in zip(ocean_proximity, colors):
    indicesToKeep = finalDf['ocean_proximity'] == proximity
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'],
               finalDf.loc[indicesToKeep, 'principal component 2'],
               c=color, s=50)
ax.legend(ocean_proximity)
ax.grid()
plt.show()
