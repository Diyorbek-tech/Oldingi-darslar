"""

                Tanlash operatori   match

Boshqa dastrulash tillarida switch case deb ishlatiladi (c#, c++, java)
python 3.10

match s:
    case "salom": print("salomga teng")
    case "hayr":
        print("hayrga teng")
        print("hayrga teng")
        print("hayrga teng")
        print("hayrga teng")
        print("hayrga teng")
        print("hayrga teng")
        print("hayrga teng")
    case _: print("yuqoridagilar bajarilmadi")

if s=="salom"
elif s=="hayr"

"""
# k=int(input('hafta kuni>>>'))
# match k:
#     case 1:print("Dushanba")
#     case 2:print("Seshanba")
#     case 3:print("Chorshanba")
#     case 4:print("Payshanba")
#     case 5:print("Juma")
#     case 6:print("Shanba")
#     case 7:print("Yakshanba")
#     case _:print("Bunday hafta kuni yoq")
#
# #match3
# oy = int(input('oy_raqami>>>'))
#
# match oy:
#     case 1 | 2 | 12:
#         print("Qish")
#     case :3 | 4 | 5
#         print("Bahor")
#     case 6 | 7 | 8:
#         print("Yoz")
#     case 9 | 10 | 11:
#         print("Kuz")

# match5
# A=float(input("A="))
# B=float(input("B="))
# amal=int(input("AMAL="))
#
# match amal:
#     case 1: print(A+B)
#     case 2: print(A-B)
#     case 3: print(A/B)
#     case 4: print(A*B)


# # match8
#
# D, M = map(int, input().split(' '))
# match M:
#     case 1:print(f"{D}-Yanvar")
#     case 2:print(f"{D}-Fevral")
#     case 3:print(f"{D}-Mart")
#     case 4:print(f"{D}-Aprel")
#     case 5:print(f"{D}-May")
#     case 6:print(f"{D}-Iyun")
#     case 7:print(f"{D}-Iyul")
#     case 8:print(f"{D}-Avgust")
#     case 9:print(f"{D}-Sentabr")
#     case 10:print(f"{D}-Oktabr")
#     case 11:print(f"{D}-Noyabr")
#     case 12:print(f"{D}-Dekabr")


# n = int(input('n='))  # 123
# birlar = n % 10
# onlar = n // 10 % 10
# yuzlar = n // 100
#
# text_birlik = ''
# text_onlik = ''
# text_yuzlik = ''
#
# match birlar:
#     case 1:
#         text_birlik = 'bir'
#     case 2:
#         text_birlik = 'ikki'
#     case 3:
#         text_birlik = 'uch'
#     case 4:
#         text_birlik = 'tort'
#     case 5:
#         text_birlik = 'besh'
#     case 6:
#         text_birlik = 'olti'
#     case 7:
#         text_birlik = 'yetti'
#     case 8:
#         text_birlik = 'sakkiz'
#     case 9:
#         text_birlik = 'to\'qqiz'
#
# match onlar:
#     case 1:
#         text_onlik = 'o\'n'
#     case 2:
#         text_onlik = 'yigirma'
#     case 3:
#         text_onlik = 'o‘ttiz'
#     case 4:
#         text_onlik = 'qirq'
#     case 5:
#         text_onlik = 'ellik'
#     case 6:
#         text_onlik = 'oltmish'
#     case 7:
#         text_onlik = 'yetmish'
#     case 8:
#         text_onlik = 'sakson'
#     case 9:
#         text_onlik = 'to\'qson'
#
# match yuzlar:
#     case 1:
#         text_yuzlik = 'bir'
#     case 2:
#         text_yuzlik = 'ikki'
#     case 3:
#         text_yuzlik = 'uch'
#     case 4:
#         text_yuzlik = 'tort'
#     case 5:
#         text_yuzlik = 'besh'
#     case 6:
#         text_yuzlik = 'olti'
#     case 7:
#         text_yuzlik = 'yetti'
#     case 8:
#         text_yuzlik = 'sakkiz'
#     case 9:
#         text_yuzlik = 'to\'qqiz'
#
# print(text_yuzlik, 'yuz', text_onlik, text_birlik)


yil = int(input('yil='))
rang = yil % 60 % 5
hayvon = yil % 60 % 12

text_rang = ''
text_hayvon = ''

match rang:
    case 4:
        text_rang = 'yashil'
    case 0:
        text_rang = 'qizil'
    case 1:
        text_rang = 'sariq'
    case 2:
        text_rang = 'oq'
    case 3:
        text_rang = 'qora'

match hayvon:
    case 4:text_hayvon="Sichqon"
    case 5:text_hayvon="Sigir"
    case 6:text_hayvon="Yolbars"
    case 7:text_hayvon="Quyon"
    case 8:text_hayvon="Baliq"
    case 9:text_hayvon="Ilon"
    case 10:text_hayvon="Ot"
    case 11:text_hayvon="Qoy"
    case 0:text_hayvon="Maymun"
    case 1:text_hayvon="Tovuq"
    case 2:text_hayvon="It"
    case 3:text_hayvon="Tong‘iz"

print(text_rang,text_hayvon)