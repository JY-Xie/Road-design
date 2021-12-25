import math


angle = 32.9
angle = float(angle) * math.pi / 180
D1 = 758.96
D2 = 760.54

for Ls in range(360, 1000):
    for R in range(100, 1000):
        q = Ls/2 - Ls**3 / (240*R**2)
        p = Ls**2/(24*R) - Ls**4/(2688*R**3)
        T = (R+p)*math.tan(angle/2)+q

        A1 = math.sqrt(110*70)
        A2 = math.sqrt(R*Ls)

        if D1 - 111.63 - T > 360 and D2 - 58.94 - T > 360:
            print(Ls, '\n', R, '\n',  D1 - 111.63 - T, "success \n", D2 - 58.94 - T)
            print("p, q, T\n", p, q, T)
