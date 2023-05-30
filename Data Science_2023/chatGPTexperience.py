import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 주어진 데이터셋을 데이터프레임으로 생성
data = {
    'District': ['Suburban', 'Suburban', 'Rural', 'Urban', 'Urban', 'Urban', 'Rural', 'Suburban', 'Suburban', 'Urban', 'Suburban', 'Rural', 'Rural', 'Urban'],
    'House Type': ['Detached', 'Detached', 'Detached', 'Semi-detached', 'Semi-detached', 'Semi-detached', 'Semi-detached', 'Terrace', 'Semi-detached', 'Terrace', 'Terrace', 'Terrace', 'Detached', 'Terrace'],
    'Income': ['High', 'High', 'High', 'High', 'Low', 'Low', 'Low', 'High', 'Low', 'Low', 'Low', 'High', 'Low', 'High'],
    'Previous Customer': ['No', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes'],
    'Outcome': ['Not responded', 'Not responded', 'Responded', 'Responded', 'Responded', 'Not responded', 'Responded', 'Not responded', 'Responded', 'Responded', 'Responded', 'Responded', 'Responded', 'Not responded']
}

df = pd.DataFrame(data)

# 문자열 특성을 숫자로 변환
label_encoder = LabelEncoder()
for column in df.columns:
    if df[column].dtype == object:
        df[column] = label_encoder.fit_transform(df[column])

# 특성과 타겟 데이터를 분리
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Entropy 계산 함수
def compute_entropy(y):
    classes, counts = np.unique(y, return_counts=True)
    probabilities = counts / len(y)
    entropy = -np.sum(probabilities * np.log2(probabilities))
    return entropy

# 정보이득 계산 함수
def compute_information_gain(X, y, feature):
    feature_values = np.unique(X[:, feature])
    entropy_parent = compute_entropy(y)
    weighted_avg_entropy_children = 0
    for value in feature_values:
        X_subset = X[X[:, feature] == value]
        y_subset = y[X[:, feature] == value]
        entropy_child = compute_entropy(y_subset)
        weight = len(X_subset) / len(X)
        weighted_avg_entropy_children += weight * entropy_child
    information_gain = entropy_parent - weighted_avg_entropy_children
    return information_gain

# 트리 노드 클래스
class TreeNode:
    def __init__(self, feature=None, threshold=None, value=None, left=None, right=None):
        self.feature = feature
        self.threshold = threshold
        self.value = value
        self.left = left
        self.right = right

# 의사결정 트리 생성 함수
def create_decision_tree(X, y, depth=0, max_depth=None):
    # 리프 노드 생성
    if depth == max_depth or len(np.unique(y)) == 1:
        value = np.bincount(y).argmax()
        return TreeNode(value=value)

    num_features = X.shape[1]
    best_feature = None
    best_threshold = None
    max_info_gain = -np.inf

    for feature in range(num_features):
        thresholds = np.unique(X[:, feature])
        for threshold in thresholds:
            left_indices = np.where(X[:, feature] <= threshold)[0]
            right_indices = np.where(X[:, feature] > threshold)[0]
            info_gain = compute_information_gain(X, y, feature)
            if info_gain > max_info_gain:
                max_info_gain = info_gain
                best_feature = feature
                best_threshold = threshold
                best_left_indices = left_indices
                best_right_indices = right_indices

    # 분할한 데이터로 자식 노드 생성
    left_node = create_decision_tree(X[best_left_indices], y[best_left_indices], depth + 1, max_depth)
    right_node = create_decision_tree(X[best_right_indices], y[best_right_indices], depth + 1, max_depth)

    return TreeNode(feature=best_feature, threshold=best_threshold, left=left_node, right=right_node)

# 트리 구조 출력 함수
def print_tree(node, depth=0):
    indent = "  " * depth
    if node.value is not None:
        print(f"{indent}Outcome: {label_encoder.inverse_transform([node.value])[0]}")
    else:
        print(f"{indent}{list(df.columns[node.feature])} <= {node.threshold}")
        print_tree(node.left, depth + 1)
        print_tree(node.right, depth + 1)

# Decision Tree 생성
decision_tree = create_decision_tree(X.values, y.values, max_depth=3)

# 트리 구조 출력
print("Decision Tree Structure:")
print_tree(decision_tree)

# 주어진 조건에 따른 마케팅 결과 예측
def predict_outcome(node, sample):
    if node.value is not None:
        return label_encoder.inverse_transform([node.value])[0]
    if sample[node.feature] <= node.threshold:
        return predict_outcome(node.left, sample)
    else:
        return predict_outcome(node.right, sample)

# 예측할 샘플 데이터
sample = np.array([2, 0, 1, 1])  # [District, House Type, Income, Previous Customer]

# 주어진 조건에 따른 마케팅 결과 예측
predicted_outcome = predict_outcome(decision_tree, sample)
print("\nPredicted Outcome:", predicted_outcome)

