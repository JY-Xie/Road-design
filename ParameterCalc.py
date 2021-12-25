import math


print("Please input the parameters of the road")
R = input("Please input the radius of the road\n")
angle = input("Please input the angle of the corner\n")

R = float(R)
angle = float(angle) * math.pi / 180

if input("choose the 1.calc-result of Ls or input your 2.Ls, input 1 or 2\n") == "1":
    Ls = (angle/2) * (math.pi/180) * R
    print(Ls)
else:
    Ls = input("Please input the length of the turn-road\n")
    Ls = float(Ls)

q = Ls/2 - Ls**3 / (240*R**2)
p = Ls**2/(24*R) - Ls**4/(2688*R**3)
T = (R+p)*math.tan(angle/2)+q

print("p, q, T\n", p, q, T)

A1 = math.sqrt(110*70)
A2 = math.sqrt(R*Ls)
if 0 < 267.71-T-157.11 < (A1 + A2)/40:
    print("success")
else:
    print("fail")

print(267.71-T-157.11, "\n", (A1 + A2)/40)
