# 指数平滑算法
def exponential_smoothing(alpha, s):
    #     一次指数平滑
    #     :param alpha:  平滑系数
    #     :param s:      数据序列， list
    #     :return:       返回一次指数平滑模型参数， list

    s_temp = [0 for i in range(len(s))]
    s_temp[0] = (s[0] + s[1] + s[2]) / 3
    for i in range(1, len(s)):
        s_temp[i] = alpha * s[i] + (1 - alpha) * s_temp[i - 1]
    return s_temp


def compute_single(alpha, s):
    #     一次指数平滑
    #     :param alpha:  平滑系数
    #     :param s:      数据序列， list
    #     :return:       返回一次指数平滑模型参数， list

    return exponential_smoothing(alpha, s)


def compute_double(alpha, s):
    #     '''
    #     二次指数平滑
    #     :param alpha:  平滑系数
    #     :param s:      数据序列， list
    #     :return:       返回二次指数平滑模型参数a, b， list
    #     '''
    s_single = compute_single(alpha, s)
    s_double = compute_single(alpha, s_single)

    a_double = [0 for i in range(len(s))]
    b_double = [0 for i in range(len(s))]

    for i in range(len(s)):
        a_double[i] = 2 * s_single[i] - s_double[i]  # 计算二次指数平滑的a
        b_double[i] = (alpha / (1 - alpha)) * (s_single[i] - s_double[i])  # 计算二次指数平滑的b

    return a_double, b_double


def compute_triple(alpha, s):
    #     '''
    #     三次指数平滑
    #     :param alpha:  平滑系数
    #     :param s:      数据序列， list
    #     :return:       返回三次指数平滑模型参数a, b, c， list
    #     '''
    s_single = compute_single(alpha, s)
    s_double = compute_single(alpha, s_single)
    s_triple = exponential_smoothing(alpha, s_double)

    a_triple = [0 for i in range(len(s))]
    b_triple = [0 for i in range(len(s))]
    c_triple = [0 for i in range(len(s))]

    for i in range(len(s)):
        a_triple[i] = 3 * s_single[i] - 3 * s_double[i] + s_triple[i]
        b_triple[i] = (alpha / (2 * ((1 - alpha) ** 2))) * (
                    (6 - 5 * alpha) * s_single[i] - 2 * ((5 - 4 * alpha) * s_double[i]) + (4 - 3 * alpha) * s_triple[i])
        c_triple[i] = ((alpha ** 2) / (2 * ((1 - alpha) ** 2))) * (s_single[i] - 2 * s_double[i] + s_triple[i])

    return a_triple, b_triple, c_triple


if __name__ == "__main__":
    alpha = 0.8
    next_T = 1
    data = [i for i in range(100)]

    sigle = compute_single(alpha, data)
    prediction = alpha * data[-1] + (1 - alpha) * sigle[-1]
    print(prediction)

    double_a, double_b = compute_double(alpha, data)
    prediction = double_a[-1] + double_b[-1] * next_T
    print(prediction)

    triple_a, triple_b, triple_c = compute_triple(alpha, data)
    prediction = triple_a[-1] + triple_b[-1] * next_T + triple_c[-1] * (next_T ** 2)
    print(prediction)
