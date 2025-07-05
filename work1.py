import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score, f1_score, classification_report, log_loss
import matplotlib.pyplot as plt
import seaborn as sns

# 读取数据
file_path = r"D:\通用文件夹\空间分析项目\8.10\提交草稿\B1728数据\问卷点指标计算结果.xlsx"
data = pd.read_excel(file_path, skiprows=1)

# 根据列的顺序提取特征和目标
X = data.iloc[:, 1:6]
y = data.iloc[:, 6].astype(int)

# 分割数据集为训练集和测试集，测试集比例减少到10%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# 使用GridSearchCV来优化超参数，并限定树的深度
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [2, 3, 4],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2]
}

rf = RandomForestClassifier(random_state=42)
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=3, n_jobs=-1, scoring='accuracy')
grid_search.fit(X_train, y_train)

# 获取最佳模型
best_rf = grid_search.best_estimator_
print("Best parameters found by GridSearchCV:")
print(grid_search.best_params_)

# 训练最佳模型
best_rf.fit(X_train, y_train)

# 预测和评估模型
y_pred = best_rf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')
print(f"Accuracy: {accuracy}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# 特征重要性
feature_importances = best_rf.feature_importances_
feature_names = ['Road Ratio', 'Building Ratio', 'Greenery Ratio', 'Sky Ratio', 'Sunlight Ratio']
features_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importances})
features_df = features_df.sort_values(by='Importance', ascending=False)
print("Feature Importances:")
print(features_df)

# 可视化特征重要性
plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=features_df)
plt.title('Feature Importances')
plt.show()

