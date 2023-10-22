from math import sqrt

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

one.sort()
two.sort()
three.sort()

max1 = one[-1]
max2 = two[-1]
max3 = three[-1]
p = (max1 + max2 + max3)/2
maxS = sqrt(p * (p - max1) * (p - max2) * (p - max3))
print(f'Площадь треугольника из максимальных элементов списков: {maxS}')

min1 = one[0]
min2 = two[0]
min3 = three[0]
p = (min1 + min2 + min3)/2
minS = sqrt(p * (p - min1) * (p - min2) * (p - min3))
print(f'Площадь треугольника из минимальных элементов списков: {minS}')
