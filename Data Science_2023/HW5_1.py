import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

def main():
    # given dataset from exercise 1
    age = [30, 40, 50, 60, 40]
    income = [200, 300, 800, 600, 300]
    worked = [10, 20, 20, 20, 20]
    vacation = [4, 4, 1, 2, 5]
    # get population covariance matrix
    data = np.array([age, income, worked, vacation])
    covMatrix = np.cov(data, bias=True)
    print(covMatrix)
    print('--------------------------------------------------------------------------')
    # print as heatmap
    sn.heatmap(covMatrix, annot=True, fmt='g')
    plt.show()
    # get sample covariance matrix with numpy
    covMatrix_np = np.cov(data, bias=False)
    sn.heatmap(covMatrix, annot=True, fmt='g')
    plt.show()
    print(covMatrix_np)
    print('--------------------------------------------------------------------------')
    # get sample covariance matrix with pandas
    data = {'Age': age, 'Income': income, 'Yrs worked': worked, 'Vacation': vacation}
    df = pd.DataFrame(data, columns=['Age', 'Income', 'Yrs worked', 'Vacation'])
    covMatrix_pd = pd.DataFrame.cov(df)
    print(covMatrix_pd)
    # visualize as heatmap
    sn.heatmap(covMatrix, annot=True, fmt='g')
    plt.show()


if __name__ == "__main__":
    main()
