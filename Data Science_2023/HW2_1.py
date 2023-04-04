import numpy as np
import pandas as pd


def main():
    a = pd.DataFrame({'0': [3., '?', 2., 5.], '1': ['*', 4., 5., 6.], '2': ['+', 3., 2., '&'], '3': [5., '?', 7., '!']})
    # original dataframe
    print('original data frame')
    print(a)
    print('------------')
    for i in range(0, 4):
        for j in range(0, 4):
            k = a.iloc[i][j]
            if type(k) != float:
                a.iloc[i][j] = np.NaN
    # dataframe replaced with NAN
    print('dataframe replaced with NAN')
    print(a)
    print('------------')
    # isna
    print('isna')
    print(a.isna())
    print('------------')
    # isna with any
    print('isna with any')
    print(a.isna().any())
    print('------------')
    # isna with sum
    print('isna with sum')
    print(a.isna().sum())
    print('------------')
    # dropna with all
    print('dropna with all')
    print(a.dropna(how='all'))
    print('------------')
    # dropna with any
    print('drop na with any')
    print(a.dropna(how='any'))
    print('------------')
    # fillna with 100
    print('fill na with 100')
    print(a.fillna(100))
    print('------------')
    # fillna with mean
    print('fill na with mean')
    print(a.fillna(a.mean()))
    print('------------')
    # fillna with median
    print('fill na with median')
    print(a.fillna(a.median()))
    print('------------')
    # ffill
    print('ffill')
    print(a.fillna(method='ffill'))
    print('------------')
    # bfill
    print('bfill')
    print(a.fillna(method='bfill'))
    print('------------')


if __name__ == "__main__":
    main()
