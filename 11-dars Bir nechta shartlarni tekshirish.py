"""
Sana : 08/11/2022
Sobirjonov Khusanboy
#11 - dars : Bir nechta shartlarni tekshirish
Amaliyot
"""
# 1 - Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
# juft_son = int(input("Juft sonni kiriting : "))
# if juft_son % 2 == 0:
#     print("Raxmat!")
# else:
#     print("Bu son juft emas")

# 2 - Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
# yosh = int(input("Yoshingiz nechida ? >>> "))
# if yosh <= 4 or 60 <= yosh:
#     print("Bepul")
# elif yosh < 18:
#     print("10000 so'm")
# else:
#     print("20000 so'm")

# 3 - Foydalanuvchidan ikkita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
# b_son = int(input("Birinchi sonni kiriting : "))
# i_son = int(input("Ikkinchi sonni kiriting : "))
# if b_son == i_son:
#     print(f"{b_son} = {i_son}")
# elif b_son > i_son:
#     print(f"{b_son} > {i_son}")
# else:
#     print(f"{b_son} < {i_son}")

# 4 - mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. 
# Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta 
# mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan 
# solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, 
# "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
# mahsulotlar = ["olma", "uzum", "anor", "behi", "nok", "shaftoli", "olxo'ri", "olcha", "o'rik", "bodom"]
# savat = []
# for i in range(5):
#     savat.append(input(f"Savatga {i + 1} - mahsulotni qo'shing : "))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"{mahsulot.title()} do'konimizda bor.")
#     else:
#         print(f"{mahsulot.title()} do'konimizda yo'q.")

# 5 - Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. 
# Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, 
# do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas 
# ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, 
# aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.
# bor_mahsulotlar = []
# mavjud_emas = []
# for i in range(5):
#     mahsulot = input(f"Savatga {i + 1} - mahsulotni qo'shing : ")
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
# else:
#     print(f"Quyidagi mahsulotlar do'konimizda yo'q: {mavjud_emas}")

# 6 - foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. 
# Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni 
# foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday 
# login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, 
# foydalanuvchi!" xabarini chiqaring.
# foydalanuvchilar = ["admin", "login", "hacker", "user", "anonymos"]
# foydalanuvchi = input("Yangi login tanlang : ")
# if foydalanuvchi in foydalanuvchilar:
#     print("Login band, yangi login tanlang!")
# else:
#     print(f"Xush kelibsiz {foydalanuvchi}!")

# 7 - Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 
# 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring. 
# son = int(input("Istalgan butun sonni kiriting : "))
# for i in range(2,11):
#     if not (son % i):
#         print(f"{son} soni {i} ga qoldiqsiz bo'linadi")

