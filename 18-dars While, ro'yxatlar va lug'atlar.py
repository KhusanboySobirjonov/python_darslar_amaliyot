"""
Sana : 12/11/2022
Sobirjonov Khusanboy
#18 - dars : While, ro'yxatlar va lug'atlar
Amaliyot
"""
# 1 - Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul 
# qilib, yangi ro'yxatga joylang.
# buyurtmalar = []
# eslatma = "(dasturni to'xtatish uchun exit deb yozing)"
# n = m = 1
# print("Hurmatli foydalanuvchi buyurtmalarni kiriting :")
# while True:
#     buyurtma = input(f"{n}-buyurtmani kiriting : {eslatma}")
#     if buyurtma == "exit":
#         break
#     buyurtmalar.append(buyurtma)
#     n += 1
# print("Sizning buyurtmalaringiz ro'yxati :")
# for item in buyurtmalar:
#     print(f"{m}. {item}")
#     m += 1

# 2 - e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. 
# Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
# e_bozor = {}
# while True:
#     mahsulot = input("Mahsulot nomini kiriting : ")
#     narx = int(input(f"{mahsulot.title()} narxini kiriting : "))
#     e_bozor["mahsulot"] = narx
#     savol = input("Yana mahsulotni qo'shasizmi ? (ha/yo'q) ")
#     if savol == "yo'q":
#         break
# print("Mahsulotlar qo'shildi!")

# 3 - Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni 
# e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot 
# e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
# buyurtmalar = ['olma','nok','uzum','anor']
# mahsulotlar = {'olma':10000,'nok':20000,'anor':30000,'limon':15000}
# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         print(f"{buyurtma.title()} narxi {mahsulotlar[buyurtma]} so'm")
#     else:
#         print(f"Bizda {buyurtma} yo'q")
















