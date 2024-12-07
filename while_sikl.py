"""
 for i in range(10)
While -shart sikl operatori

while shart: # shart =true
    # sikl ichki codlari

"""
# while True:
#     print("salom")

# # while1
# a = int(input('a='))
# b = int(input('b='))
# while a > b:
#     a = a - b
# print(a)
#
# # while2
# a = int(input('a='))
# b = int(input('b='))
# counter = 0
# while a > b:
#     a = a - b
#     counter += 1
# print(counter)

# ----------------------------------------------------------------

""" 
break-sindirish,chiqish
continue- davom qilish
"""

# for i in range(10):
#     if i == 5:
#         continue
#     print(i)

# while 6
# a = 1
# while 100 > a > 1:
#     a += 1
#     if a == 10:
#         break
#     elif a == 5:
#         continue
#     print(a)
# else:
#     print("while operatori sharti yolg'onga aylanib to'xtadi")

# while 5
# n = int(input("n="))
# counter = 0
# while n >= 2:
#     n = n // 2
#     counter += 1
# print(counter)

# while 7
# n = int(input("n="))
# a = 1
# y = 0
# k = 0
# while y < n:
#     y += a
#     a += 2
#     k += 1
# print(k)

# while 8
# n = int(input("n="))
# a = 1
# y = 0
# k = 0
# while y < n:
#     y += a
#     a += 2
#     k += 1
# print(k-1)

# print((int(input()) + int(input())) % 24)
# print([chr(i) for i in range(65,91)])

# while True:
#     ism = input('Ismingizni kiriting>>>')  # Abror
#     ism_valid = len([ord(i) for i in ism if not (90 > ord(i) >= 65 or 97 < ord(i) < 122)]) > 0
#     if ism[0] in [chr(i) for i in range(65, 91)] and not (ism_valid):
#         print(f"{ism} xush kelibsiz!!!")
#         break
#     else:
#         print("Bu ism emas. Iltimos tekshirib qaytadan kiriting!!!")


# import random

# ball = 0
# while True:
#     numberss = [i for i in range(1, 10)]
#     amallar = ['+', '-', '/', '*']
#     a = random.choice(numberss)
#     b = random.choice(numberss)
#     amal = random.choice(amallar)
#     if amal == '-' and a < b:
#         a, b = b, a
#     if amal == '/':
#         a = a * b
#     print(f"{a}{amal}{b}=", end=' ')
#     javob = int(input())
#     if eval(f"{a}{amal}{b}") == javob:
#         ball += 1
#         print(f"To'g'ri!!! Balingiz: {ball}")
#     else:
#         ball -= 1
#         print(f"Xato!!! Balingiz: {ball}")
#         continue
#     if ball > 10:
#         print("Siz yutdingiz!!! Ball:10")
#         break
# while 15
S = float(input('S:'))
p = int(input('0<p<25:'))
BS = S
k = 0
while BS < 2 * S:
    BS += (BS * p / 12) / 100
    k += 1
print(k, BS)

#while 17
n, m = map(int, input().split(' '))
butun = 0
while n > m:
    n -= m
    butun += 1
print(butun, n)

#while 18
n = int(input('n:'))
while n > 0:
    print(n % 10, end='')
    n //= 10


n = input()  # 214234
s = len([i for i in n if int(i) % 2 == 0]) == 0 and len(n) % 2 == 1
print("YES") if s else print("NO")
