import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

pd.set_option('display.max_columns', None)


def kfold_for_model(model):
    # K-fold 교차 검증 설정
    kfold = KFold(n_splits=5, shuffle=True, random_state=1)
    # K-fold 교차 검증 수행
    mse_scores = []
    for train_index, eval_index in kfold.split(X):
        X_train, X_eval = X.iloc[train_index], X.iloc[eval_index]
        y_train, y_eval = y.iloc[train_index], y.iloc[eval_index]
        # 모델 학습
        model.fit(X_train, y_train)
        # 평가 데이터에 대한 예측
        y_eval_pred = model.predict(X_eval)
        # 평가 지표(MSE) 계산
        mse = mean_squared_error(y_eval, y_eval_pred)
        mse_scores.append(mse)
    # K-fold 교차 검증 평균 MSE 계산
    mean_mse = np.mean(mse_scores)
    print(model, "의 평균 MSE:", mean_mse)


data = pd.read_csv("C://Users//-//Downloads//archive//kbopitchingdata.csv", encoding='CP949')
# NaN값 및 불필요한 데이터 제거()
data = data.dropna()
df = data.drop(
    columns=["id", "승", "패", "경기 수", "선발 출장 수", "완투 게임 수", "투구 이닝", "피안타", "실점", "자책점", "피홈런", "볼넷", "고의사구", "탈삼진",
             "사구", "보크", "폭투", "상대타자", "완투 수", "완봉 수", "경기당 실점", "9이닝당 피안타", "9이닝당 볼넷"], axis='columns')
# 긍정적, 부정적 컬럼 설정
positive_columns = ['평균 연령', '탈삼진 볼넷 비율', '세이브', '9이닝당 탈삼진']
negative_columns = ['ERA', '9이닝당 실점', '9이닝당 피홈런', 'WHIP']
X = df.drop(columns=['승률', '연도', '팀'])  # 예측에 사용할 특성들
y = df['승률']  # 타겟 변수 (승률)

# 랜덤 포레스트 모델 학습
rf = RandomForestRegressor()
kfold_for_model(rf)

rf.fit(X, y)
# 특성 중요도 계산, 중요도 표준화
importance = rf.feature_importances_
normalized_importance = (importance - importance.min()) / (importance.max() - importance.min())
# 점수 계산
df['점수'] = df[positive_columns].dot(normalized_importance[:len(positive_columns)]).round(2) \
           + df[negative_columns].dot(-normalized_importance[:len(negative_columns)]).round(2)

# 클러스터링 / KMeans 모델 학습
X = df[['점수', '승률']]
kmeans = KMeans(n_clusters=10, random_state=1)
kfold_for_model(kmeans)
kmeans.fit(X)
df['Cluster'] = kmeans.labels_

# 원본 데이터에서 우승팀 정보 필터링
winning_teams = [('2010', 'SK Wyverns'), ('2011', 'Samsung Lions'), ('2012', 'Samsung Lions'),
                 ('2013', 'Samsung Lions'), ('2014', 'Samsung Lions'), ('2015', 'Doosan Bears'),
                 ('2016', 'Doosan Bears'), ('2017', 'Kia Tigers'), ('2018', 'SK Wyverns'), ('2019', 'Doosan Bears'),
                 ('2020', 'NC Dinos'), ('2021', 'KT Wiz')]
filtered_df = df[df.apply(lambda row: (str(row['연도']), row['팀']) in winning_teams, axis=1)]
new_dataset = filtered_df.copy()
new_dataset = new_dataset[['연도', '팀', '승률', '점수', 'Cluster']]
print(new_dataset)

# 현재 진행 중인 리그의 데이터셋
data_2023 = pd.read_excel("C://Users//-//Downloads//archive//2023kbopitching.xlsx")
features = ['평균 연령', 'ERA', '9이닝당 실점', '세이브', 'WHIP', '9이닝당 피홈런', '탈삼진 볼넷 비율']

# Linear Regression 모델 학습 및 이번 시즌 종료시 데이터 예측
df_predict = data_2023.copy()
df_predict['경기'] = 144
X_2023 = data_2023[features]
y_2023 = data_2023['승률']
X_predict = df_predict[features]
lr = LinearRegression()
kfold_for_model(lr)
lr.fit(X_2023, y_2023)
y_predict = lr.predict(X_predict)
df_predict['승률'] = y_predict.round(3)
df_predict = df_predict.drop(columns=["경기"])

# 현재 시즌 데이터 점수 계산
X_score = df_predict[positive_columns + negative_columns]
df_predict['점수'] = X_score.dot(normalized_importance).round(2)

# 현재 시즌 클러스터 할당
X_cluster = df_predict[['점수', '승률']]
labels_predict = kmeans.predict(X_cluster)
df_predict['Cluster'] = labels_predict

print(df_predict[['팀', '승률', '점수', 'Cluster']])

# 시각화를 위한 데이터 분리
winning_dataset = new_dataset
current_dataset = df_predict
plt.figure(figsize=(10, 6))
cluster_colors = ['lightcoral', 'lightblue', 'lightgreen', 'lightsalmon', 'thistle', 'lightyellow', 'lightcyan',
                  'lightpink', 'tan', 'lightgray']
for cluster in range(10):
    cluster_data = df[df['Cluster'] == cluster]
    plt.scatter(cluster_data['점수'], cluster_data['승률'], color=cluster_colors[cluster], alpha=0.6,
                label=f'Cluster {cluster}')
plt.scatter(winning_dataset['점수'], winning_dataset['승률'], color='gold', edgecolors='black', linewidths=1.5,
            label='Previous Winners')  # 우승팀
plt.scatter(current_dataset['점수'], current_dataset['승률'], color='limegreen', edgecolors='black', linewidths=1.5,
            label='Season 2023')  # 현재 시즌
for i, team_name in enumerate(current_dataset['팀']):
    plt.annotate(team_name, (current_dataset['점수'].values[i], current_dataset['승률'].values[i]),
                 xytext=(5, -5), textcoords='offset points')
plt.title('KBO Winner Prediction')
plt.xlabel('Score')
plt.ylabel('Win Rate')
plt.legend()
plt.show()
