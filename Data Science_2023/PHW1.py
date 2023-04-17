import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from scipy.stats import norm
pd.set_option('mode.chained_assignment',  None)


def main():
    # dataset 읽어오기 ---------------------------------------------------------------------
    df = pd.read_excel('C://Users//-//Downloads//archive//bmi_data_phw1.xlsx')
    m_df = df[df['Sex'] == 'Male']
    f_df = df[df['Sex'] == 'Female']
    phw1(df)
    # 성별로 dataset 분류
    print("------------------ Male data---------------------------------------------------")
    phw1(m_df)
    print("------------------ Female data-------------------------------------------------")
    phw1(f_df)


def phw1(data):
    # data의 statistical data, feature name, data type 출력 --------------------------------
    print(data.describe())
    print(data.dtypes)
    # 히스토그램 형성 ------------------------------------------------------------------------
    g = sns.FacetGrid(data, col='BMI')
    g = g.map(plt.hist, 'Height (Inches)', bins=10)
    g = sns.FacetGrid(data, col='BMI')
    g = g.map(plt.hist, 'Weight (Pounds)', bins=10)
    plt.show()
    # 테스트 데이터셋 형성 후 Scaler 사용 ------------------------------------------------------
    data_test = data[['Height (Inches)', 'Weight (Pounds)']]
    std_data = StandardScaler().fit_transform(data_test)
    mm_data = MinMaxScaler().fit_transform(data_test)
    rob_data = RobustScaler().fit_transform(data_test)
    # Scaler가 완료된 값을 데이터프레임으로 형성 -------------------------------------------------
    std_scaled_df = pd.DataFrame(std_data, columns=['Height (Inches)', 'Weight (Pounds)'])
    mm_scaled_df = pd.DataFrame(mm_data, columns=['Height (Inches)', 'Weight (Pounds)'])
    rob_scaled_df = pd.DataFrame(rob_data, columns=['Height (Inches)', 'Weight (Pounds)'])
    # 히스토그램 4개 출력 ---------------------------------------------------------------------
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
    # Linear regression equation E 계산
    test_X = data["Height (Inches)"]
    test_y = data["Weight (Pounds)"]
    model = LinearRegression().fit(test_X.values.reshape(-1, 1), test_y)
    # compute E / x절편 : A, y절편 : B
    A = model.coef_[0]
    B = model.intercept_
    # E를 이용하여 e, Z(e) 계산
    data['e'] = data["Weight (Pounds)"] - (data["Height (Inches)"] * A + B)
    data['Z(e)'] = (data['e'] - data['e'].mean()) / data['e'].std()
    # Z(e)의 분포 히스토그램으로 표현
    g = sns.FacetGrid(data)
    g = g.map(plt.hist, 'Z(e)', bins=10)
    plt.show()
    # a 값 계산
    value_0 = data.loc[data['BMI'] == 0, 'Z(e)'].max()
    value_4 = data.loc[data['BMI'] == 4, 'Z(e)'].min()
    a = int(min(-value_0, value_4) * 100) / 100
    print('a = ', a)
    # 정규 분포 그래프 형성
    rv = norm(loc=0, scale=1)
    # 예측치, 데이터에서 얻은 수치를 각각 정규분포로 환산
    est_result = 1 - (rv.cdf(a) - rv.cdf(-a))
    act_result = ((data['BMI'] == 0) | (data['BMI'] == 4)).sum() / data.shape[0]
    print("Estimated BMI values of 0, 4 : ", int(est_result * 100), '%')
    print("Actual BMI values of 0, 4 : ", int(act_result * 100), '%')


if __name__ == "__main__":
    main()
