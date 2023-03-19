import numpy as np
import matplotlib.pyplot as plt


# Numpy Exercise
def main():
    freq = [0] * 4
    wt = np.random.rand(100)
    for i in range(0, 100):  # wt array for float 40 ~ 90
        wt[i] = wt[i] * 50 + 40
    ht = np.random.randint(140, 200, 100)  # ht array for int 140 ~ 200
    bmi = [0] * 100

    for i in range(0, 100):  # calculate bmi
        bmi[i] = wt[i] / (ht[i] * ht[i]) * 10000
        if bmi[i] < 18.5:
            freq[0] += 1
        elif 18.5 <= bmi[i] < 25.0:
            freq[1] += 1
        elif 25.0 <= bmi[i] < 30.0:
            freq[2] += 1
        elif bmi[i] >= 30:
            freq[3] += 1
    langs = ['Underweight', 'Healthy', 'Overweight', 'Obese']
    # Bar Chart
    plt.bar(langs, freq)
    plt.xlabel('BMI level')
    plt.ylabel('Distribution')
    plt.show()
    # Histogram
    plt.hist(bmi, bins=4)
    plt.xticks([13, 18.5, 25, 30, 38])
    plt.xlabel('BMI level')
    plt.ylabel('Distribution')
    plt.show()
    # Pie Chart
    plt.pie(freq, labels=langs, autopct='%1.2f%%')
    plt.show()
    # Scatter Plot
    plt.scatter(wt, ht, color='b')
    plt.xlabel('Height')
    plt.ylabel('Weight')
    plt.show()


if __name__ == "__main__":
    main()
