# Задача 26: Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = int(input("введите число А : "))
a1 = a
b = int(input("введите число В : "))
count = 1
def st(x, y, z, w):
    
    if z == y:
        return x
    z += 1
    return st(x*w, y, z, w)

print(f' Итог = {st(a, b, count, a1)}')
