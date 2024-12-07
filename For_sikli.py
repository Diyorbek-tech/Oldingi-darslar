"""
Pythonda 2 xil sikl operatori bor  For and While
                        for sikl operatori

for value in [1,2,3,4,5,6,7,8,9]:
    print(value)


1) range(end)  [0,1,2....end-1]
2) range(start,end)  [start.....end-1]
3) range(start,end,step)  [start,start+step,.....end-1]


 """
# s = 0
# for i in range(11):  # range(start,end,step)
#     s += i
# print('yig\'indi',s)

# for1
# n, k = map(int, input().split(' '))
# for i in range(n):
#     print(k, end=' ')

# for3
# counter = 0
# a, b = map(int, input().split(' '))
# for i in range(a+1, b).__reversed__():
#     print(i, end=' ')
#     counter += 1
# print('count=', counter)


# # for5
# narx = float(input('narx='))
# for i in range(1, 11):
#     gram = i / 10
#     print(f"{gram * 1000} gram kanfet {gram * narx} so'm bo'ladi")

#
# # for 7
# a, b = map(int, input().split(' '))
# yigindi = 0
# for i in range(a, b):
#     yigindi += i
# print(yigindi)
#
#
# # for 8
# a, b = map(int, input().split(' '))
# kopaytma = 1
# for i in range(a, b):
#     kopaytma *= i
# print(kopaytma)
#
# # for 9
# a, b = map(int, input().split(' '))
# yigindi = 0
# for i in range(a, b):
#     yigindi += i**2
# print(yigindi)


# for 18
n = int(input('n='))
a = float(input('a='))
yigindi = 0
for i in range(n):
    yigindi += ((-1) ** i) * (a ** i)
print(yigindi)
