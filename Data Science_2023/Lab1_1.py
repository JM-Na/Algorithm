import numpy as np


def main():
    wt = np.random.rand(100)
    for i in range(0, 100):  # wt array for float 40 ~ 90
        wt[i] = wt[i] * 50 + 40
    ht = np.random.randint(140, 200, 100)  # ht array for int 140 ~ 200
    bmi = [0] * 100

    for i in range(0, 100):  # calculate bmi
        bmi[i] = wt[i] / (ht[i] * ht[i]) * 10000

    for x in bmi:
        print(x)


if __name__ == "__main__":
    main()
