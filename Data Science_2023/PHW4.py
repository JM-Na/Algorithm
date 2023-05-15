import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

pd.set_option('display.max_columns', None)


def main():
    df = pd.read_csv("C://Users//-//Downloads//archive//mouse.csv", header=0)
    df.columns = ["x", "y"]
    for n in (2, 3, 4, 5, 6):
        for m in (50, 100, 200, 300):
            k_mean(df, n, m)


def k_mean(df, n, m):
    kmeans = KMeans(n_clusters=n, max_iter=m).fit(df)
    centroids = kmeans.cluster_centers_
    print(centroids)
    # 노이즈 구분을 위한 거리 계산
    dist = np.min(kmeans.transform(df), axis=1)
    # 노이즈 임계값 설정
    eps = np.percentile(dist, q=96)
    # 노이즈 추출
    noise_points = df[dist >= eps]

    plt.scatter(df['x'], df['y'], c=kmeans.labels_.astype(float),
                s=50, alpha=0.5)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
    plt.scatter(noise_points['x'], noise_points['y'], c='black', s=50)
    plt.title("K-means clustering (n_clusters={}, max_iter={})".format(n, m))
    plt.show()


if __name__ == "__main__":
    main()