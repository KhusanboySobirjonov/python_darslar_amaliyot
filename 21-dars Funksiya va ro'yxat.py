"""
Sana : 16/11/2022
Sobirjonov Khusanboy
#21 - dars : Funksiya va ro'yxat
Amaliyot
"""
# 1 - Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga 
# o'zgatiruvchi funksiya yozing. 
# def katta_harf(royxat):
#     """har bir matnning birinchi harfini katta qilib qaytaruvchi funksiya"""
#     for i in range(len(royxat)):
#         royxat[i] = royxat[i].title()
#     return royxat
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf(ismlar)
# print(ismlar)

# 2 - Yuqoridagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat qaytaradigan qilib o'zgartiring
# def katta_harf(royxat):
#     """har bir matnning birinchi harfini katta qilib qaytaruvchi funksiya asl ro'yxat 
#     o'zgarmaydi"""
#     royxat = royxat[:]
#     for i in range(len(royxat)):
#         royxat[i] = royxat[i].title()
#     return royxat
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# yangi_simlar = katta_harf(ismlar)
# print(ismlar)
# print(yangi_simlar)

# 3 -Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan va asl ro'yxatga o'zgartirish 
# kiritmasdan faqat lug'at qaytaradigan qilib yozing.
# def bahola(ismlar):
#     ismlar = ismlar[:]
#     baholar = {}
#     while ismlar:
#         ism = ismlar[-1]
#         del ismlar[-1]
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar

# def bahola(ismlar):
#     baholar = {}
#     for ism in ismlar:
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(talabalar)
# print(baholar)













