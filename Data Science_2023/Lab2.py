import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.linear_model import LinearRegression

data = pd.read_csv('C://Users//-//Downloads//archive//bmi_data_lab2.csv')
print(data.describe())
print(data.dtypes)
# print(data.head(10))
# 3/7 Remove all likely wrong values & replace with NaN
data.loc[(data['Height (Inches)'] > 90) | (data['Height (Inches)'] <= 0), 'Height (Inches)'] = np.nan
data.loc[(data['Weight (Pounds)'] > 600) | (data['Weight (Pounds)'] <= 0), 'Weight (Pounds)'] = np.nan
# 3/7 extract without NaN
extract_data = data.dropna()
# 3/7 Fill NAN with mean, median, or using ffill / bfill methods
data.fillna(data.mean())
data.fillna(data.median())
data.fillna(method='ffill')
data.fillna(method='bfill')
# 히스토그램 형성
g = sns.FacetGrid(data, col='BMI')
g = g.map(plt.hist, 'Height (Inches)', bins=10)
g = sns.FacetGrid(data, col='BMI')
g = g.map(plt.hist, 'Weight (Pounds)', bins=10)
plt.show()

data_test = data[['Height (Inches)', 'Weight (Pounds)']]
std = StandardScaler()
std_data = std.fit_transform(data_test)
# print(std_data_h)
mm = MinMaxScaler()
mm_data = mm.fit_transform(data_test)
# print(mm_data_h)
rob = RobustScaler()
rob_data = rob.fit_transform(data_test)
# print(rob_data)
# Scaler가 완료된 값을 데이터프레임으로 형성, 시각화
std_scaled_df = pd.DataFrame(std_data, columns=['Height (Inches)', 'Weight (Pounds)'])
mm_scaled_df = pd.DataFrame(mm_data, columns=['Height (Inches)', 'Weight (Pounds)'])
rob_scaled_df = pd.DataFrame(rob_data, columns=['Height (Inches)', 'Weight (Pounds)'])
fig, (ax1, ax2, ax3, ax4) = plt.subplots(ncols=4, figsize=(10, 5))
ax1.set_title('Before Scaling')
sns.kdeplot(data['Height (Inches)'], ax=ax1)
sns.kdeplot(data['Weight (Pounds)'], ax=ax1)
ax2.set_title('After Standard Scaler')
sns.kdeplot(std_scaled_df['Height (Inches)'], ax=ax2)
sns.kdeplot(std_scaled_df['Weight (Pounds)'], ax=ax2)
ax3.set_title('After MinMax Scaler')
sns.kdeplot(mm_scaled_df['Height (Inches)'], ax=ax3)
sns.kdeplot(mm_scaled_df['Weight (Pounds)'], ax=ax3)
ax4.set_title('After Robust Scaler')
sns.kdeplot(rob_scaled_df['Height (Inches)'], ax=ax4)
sns.kdeplot(rob_scaled_df['Weight (Pounds)'], ax=ax4)
plt.show()

test_data = data.dropna()
test_X = test_data["Height (Inches)"]
test_y = test_data["Weight (Pounds)"]
# 선형 회귀 모델 학습
model = LinearRegression().fit(test_X.values.reshape(-1, 1), test_y)
# compute E / x절편 : a, y절편 : b
a = model.coef_[0]
b = model.intercept_
# E를 사용하여 NaN값 예측 후 대체
test_data.loc[pd.isnull(data['Weight (Pounds)']), 'Weight (Pounds)'] = \
    test_data.loc[pd.isnull(data['Weight (Pounds)']), 'Height (Inches)'] * a + b
test_data.loc[pd.isnull(data['Height (Inches)']), 'Height (Inches)'] = \
    (test_data.loc[pd.isnull(data['Height (Inches)']), 'Weight (Pounds)'] - b) / a
# 결측치 확인
print(data.isnull())

# 열/행별 결측치 수 확인
print(data_test.isnull().sum())
print(data_test.isnull().sum(axis=1))

# 시각화
X = test_data["Height (Inches)"]
y = test_data["Weight (Pounds)"]
plt.plot(X, y, 'o')
line_fitter = LinearRegression()
line_fitter.fit(X.values.reshape(-1,1), y)
plt.plot(X,line_fitter.predict(X.values.reshape(-1,1)))
plt.show()
# divide group by BMI and Sex
grouped_df = test_data.groupby(['Sex', 'BMI'])
print(grouped_df)