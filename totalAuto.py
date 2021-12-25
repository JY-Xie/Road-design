import math


def angleChange(dgree, minute, second):
    # dgree = float(input("输入度"))
    # minute = float(input("输入分"))
    # second = float(input("输入秒"))
    dgree = dgree * 3600 + minute * 60 + second
    return math.radians(dgree / 3600)


class calc:
    def __init__(self, Ls, R, angle):
        self.Ls = Ls
        self.R = R
        self.angle = angle

    def qieXianZenChang_q(self):
        q = self.Ls / 2 - self.Ls ** 3 / (240 * self.R ** 2)
        print('q', q)
        return q

    def neiYi_p(self):
        p = self.Ls ** 2 / (24 * self.R) - self.Ls ** 4 / (2688 * self.R ** 3)
        print('p', p)
        return p

    def beiTa_b(self):
        b = self.Ls / (2 * self.R) * (180 / math.pi)
        print('b', b)
        return b

    def qieXian_T(self):
        T = (self.R + calc.neiYi_p(self)) * math.tan(self.angle / 2) + calc.qieXianZenChang_q(self)
        print('T', T)
        return T

    def pingQuXian_L(self):
        L = (self.angle * 180 / math.pi - 2 * calc.beiTa_b(self)) * math.pi / 180 * self.R + 2 * self.Ls
        print('L', L)
        return L

    def HuiXuanXianPar_A(self):
        A = math.sqrt(self.R * self.Ls)
        return A


class NoHuanHe:
    def __init__(self, R, angle):
        self.R = R
        self.angle = angle

    def qieXian_T(self):
        T = self.R * self.angle
        print('T', T)
        return T


if __name__ == '__main__':
    JD1 = calc(65, 300, angleChange(29, 30, 0))
    JD1.qieXianZenChang_q()
    JD1.neiYi_p()
    JD1.beiTa_b()
    JD1.qieXian_T()
    JD1.pingQuXian_L()
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

    JD2 = calc(160, 550, angleChange(32, 54, 0))
    JD2.qieXianZenChang_q()
    JD2.neiYi_p()
    JD2.beiTa_b()
    JD2.qieXian_T()
    JD2.pingQuXian_L()
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

    JD3 = NoHuanHe(2000, angleChange(4, 30, 0))
    JD3.qieXian_T()
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n以下为程序垃圾")
    if 758.96 - JD1.qieXian_T() - JD2.qieXian_T() > 360 and 760.54 - JD2.qieXian_T() - JD3.qieXian_T() > 360:
        print(1)
        if 0.333 < ((JD1.pingQuXian_L() - 65*2) / JD1.pingQuXian_L()) < 0.5 and (0.333 < (JD1.pingQuXian_L() - 160*2) / JD1.pingQuXian_L()) < 0.5:
            print("you are successful")
