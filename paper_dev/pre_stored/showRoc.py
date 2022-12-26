import pandas as pd  # 数据分析
import numpy as np  # 科学计算
from pandas import DataFrame
from sklearn import linear_model, neighbors, tree, svm
from sklearn import naive_bayes
from sklearn.model_selection import cross_val_score, train_test_split
import csv
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics


# 读取文件的第n行数据
def get_nthrow(nthrow):
    test = open('D:\OneDriveData\OneDrive - hnu.edu.cn\Scholar\师兄师姐小论文\paper_xmy\实验相关\paper_dev\dataset\Train.csv', 'r',
                newline='')
    reader = csv.reader(test)
    data = []
    for i, rows in enumerate(reader):
        if i == nthrow:
            row = rows  # type(row):list
            data.append(row)
            break
    test.close()
    data_f = DataFrame(data)
    return data_f


# 读取文件的第n-m行的数据
def get_nmthrow(n, m):
    test = open('D:\OneDriveData\OneDrive - hnu.edu.cn\Scholar\师兄师姐小论文\paper_xmy\实验相关\paper_dev\dataset\Test.csv', 'r',
                newline='')
    reader = csv.reader(test)
    data = []
    for i, rows in enumerate(reader):
        if i in range(n, m + 1):
            row = rows  # type(row):list
            data.append(row)
        if i > m:
            break
    test.close()
    data_f = DataFrame(data)
    print(data_f)
    return data_f


# 获取Train.csv文件的总行数
def file_rows_num():
    file = open('D:\OneDriveData\OneDrive - hnu.edu.cn\Scholar\师兄师姐小论文\paper_xmy\实验相关\paper_dev\dataset\Test.csv', 'r',
                newline='')
    reader = csv.reader(file)
    count = 0
    for i, rows in enumerate(reader):
        count = count + 1
    return count


# 读取n_rows行数据构建模型预测，预测下一个数据
def model_predict(n_rows):
    data_train = pd.read_csv("D:\OneDriveData\OneDrive - hnu.edu.cn\Scholar\师兄师姐小论文\paper_xmy\实验相关\paper_dev\dataset\Train.csv",
                             nrows=n_rows)  # 读取文件的前n_rows行
    data_train.dropna(axis=0, subset=['Is_edge'], inplace=True)
    train_y = data_train.Is_edge
    train_x = data_train.drop(['Is_edge'], axis=1).select_dtypes(exclude=['object'])

    # x_shuffle, y_shuffle = shuffle(x, y)

    clf1 = linear_model.LogisticRegression(C=1.0, penalty='l1', tol=1e-6)  # 0.706
    clf2 = linear_model.SGDClassifier(loss="hinge", penalty="l2")  # 0.588
    clf3 = svm.SVC(C=0.8, kernel='linear', gamma=20, decision_function_shape='ovr')  # 0.67
    clf4 = RandomForestClassifier(n_estimators=10, max_depth=2, random_state=0, bootstrap=True)  # 0.725
    clf5 = naive_bayes.GaussianNB()  # 0.616
    clf6 = neighbors.KNeighborsClassifier(n_neighbors=120, weights='distance')  # 0.67
    clf7 = tree.DecisionTreeClassifier()  # 0.858

    modelacc = []
    model_acc1 = np.mean(cross_val_score(clf1, train_x, train_y, cv=3))  # 模型精确度
    modelacc.append(model_acc1)
    model_acc2 = np.mean(cross_val_score(clf2, train_x, train_y, cv=3))  # 模型精确度
    modelacc.append(model_acc2)
    model_acc3 = np.mean(cross_val_score(clf3, train_x, train_y, cv=3))  # 模型精确度
    modelacc.append(model_acc3)
    model_acc4 = np.mean(cross_val_score(clf4, train_x, train_y, cv=3))  # 模型精确度
    modelacc.append(model_acc4)
    model_acc5 = np.mean(cross_val_score(clf5, train_x, train_y, cv=3))  # 模型精确度
    modelacc.append(model_acc5)
    model_acc6 = np.mean(cross_val_score(clf6, train_x, train_y, cv=3))  # 模型精确度
    modelacc.append(model_acc6)
    model_acc7 = np.mean(cross_val_score(clf7, train_x, train_y, cv=3))  # 模型精确度
    modelacc.append(model_acc7)

    clf = 0
    maxindex = modelacc.index(max(modelacc))
    if maxindex == 0:
        clf = clf1
    if maxindex == 1:
        clf = clf3
    if maxindex == 2:
        clf = clf4
    if maxindex == 3:
        clf = clf5
    if maxindex == 4:
        clf = clf6
    if maxindex == 5:
        clf = clf7

    # 获取下一个segment的feature值
    testData = get_nmthrow(n_rows + 1, n_rows + 200)
    test_x = testData.iloc[:, [0, 1, 2, 3]].values.astype(int)
    test_y = testData.iloc[:, [4]].values.astype(int)
    print(test_x)
    y_score = clf.fit(train_x, train_y).decision_function(test_x)
    # Compute ROC curve and ROC area for each class
    fpr, tpr, threshold = metrics.roc_curve(test_y, y_score)  ###计算真正率和假正率
    roc_auc = metrics.auc(fpr, tpr)  ###计算auc的值
    print(roc_auc)

    plt.figure()
    lw = 2
    plt.figure(figsize=(10, 10))
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)  ###假正率为横坐标，真正率为纵坐标做曲线
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right")
    plt.show()


def roc(test_size):
    data_train = pd.read_csv(
        "D:\OneDriveData\OneDrive - hnu.edu.cn\Scholar\师兄师姐小论文\paper_xmy\实验相关\paper_dev\dataset\Train.csv")  # 读取文件
    data_train.dropna(axis=0, subset=['Is_edge'], inplace=True)
    y = data_train.Is_edge
    X = data_train.drop(['Is_edge'], axis=1).select_dtypes(exclude=['object'])
    # print(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=0)

    clf1 = linear_model.LogisticRegression(C=1.0, penalty='l1', tol=1e-6, solver='liblinear')  # 0.706
    # clf2 = linear_model.SGDClassifier(loss="hinge", penalty="l2")  # 0.588
    # clf3 = svm.SVC(C=0.8, kernel='linear', gamma=20, decision_function_shape='ovr')  # 0.67
    # clf4 = RandomForestClassifier(n_estimators=10, max_depth=2, random_state=0, bootstrap=True)  # 0.725
    # clf5 = naive_bayes.GaussianNB()  # 0.616
    # clf6 = neighbors.KNeighborsClassifier(n_neighbors=120, weights='distance')  # 0.67
    clf7 = tree.DecisionTreeClassifier()  # 0.858

    modelacc = []
    model_acc1 = np.mean(cross_val_score(clf1, X_train, y_train, cv=3))  # 模型精确度
    modelacc.append(model_acc1)
    # model_acc2 = np.mean(cross_val_score(clf2, X_train, y_train, cv=3))  # 模型精确度
    # modelacc.append(model_acc2)
    # model_acc3 = np.mean(cross_val_score(clf3, X_train, y_train, cv=3))  # 模型精确度
    # modelacc.append(model_acc3)
    # model_acc4 = np.mean(cross_val_score(clf4, X_train, y_train, cv=3))  # 模型精确度
    # modelacc.append(model_acc4)
    # model_acc5 = np.mean(cross_val_score(clf5, X_train, y_train, cv=3))  # 模型精确度
    # modelacc.append(model_acc5)
    # model_acc6 = np.mean(cross_val_score(clf6, X_train, y_train, cv=3))  # 模型精确度
    # modelacc.append(model_acc6)
    model_acc7 = np.mean(cross_val_score(clf7, X_train, y_train, cv=3))  # 模型精确度
    modelacc.append(model_acc7)

    clf = clf1
    maxindex = modelacc.index(max(modelacc))
    if maxindex == 0:
        clf = clf1
    # if maxindex == 1:
    #     clf = clf2
    # if maxindex == 2:
    #     clf = clf3
    # if maxindex == 3:
    #     clf = clf4
    # if maxindex == 4:
    #     clf = clf5
    # if maxindex == 5:
    #     clf = clf6
    if maxindex == 6:
        clf = clf7
    #
    if clf == clf7:
        # print("yes-------")
        y_score = clf.fit(X_train, y_train).predict_proba(X_test)[:, 1]
    else:
        y_score = clf.fit(X_train, y_train).decision_function(X_test)
    # Compute ROC curve and ROC area for each class
    fpr, tpr, threshold = metrics.roc_curve(y_test, y_score)  ###计算真正率和假正率
    roc_auc = metrics.auc(fpr, tpr)  ###计算auc的值
    return fpr, tpr, roc_auc


def showRoc(fpr, tpr, roc_auc):
    lw = 2
    plt.figure(figsize=(10, 10))
    plt.plot(fpr[0], tpr[0], color='red',
             lw=lw, label='ROC curve of TS insurance set(area = %0.2f)' % roc_auc[0])  ###假正率为横坐标，真正率为纵坐标做曲线
    plt.plot(fpr[1], tpr[1], color='yellow',
             lw=lw, label='ROC curve of CP insurance set(area = %0.2f)' % roc_auc[1])  ###假正率为横坐标，真正率为纵坐标做曲线
    plt.plot(fpr[2], tpr[2], color='blue',
             lw=lw, label='ROC curve of CE insurance set(area = %0.2f)' % roc_auc[2])  ###假正率为横坐标，真正率为纵坐标做曲线

    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate', fontsize=22)
    plt.ylabel('True Positive Rate', fontsize=22)
    plt.xticks(size=18)
    plt.yticks(size=18)
    # plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right", prop={'size': 15})
    plt.show()


if __name__ == "__main__":
    res_fpr = []
    res_tpr = []
    res_auc = []
    for testsize in [200, 800, 1200]:
        fpr, tpr, roc_auc = roc(testsize)
        print(fpr, tpr, roc_auc)
        res_fpr.append(fpr)
        res_tpr.append(tpr)
        res_auc.append(roc_auc)
    showRoc(res_fpr, res_tpr, res_auc)
