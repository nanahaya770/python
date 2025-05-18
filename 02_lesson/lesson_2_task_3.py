import math


def square(side):
    S = side * side
    return math.ceil(S)


side = float(input("введите сторону квадрата "))
print(f"площадь квадрата равна = {square(side)}")
