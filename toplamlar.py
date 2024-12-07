# """
# List-malumot tipi
# List belgisi []
# Toplam-Ma'lum bir sinfga tegishli va malum maqsadda yigilgan malumotlar
# (qiymatlar yoki ozgaruvchilar) dan tashkil topgan ro'yxat
#
# Listda malumotlar ,(belgul) bilan ajratilib yoziladi [1,2,3,4]
#
# listda elementlar indexlangan boladi va index-0 dan boshlidi
#
# """
# raqamlar = [1, 5, 7, 4, 5, 6]
# sozlar = ['salom', 'xayr', 'dost', 'odam', 'akbar']
# print(raqamlar[-1])
# raqamlar.append(0)  # listga ohiridan element qoshish
# raqamlar[1] = 10 # update ('o'zgartirish yoki qiymatni yangilash')
# a=raqamlar.pop(4) # listdan berilgan indexdagi qiymatni yulib oladi va shu qiymatni qaytaradi, ozgaruvchiga yuklash mumkin
# print(f"{a} ni listdan ochirdim va a ga yukladim")
# raqamlar.insert(2,20)# listga belgilangan indexiga qiymat kiritish
# a = raqamlar.index(6) # qiymat joylashgan indexni qaytaradi
# sozlar.sort()  # tartiblash
# a = raqamlar.count(6) # berilgan qiymat toplam ichida necha marta takrorlanganini sonini qaytaradi
# print(a)
# raqamlar.clear()# toplamni tozalash uchun ishlatiladi
# raqamlar2 = raqamlar.copy() # listni nusxasini yaratish
#
# raqamlar.extend([10, 11, 12, 13, 14])# toplamga toplamni birlashtirish yoki qo'shish
# print(raqamlar)
# raqamlar.reverse()  # toplamni teskarisiga ogirish
# raqamlar.remove(5)# toplamdan berilgan qiymatni ochirish bunda birinchi uchragan elementni ochiradi
# print(raqamlar)
#
# # for i in raqamlar:
# #     print(i * 2, end=' ')
# # length = len(raqamlar)
# # print(length)
#
# n = int(input('n='))
# S = []
# for i in range(1, n + 1):
#     S.append(2 * i - 1)
# print(S)
#
# if '13' in input():
#     print("omadsiz chipta")
# else:
#     print("omadli chipta")
#
#
# # S = 0
# # for i in s:
# #     S += int(i)
# # print(S)
# # print(sum([int(i) for i in s]))
#
#
# s='12234232'
# print(s, type(s))
# a = int(s)
# print(a, type(a))
# ss = str(a)
# print(ss, type(ss))

"Tub sonlar - birga va oziga bolinadigan sonlar "
import math

'''

3453
2,3,5,7,11,13.....
1) sonni ildizdan chiqaramiz
2) ildizdan chiqqanni butun qismini olamiz
3) 3453 ni 58 gacha bolgan tub sonlarga bolib chiqamiz
4) agar bironta songa qoldiqsiz bolinsa demak tub emas (murakkab son boladi)
agar hech biriga bolinmasa tub son boladi

'''
# print(int(math.sqrt(3453)))


n = int(input('n='))
k = int(math.sqrt(n))  # 58
counter = 1
while counter != k:
    counter += 1
    if n % counter == 0:
        print(f"tub emas chunki {counter} ga bo'lindi")
        break
    else:
        continue
if counter == k:
    print(f"{n} tub son")
