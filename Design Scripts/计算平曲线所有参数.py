import math

print('Authorized by xiejiye and zhangxuhui')


class calc:
    def __init__(self, Ls, R, angle):
        self.Ls = Ls
        self.R = R
        self.angle = angle

    def qieXianZenChang_q(self):
        q = self.Ls / 2 - self.Ls ** 3 / (240 * self.R ** 2)
        print('切线增长值q', q)
        return q

    def neiYi_p(self):
        p = self.Ls ** 2 / (24 * self.R) - self.Ls ** 4 / (2688 * self.R ** 3)
        print('内移值p', p)
        return p

    def beiTa_b(self):
        b = self.Ls / (2 * self.R) * (180 / math.pi)
        print('b', b)
        return b

    def qieXian_T(self):
        T = (self.R + calc.neiYi_p(self)) * math.tan((self.angle * math.pi) / 360) + calc.qieXianZenChang_q(self)
        print('切线长T', T)
        return T

    def pingQuXian_L(self):
        L = ((self.angle - 2 * calc.beiTa_b(self)) * math.pi / 180) * self.R + 2 * self.Ls
        print('平曲线长L', L)
        return L

    def HuiXuanXianPar_A(self):
        A = math.sqrt(self.R * self.Ls)
        print('缓和曲线参数A', A)
        return A

    def waiJu(self):
        E = (self.R + calc.neiYi_p(self)) * (1 / math.cos(math.radians(self.angle) / 2)) - self.R
        print('外距E', E)
        return E

    def qieQucha(self):
        J = 2 * calc.qieXian_T(self) - calc.pingQuXian_L(self)
        print('切曲差J', J)
        return J


x0 = 280076.4
y0 = 191193.0
x1 = 280212.0
y1 = 191540.0
x2 = 280505.0
y2 = 191508.0
x3 = 280526.4
y3 = 191932.0


# print("输入五个点的坐标\n")
# x0 = input('x0\n')
# y0 = input('y0\n')
# x1 = input('x1\n')
# y1 = input('y1\n')
# x2 = input('x2\n')
# y2 = input('y2\n')
# x3 = input('x3\n')
# y3 = input('y3\n')
# x4 = input('x4\n')
# y4 = input('y4\n')
#
# x0 = float(x0)
# y0 = float(y0)
# x1 = float(x1)
# y1 = float(y1)
# x2 = float(x2)
# y2 = float(y2)
# x3 = float(x3)
# y3 = float(y3)
# x4 = float(x4)
# y4 = float(y4)


def calc_Distance(delta_x, delta_y):
    print("计算交点间距")
    L = math.sqrt(delta_x ** 2 + delta_y ** 2)
    print(L)
    return L


def calc_Fangweijiao(delta_x, delta_y):
    if delta_x > 0 and delta_y > 0:
        alpha = math.degrees(math.atan(math.fabs(delta_y) / math.fabs(delta_x)))
    if delta_x < 0 and delta_y > 0:
        alpha = 180 - math.degrees(math.atan(math.fabs(delta_y) / math.fabs(delta_x)))
    if delta_x < 0 and delta_y < 0:
        alpha = 180 + math.degrees(math.atan(math.fabs(delta_y) / math.fabs(delta_x)))
    if delta_x > 0 and delta_y < 0:
        alpha = 360 - math.degrees(math.atan(math.fabs(delta_y) / math.fabs(delta_x)))
    print('方位角', alpha)
    return alpha


def calc_Zhuanjiao(alpha2, alpha1):
    turn_angle = alpha2 - alpha1
    if alpha2 > 300:
        turn_angle = 360 - alpha2 + alpha1
    elif alpha1 > 300:
        turn_angle = 360 - alpha1 + alpha2
    res = math.fabs(turn_angle)
    print('转角', res)
    return res


R1 = 120
Ls1 = 66
R2 = 120
Ls2 = 75
# R3 = 80
# Ls3 = 36.9356
# R1 = input("输入R1\n")
# R2 = input("输入R2\n")
# R3 = input("输入R3\n")
# R1 = float(R1)
# R2 = float(R2)
# R3 = float(R3)
#
# Ls1 = input("输入Ls1\n")
# Ls2 = input("输入Ls2\n")
# Ls3 = input("输入Ls3\n")
# Ls1 = float(Ls1)
# Ls2 = float(Ls2)
# Ls3 = float(Ls3)

print("计算平曲线要素\n")
JD1 = calc(Ls1, R1, calc_Zhuanjiao(calc_Fangweijiao(x2 - x1, y2 - y1),
                                   calc_Fangweijiao(x1 - x0, y1 - y0)))  # turn_angle后面用函数嵌套计算出来
JD1.qieXianZenChang_q()
JD1.neiYi_p()
JD1.beiTa_b()
JD1.qieXian_T()
JD1.pingQuXian_L()
JD1.waiJu()
JD1.qieQucha()
JD1.HuiXuanXianPar_A()
print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

JD2 = calc(Ls2, R2, calc_Zhuanjiao(calc_Fangweijiao(x3 - x2, y3 - y2),
                                   calc_Fangweijiao(x2 - x1, y2 - y1)))
JD2.qieXianZenChang_q()
JD2.neiYi_p()
JD2.beiTa_b()
JD2.qieXian_T()
JD2.pingQuXian_L()
JD2.waiJu()
JD2.qieQucha()
JD2.HuiXuanXianPar_A()
print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

# JD3 = calc(Ls3, R3, calc_Zhuanjiao(calc_Fangweijiao(x4 - x3, y4 - y3),
#                                    calc_Fangweijiao(x3 - x2, y3 - y2)))
# JD3.qieXianZenChang_q()
# JD3.neiYi_p()
# JD3.beiTa_b()
# JD3.qieXian_T()
# JD3.pingQuXian_L()
# JD3.waiJu()
# JD3.qieQucha()
# JD3.HuiXuanXianPar_A()
# print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

QDZH = 5140
JD1ZH = QDZH + calc_Distance(x1-x0, y1-y0)
print('JD1ZH:', JD1ZH)
JD2ZH = JD1ZH + calc_Distance(x2-x1, y2-y1) - JD1.qieQucha()
print('JD2ZH:', JD2ZH)
# JD3ZH = JD2ZH + calc_Distance(x3-x2, y3-y2) - JD2.qieQucha()
# print('JD3ZH:', JD3ZH)
ZDZH = JD2ZH + calc_Distance(x3-x2, y3-y2) - JD2.qieQucha()
print('ZDZH:', ZDZH)
print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
ZH1ZH = JD1ZH - JD1.qieXian_T()
print('ZH1ZH', ZH1ZH)
HY1ZH = ZH1ZH + Ls1
print('HY1ZH', HY1ZH)
QZ1ZH = ZH1ZH + JD1.pingQuXian_L()/2
print('QZ1ZH', QZ1ZH)
HZ1ZH = ZH1ZH + JD1.pingQuXian_L()
print('HZ1ZH', HZ1ZH)
YH1ZH = HZ1ZH - Ls1
print('YH1ZH', YH1ZH)
print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
ZH2ZH = JD2ZH - JD2.qieXian_T()
print('ZH2ZH', ZH2ZH)
HY2ZH = ZH2ZH + Ls2
print('HY2ZH', HY2ZH)
QZ2ZH = ZH2ZH + JD2.pingQuXian_L()/2
print('QZ2ZH', QZ2ZH)
HZ2ZH = ZH2ZH + JD2.pingQuXian_L()
print('HZ2ZH', HZ2ZH)
YH2ZH = HZ2ZH - Ls2
print('YH2ZH', YH2ZH)
print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
# ZH3ZH = JD3ZH - JD3.qieQucha()
# print('ZH3ZH', ZH3ZH)
# HY3ZH = ZH3ZH + Ls3
# print('HY3ZH', HY3ZH)
# QZ3ZH = ZH3ZH + JD3.pingQuXian_L()/2
# print('QZ3ZH', QZ3ZH)
# HZ3ZH = ZH3ZH + JD3.pingQuXian_L()
# print('HZ3ZH', HZ3ZH)
# YH3ZH = HZ3ZH - Ls3
# print('YH3ZH', YH3ZH)

print(ZH2ZH - HZ1ZH)
