import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def main():
    # given data
    spends = np.array([2400, 2650, 2350, 4950, 3100, 2500, 5106, 3100, 2900, 1750])
    income = np.array([41200, 50100, 52000, 66000, 44500, 37700, 73500, 37500, 56700, 35600])
    # set LinearRegression model and fit it with given data
    model = LinearRegression().fit(spends[:, np.newaxis], income)
    # predict income data whose spends are 3500 and 5300
    num = model.predict(np.array([3500, 5300]).reshape(-1,1))
    # predict data to draw regression line
    px = np.array([spends.min()-1, spends.max()+1])
    py = model.predict(px[:, np.newaxis])
    # get a, b
    a = model.coef_[0]
    b = model.intercept_
    # print regression line and predicted data
    print("Regression Line is", "y = {:.2f}x + {:.2f}".format(a, b))
    print("if spends are 3500 and 5300, each are", num)
    # draw data in plt
    plt.scatter(spends, income)
    plt.plot(px, py, color='r')
    plt.show()


if __name__ == "__main__":
    main()
