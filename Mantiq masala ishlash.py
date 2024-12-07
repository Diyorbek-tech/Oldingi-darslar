# a = int(input('a='))
# b = int(input('b='))
# c = int(input('c='))
# t = a < b < c or c < b < a
# print(t)

# 8
# a= int(input('a='))
# b= int(input('b='))
# t= a%2==1 and b%2==1
# print(t)
# ctrl+alt+l
# 10
# a = int(input('a='))
# b = int(input('b='))
# t = (a % 2 == 1 and b % 2 == 0) or (a % 2 == 0 and b % 2 == 1)
# t = a % 2 != b % 2
# 11
# a = int(input('a='))
# b = int(input('b='))
# C = a%2 == b%2
# print(C)

# 12
# a, b, c = map(int, input().split(' '))
#
# D = a > 0 and b > 0 and c > 0
# print(D)

# 15
# a, b, c = map(int, input().split(' '))
# d = (a > 0 and b > 0 and c < 0) or (b > 0 and c > 0 and a < 0) or (a > 0 and c > 0 and b < 0)
# print(d)

# 17

# a = int(input('a='))
# t= (a//100%10)>=1 and a%2==1
# print(t)

# n = int(input('n=')) #123
# birlar = n % 10
# onlar = n // 10 % 10
# yuzlar = n // 100
# t = birlar != onlar != yuzlar
# print(t)

# 24
#
# d = b ** 2 - 4 * a * c
# t = d > 0
# print(t)
#

# 25
# x, y = map(int, input().split(' '))
# t = x < 0 and y > 0
# print("Javob:", t)

# # 34
# x, y = map(int, input().split(' '))
# t = (x + y) % 2 == 1  # son toq bolsa demak rang ham oq boladi
# print("Maydon oqligi ", t)

# 35
# x1, y1, x2, y2 = map(int, input().split(' '))
# t = (x1 + y1) % 2 == (x2 + y2) % 2
# print("bir hil rangdaligi ", t)

# 36
# x1, y1, x2, y2 = map(int, input().split(' '))
# t = x1 == x2 or y1 == y2
# print("Javob ", t)

# 37 -38
# x1, y1, x2, y2 = map(int, input().split(' '))
# t = (abs(x1 - x2) == abs(y1 - y2)) or (x1 == x2 or y1 == y2)
# print("Javob ", t)

# 40
x1, y1, x2, y2 = map(int, input().split(' '))
t = (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2)
print("Javob ", t)
