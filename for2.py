# s = [i for i in range(100)]
# print(s)
#
# s1=[]
# for i in range(100):
#     s1.append(i)
# print(s1)
#
s = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in s:
    for j in i:
        print(j)

S = [j for i in s for j in i]
print(S)












# for 10
n = int(input('n='))
s = 0
for i in range(1, n + 1):
    s += 1 / i
print(s)

# for 11
n = int(input('n='))
s = 0
for i in range(0, n + 1):
    s += (n + i) ** 2
print(s)

# for 12
n = int(input('n='))
k = 1
for i in range(1, n + 1):
    k *= (i + 10) / 10
print(k)

# # for 14
# n = int(input('n='))
# s = 0
# for i in range(1, n + 1):
#     s += (2*i-1)
#     print(f'{i}^2=', s)
# #
#
# # # for 15
# n = int(input('n='))
# a = float(input('k='))
# t = 1
# for i in range(n):
#     t *= a
# print(f'{a}^{n}=', t)
#
# # for 16
# n = int(input('n='))
# a = float(input('k='))
# for i in range(n + 1):
#     print(f'{a}^{i}=', a ** i)


# # for 20
# n = int(input('n='))
# f = 1
# s = 0
# for i in range(1, n + 1):
#     f *= i
#     s += f
# print(s)
#
# # for 21
# n = int(input('n='))
# f = 1
# s = 0
# for i in range(1, n + 1):
#     f *= i
#     s += 1 / f
# print(s)
#
#
# # for 22
# n = int(input('n='))
# x = float(input('x='))
# f = 1
# s = 1
# for i in range(1, n + 1):
#     f *= i
#     s += x**i / f
# print(s)
