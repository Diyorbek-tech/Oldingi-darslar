"""  Shart operatori -if (agar) """

"""
else +if =elif= aks holda agar


shart=a>10 and b<5
if shart:
    print(True)
else:
    print(False)
   
if shart:
   print(_)
elif shart2:
   print('asdas')
else:
   print("asdasdasd")


if -zanjir boshi
else-zanjir ohiri
elif- zanjir halqasi

1)  if
2)  if else
3)  if elif 
4)  if elif else
5)  if elif elif elif ...... 
6)  if elif elif elif ...... else
"""
#
# n = int(input("n="))
# if n > 0 and n != 1:
#     print("Musbat")
# elif n == 1:
#     print("1-musbat")
# else:
#     print("boshqa")

# a, b, c = map(int, input().split(' '))
# t1 = a > 0 and b > 0 and c > 0  # 3musbat
# t2 = (a > 0 and b > 0 and c < 0) or (a > 0 and b < 0 and c > 0) or (a < 0 and b > 0 and c > 0)
# t3 = (a < 0 and b < 0 and c < 0)
#
# if t1:
#     print("3 musbat")
# elif t2:
#     print("2 musbat")
# elif t3:
#     print("0 musbat")
# else:
#     print("1 musbat")
# # ----------------------------------------------------------

#if11
a, b = map(int, input().split(' '))
if a != b:
    a = max(a, b)
    b = max(a, b)
else:
    a = 0
    b = 0
