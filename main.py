# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def learn():
    # 导入sklearn数据集的库
    import sklearn
    # 查看sklearn的版本
    sklearn.__version__

    # 导入数据集
    from sklearn.datasets import load_iris
    data = load_iris()
    print(data.DESCR)
    X = data.data
    print(X)
    y = data.target
    print(y)

    # 划分数据集
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(X_train)
    print(X_test)
    print(y_train)
    print(y_test)

    # 导入算法构建模型
    from sklearn.tree import DecisionTreeClassifier
    # 初始化模型
    tree_clf = DecisionTreeClassifier(max_depth=4, random_state=42)

    # 训练模型
    # X_train 训练集
    # y_train 训练集
    tree_clf.fit(X_train, y_train)

    # 预测数据
    # 预测结果
    predict_X = tree_clf.predict([X_test[0]])
    print(predict_X)
    # 测试结果
    y_test[0]
    print(y_test[0])

    # 评估模型
    score_Xy = tree_clf.score(X_test, y_test)
    print(score_Xy)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    learn()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
