"""
Sana : 18/11/2022
Sobirjonov Khusanboy
#15 - dars : Lug'at elementlari bilan tanishuv
Amaliyot
"""
# 1 - Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va 
# qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 
# words = {'int': 'butun son',
#           'typecasting': 'turni almashtirish',
#           'strip': "boshi va oxiridan bo'shliqni olish",
#           'type': 'turni aniqlash',
#           'upper': 'harflarni yuqori registrga o\'tkazish',
#           'lower': 'harflarni quyi registrga o\'tkazish',
#           'title': "so'zlarning birinchi harfini katta qilish",
#           'capitalize': "birinchi so'zning birinchi harfini katta qilish",
#           '__doc__': "funksiya haqida ma'lumot olish",
#           'choice': "ro'yxat ichidan tanlab berish"
#           }
# for k, v in words.items():
#     print(f"{k.title()} - {v.capitalize()}")

# 2 - Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni 
# alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.
# dunyo_davlatlari = {'aqsh': 'washington d.c.',
#                     'italiya': "rim",
#                     'malayziya': 'kuala-lumpur',
#                     'o\'zbekiston': 'toshkent',
#                     'qirg\'iziston': 'bishkek',
#                     'qozog\'iston': 'nursulton',
#                     'rossiya': 'moskva',
#                     'singapur': 'dungapur',
#                     'tojikiston': 'dushanbe'
#                     }
# print("Dunyo davlatlari : ")
# for key in sorted(dunyo_davlatlari):
#     print(key.upper())

# print("\nDavlatlarning poytaxti : ")
# for values in sorted(dunyo_davlatlari.values()):
#     print(values.title())

# 3 - Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga 
# chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan 
# xabarni chiqaring.
# davlat = input("Qaysi davlatning poytaxtini bilishni istaysiz ? ").lower()
# javob = dunyo_davlatlari.get(davlat)
# if javob != None:
#     print(f"{davlat.upper()}ning poytaxti {dunyo_davlatlari[davlat].title()} shahri.")
# else:
#     print("Kechirasiz, bizda bu haqida ma'lumot yo'q")

# 4 - Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 
# ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar 
# taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
# restoran_menusi = {'non': 4000,
#                    'osh': 20000,
#                    'mastava': 14000,
#                    'sho\'rva': 15000,
#                    'lag\'mon': 12000,
#                    'bishteks': 17000,
#                    'kfc': 20000,
#                    'shashlik': 8000,
#                    'lavash': 16000,
#                    'pitsa': 23000
#                    }
# menu = []
# print("3 ta taom buyurtma bering.")
# for i in range(3):
#     menu.append(input(f"{i + 1} - taom : ").lower())
# for taom in menu:
#     if taom in restoran_menusi:
#         print(f"{taom.title()} {restoran_menusi[taom]} so'm")
#     else:
#         print(f"Kechirasiz, bizda {taom} yo'q.")













