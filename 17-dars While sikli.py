"""
Sana : 10/11/2022
Sobirjonov Khusanboy
#17 - dars : While sikli
Amaliyot
"""
# 1 - Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi 
# bilan dasturni to'xtating
# print("Yaxshi ko'rgan kitoblaringizni kiriting :\n")
# kitob = ''
# n = 1
# while kitob != 'stop':
#     kitob = input(f"{n} - yaxshi ko'rgan kitobingiz (To'xtatish uchun stop so'zini yozing) >>> ")
#     n += 1 
# print("Dastur tugadi!")

# 2 - Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 
# gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, 
# dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit 
# deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
# Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora, yoki shart tekshirish)
# savol = "Yoshingiz nechida ? "
# savol += "(Dasturni to'xtatish uchun exit yoki quit deb yozing) : "
# chipta = ''
# while True:
#     chipta = input(savol)
#     if chipta != 'quit' or chipta != 'exit':
#         break
#     yosh = int(chipta)
#     if yosh < 7:
#         print("Chipta narxi : 2000 so'm")
#     elif yosh >= 7 and yosh < 18:
#         print("Chipta narxi : 3000 so'm")
#     elif 18 <= yosh and yosh < 65:
#         print("Chipta narxi : 10000 so'm")
#     else:
#         print("Chipta narxi : bepul")
# print("Dastur tugadi!")

# 3 - Quyidagi dasturda bir nechta mantiqiy xatolar bor. Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib 
# qolmoqda. Xatolarni to'g'rilay olasizmi?
# savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# while True:
#     qiymat = input(savol)
#     if float(qiymat)<0:
#         continue
#     elif qiymat=='exit':
#         break
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")
















