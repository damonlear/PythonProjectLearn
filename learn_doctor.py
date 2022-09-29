# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def learn():

    # 导入sklearn数据集的库
    import sklearn
    # 查看sklearn的版本
    sklearn.__version__

    # 导入数据
    # 导入数据集
    from sklearn.datasets import load_breast_cancer
    # 加载breast_cancer数据集到data中
    data = load_breast_cancer()
    print('---------------------------')
    # 数据集简介
    print(data.DESCR)
    # 获取X和y数据
    # 原始特征数据
    X = data.data
    print(X)
    # 原始目标数据
    y = data.target
    print(y)

    # 划分数据集（划分 训练数据 和 测试数据）
    from sklearn.model_selection import train_test_split
    # 使用train_test_split划分数据，随机采样
    # 把原始数据放进来
    # test_size=测试集占整个数据集的占比20% （test_size + train_size = 100% ）
    # random_state随机总和，保证数据源同时放进来，且保证X和y采顺序一致
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # 特征数据X训练集原始数据
    print(X_train)
    # 特征数据X测试集原始数据
    print(X_test)
    # 目标数据y训练集原始数据
    print(y_train)
    # 目标数据y训练集原始数据
    print(y_test)

    # 导入算法构建模型【重点】
    # DecisionTreeClassifier是一个算法模型的库
    from sklearn.tree import DecisionTreeClassifier
    # 初始化模型
    # 最大深度max_depth重要参数
    # 得到一个初始化的算法模型
    tree_clf = DecisionTreeClassifier(max_depth=30, random_state=42)

    # 训练模型
    # tree_clf函数做计算，找X_train和y_train训练集之间的映射关系，认为这个关系可以代表所有的数据
    # X_train 训练集
    # y_train 训练集
    tree_clf.fit(X_train, y_train)

    # 预测数据
    # 预测结果
    # 一个完全没有用过的用来做测试验证的数据
    # 索引表示的是目标数据集的类[0000,111,222]
    X_test[1]
    predict_X = tree_clf.predict([X_test[1]])
    print(predict_X)
    # 测试结果
    y_test[1]
    print(y_test[1])

    # 评估模型(统计结果)
    score_Xy = tree_clf.score(X_test, y_test)
    print(score_Xy)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    learn()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
