# Homework 1
# 1 - Даны 2 действительных числа a и b. Получить их сумму, разность и
# произведение (You are given two real numbers a and b. Get their sum,
# difference and product)

a = 3
b = 2

print(a + b)
print(a - b)
print(a * b)

# 2 - Даны действительные числа x и y. Получить 1+|xy|/|x|−|y|
# (You are given real numbers x and y. Get 1+|xy|/|x|−|y|)

x = 3
y = 2

print((x - y) / (1 + x * y))

# 3 - Дана длина ребра куба. Найти объем куба и площадь его боковой
# поверхности (The length of the edge of the cube is given. Find the
# volume of a cube and the area of its lateral surface)

''' Дана длина ребра куба, допустим она равна 7
    (Given the length of the edge of the cube, let's say it is 7)
    Далее ищем sb (площадь боковой поверхности)
    (Next, we look for sb (lateral surface area))
    Далее ищем v (обьем куба)
    (Next, we are looking for v (volume of the cube))
    Исходя из первого действия площадь боковой поверхности равна 28
    (Based on the first action, the lateral surface area is 28)
    Исходя из второго действия обьем куба равен 168
    (Based on the second action, the volume of the cube is 168) '''

lon = 7
print(lon * 4)

sb = 28
print(sb * 6)

# 4 - Даны два действительных числа. Найти среднее арифметическое и
# среднее геометрическое этих чисел (Two real numbers are given.
# Find the arithmetic mean and geometric mean of these numbers)

''' Мат. формула среднего арифметического (a+b)/2)
    (arithmetic mean formula (a + b) / 2))
    Мат. формула среднего геометрического √a*b
    (geometric mean formula √a * b)
    Что бы это посчитать, будем использовать модуль math
    (To calculate this, we will use the math module) '''

import math

a = 5
b = 6

print((a + b) / 2)
print(math.sqrt(a * b))

# 5 - Даны катеты прямоугольного треугольника. Найти его гипотенузу и
# площадь (The legs of a right-angled triangle are given. Find its hypotenuse and area)

''' Ищем гипотенузу по формуле корня суммы квадратов катета
    (We are looking for the hypotenuse by the formula of the root of the sum of the squares of the leg)
    Ищем площадь треугольника через половину произведения корней его катетов
    (We are looking for the area of a triangle through half the product of the roots of its legs) '''

import math

a = 3
b = 4

print(math.sqrt((a * a) + (b * b)))
print(((a * a) + (b * b)) / 2)
