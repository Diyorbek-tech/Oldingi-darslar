"""
  x    y      AND         OR
False False   False       False
False True    False       True
True  False   False       True
True  True    True        True


 x        NOT
True     False
False    True

"""

# a, b, c, d = 2, 5, 7, 1
# t = a < 3 and not (c % b == 1 or a == 2 and d ** a == 1)
# print(t)

# begin 9
# import math
#
# a = int(input('a='))
# b = int(input('b='))
# G = math.sqrt(a * b)
# G1 = (a * b) ** 0.5
# print("O'rata geometriki: ", G)
# print("O'rata geometriki: ", G1)
#
# #
# R1 = int(input('R1='))
# R2 = int(input('R2='))
# pi = math.pi
# S1 = pi * R1 ** 2
# S2 = pi * R2 ** 2
# S3 = S1 - S2
# print("S1-S2= ", S3)
#
#
# n = int(input('n='))  # 21=3
# birlik = n % 10
# onlik = n // 10
# print(birlik + onlik)

# 123

# 1
n = int(input('n='))  # 21  12=1*10+2
birlik = n % 10
onlik = n // 10
print(birlik * 10 + onlik)
# 2
c = birlik
birlik = onlik
onlik = c
print(onlik * 10 + birlik)
# 3
a = 2
b = 3
print(a,b)
a, b = b, a
print(a,b)
