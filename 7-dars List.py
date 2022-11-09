"""
Sana : 07/11/2022
Sobirjonov Khusanboy
#07 - List (Ro'yxat)
Amaliyot
"""
# 1 - ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
# ismlar = ["Nurillo", "Abduhilol", "Qobiljon", "Bahtiyor", "Shuhrat"]

# 2 - Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 
# print(ismlar[0],"Age of Empires Mobile o'yini chiqadi ekan.")
# print("Bugun qayerda o'tiramiz",ismlar[4])

# 3 - sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 
# sonlar = [4, -5, 0, 1.5, 3.15419]

# 4 - Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
# sonlar[0] = sonlar[1] + sonlar[2]
# sonlar[1] = sonlar[2] * sonlar[3]
# sonlar[4] = 5.89
# sonlar[3] = sonlar[3] + sonlar[4]
# sonlar[4] = sonlar[3] - sonlar[4]
# sonlar[3] = sonlar[3] - sonlar[4]
# print(sonlar)

# 5 - t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 
# t_shaxslar = ["Amir Temur", "Abu Nasr Farobiy", "Abu Ali Ibn Sino", "Mirzo Ulug'bek"]
# z_shaxslar = ["Bill Geyts", "Pavel Durov", "Mark Sukerberg", "Ilon Mask"]

# 6 - Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
# t_shaxs = t_shaxslar.pop(2)
# z_shaxs = z_shaxslar.pop(3)
# print(f"Men tarixiy shaxslardan {t_shaxs} bilan, zamonaviy shaxslardan esa {z_shaxs} bilan suhbat qilishni istardim")

# 7 - friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 
# friends = []
# friends.append("Xushnudbek")
# friends.append("Nurillo")
# friends.append("Shuhrat")
# friends.append("Bahtiyor")
# friends.append("Qobiljon")
# print(friends)

# 8 - Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
# friends.remove("Xushnudbek")

# 9 - Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
# friends.insert(0, "Abduhilol")
# friends.insert(-1, "Islomjon")
# friends.insert(2, "Ulug'bek")
# print(friends)

# 10 - Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
# mehmonlar = []
# mehmonlar.append(friends.pop(1))
# mehmonlar.append(friends.pop(0))
# mehmonlar.append(friends.pop(3))
# print(mehmonlar)

