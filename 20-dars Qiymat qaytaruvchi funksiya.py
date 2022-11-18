"""
Sana : 16/11/2022
Sobirjonov Khusanboy
#20 - dars : Qiymat qaytaruvchi funksiya
Amaliyot
"""
# 1 - Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va 
# telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda 
# foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling 
# (masalan, tel.raqam, el.manzil)
# def user (ism, familiya, t_yil, t_joy, el_manzil = 'None', tel_raqam = 'None') :
#     if el_manzil == 'None':
#         el_manzil = "Noma'lum"
#     if tel_raqam == 'None':
#         tel_raqam = "Noma'lum"
#     yosh = 2022 - int(t_yil)
#     malumot = {
#         'ism':ism,
#         'familiya':familiya,
#         "tyil":t_yil,
#         "tjoy":t_joy,
#         'yosh':yosh,
#         'email':el_manzil,
#         'telraqam':tel_raqam
#     }
#     return malumot

# users = []
# print("Foydalanuvchi ma'lumotlarini to'ldiring :")
# ism = input("Ismi : ")
# familiya = input("Familiyasi : ")
# t_yil = int(input("Tug'ilgan yili : "))
# t_joy = input("Tug'ilgan joyi : ")
# el_manzil = input("Email : ")
# tel_raqam = input("Telefon raqami : ")
# users.append(user(ism, familiya, t_yil, t_joy, el_manzil, tel_raqam))
# print(users)

# 2 - Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni shakllantiring. 
# Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.
# def mijoz_info (ism, familiya, t_yil, t_joy, el_manzil = 'None', tel_raqam = 'None') :
#     if el_manzil == 'None':
#         el_manzil = "Noma'lum"
#     if tel_raqam == 'None':
#         tel_raqam = "Noma'lum"
#     yosh = 2022 - int(t_yil)
#     malumot = {
#         'ism':ism,
#         'familiya':familiya,
#         "tyil":t_yil,
#         "tjoy":t_joy,
#         'yosh':yosh,
#         'email':el_manzil,
#         'telraqam':tel_raqam
#     }
#     return malumot

# mijozlar = []
# while True:
#     print("Mijoz ma'lumotlarini to'ldiring :")
#     ism = input("Ismi : ")
#     familiya = input("Familiyasi : ")
#     t_yil = int(input("Tug'ilgan yili : "))
#     t_joy = input("Tug'ilgan joyi : ")
#     el_manzil = input("Email : ")
#     tel_raqam = input("Telefon raqami : ")
#     mijozlar.append(mijoz_info(ism, familiya, t_yil, t_joy, el_manzil, tel_raqam))
#     savol = input("Yana ma'lumot kiritasizmi ? (ha yoki yo'q) ")
#     if savol == "yo'q":
#         break
# for mijoz in mijozlar:
#     print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()} \n{mijoz['tyil']}-yil tug'ilgan. Hozirda {mijoz['yosh']} da\nElektron pochta : {mijoz['email']} \nTelefon raqam : {mijoz['telraqam']}")

# 3 - Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
# def max3 (a, b, c) :
#     """3 ta sondan eng kattasini qaytaruvchi funksiya"""
#     if a < b: a = b
#     if a < c: a = c
#     return a

# son, son1, son2 = map(float, input("Istalgan 3 ta sonni bitta qatorda kiriting : ").split())
# print(f"Eng katta son : {max3(son,son1,son2)}")

# 4 - Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, 
# perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing
# def aylana_info(radius, pi = 3.14159):
#     aylana = {
#         'radius':radius,
#         'diametr':2 * radius,
#         'perimetr':2 * pi * radius,
#         'yuza':pi * radius**2
#         }
#     return aylana
# print(aylana_info(5))

# 5 - Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub sonlar —
# faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)
# def tub_sonlar(min, max):
#     """Tub sonlar ro'yxatini qaytaruvchi funksiya"""
#     tubsonlar = []
#     for i in range(min, max + 1):
#         tub_son = True
#         if i < 2: 
#             tub_son = False
#         elif i == 2:
#             tub_son = True
#         else:
#             for n in range(2, i):
#                 if i % n == 0:
#                     tub_son = False
#         if tub_son:
#             tubsonlar.append(i)
#     return tubsonlar

# print(tub_sonlar(1, 5))

# 6 - Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar 
# ro'yxatni qaytaruvchi funksiya yozing.  Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning 
# yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish 
# had ko’pincha 1 deb olinadi.  1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
# def Fibonachchi(n) :
#     """Fibonachchi sonlarini ro'yxat tarzida qaytaruvchi funksiya"""
#     fibonachchi_sonlar = []
#     for i in range(0, n + 1):
#         if i == 0 or i == 1:
#             fibonachchi_sonlar.append(1)
#         else:
#             fibonachchi_sonlar.append(fibonachchi_sonlar[i - 1] + fibonachchi_sonlar[i - 2])
    
#     return fibonachchi_sonlar

# print(Fibonachchi(5))







