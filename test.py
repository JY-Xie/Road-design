import math

print(math.tan(math.pi/4))
print(math.sin(math.radians(30)))
def angleChange():
    dgree = float(input("输入度"))
    minute = float(input("输入分"))
    second = float(input("输入秒"))
    dgree = dgree * 3600 + minute * 60 + second
    return math.radians(dgree/3600)
print(angleChange())