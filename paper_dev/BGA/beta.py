import math

# /*=============================================================
# // 函 数 名：gammln
# // 功能描述：求解伽马函数的值的自然对数
# // 输入参数：x 求值的自变量
# // 返 回 值：伽马函数的值的自然对数
# //==============================================================*/

def gammln(x):
    c = [76.18009172947148,
            -86.50532032941677,  24.01409824083091,
            -1.231739572450155,  0.1208650973866179e-2,
            -0.5395239384953e-5]
    if x < 0:
        print("incorrect input parameter")
        return 0
    s = 1.000000000190015
    for i in range(6):
        s = s + c[i]/(x+i)
    t = x + 4.5
    t = t - (x-0.5) * math.log(t)
    t = math.log(2.5066282746310005*s) - t
    return t



# // 函 数 名：beta2
# // 功能描述：求解不完全贝塔积分的值
# // 输入参数：a 自变量a的值。要求a>0。
# //           b 自变量b的值。要求b>0。
# //           x 自变量x的值，要求0<=x<=1。
# //           e1 精度要求，当两次递推的值变化率小于e1时，认为已收敛
# // 返 回 值：不完全贝塔函数的值
# //==============================================================*/

NMAX = 100
EULER = 0.5772156649
FPMIN = 1.0e-30

def beta2(a,b,x,e1):
    if x < 0.0 or x > 1.0 or a <= 0.0 or b <= 0.0:
        print("Bad input parameter")
        return 0
    elif x == 0.0:
        t = 0.0
        return t
    elif x == 1.0:
        t = 1.0
        return t
    elif x > (a+1.0)/(a+b+2.0):
        t = math.exp(gammln(a + b) - gammln(a) - gammln(b) + a * math.log(x) + b * math.log(1.0 - x))
        t = 1.0 - t * subf(b, a, 1.0 - x, e1)/b
        return t
    else:
        t = math.exp(gammln(a + b) - gammln(a) - gammln(b) + a * math.log(x) + b * math.log(1.0 - x))
        t = t * subf(a, b, x, e1) / a
        return t



def subf(a,b,x,e1):
    c = 1.0
    d = 1.0 - (a+b) * x / (a+1.0)
    if math.fabs(d) < FPMIN:
        d = FPMIN
    d = 1.0 / d
    t = d
    for n in range(1, NMAX):
        an = n * (b - n) * x / ((a + 2.0 * n - 1.0) * (a + 2.0 * n))
        d = an * d + 1.0
        c = 1.0 + an / c
        if math.fabs(d) < FPMIN:
            d = FPMIN
        if math.fabs(c) < FPMIN:
            c = FPMIN
        d = 1.0/d
        de = d*c
        t = t*de
        an = -(a + n) * (a + b + n) * x / ((a + 2.0 * n) * (a + 1.0 + 2.0 * n))
        d = 1.0 + an * d
        c = 1.0 + an / c
        if math.fabs(d) < FPMIN:
            d = FPMIN
        if math.fabs(c) < FPMIN:
            c = FPMIN
        d = 1.0 / d
        de = d * c
        t = t * de
        if math.fabs(de-1.0) < e1:
            return t
    print("iteration not converged.")
    return t

