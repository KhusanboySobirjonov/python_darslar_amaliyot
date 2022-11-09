"""
Sana : 05/11/2022
Sobirjonov Khusanboy
#08 - dars : Ro'yxatlar bilan ishlash
Amaliyot
"""
# 1 - O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
# countries = ["O'zbekiston", "Qirg'iziston", "Tojikiston", "Qozog'iston", "Turkmaniston", "Afg'oniston"]
# print(countries)

# 2 - Ro'yxatning uzunligini konsolga chiqaring
# print(len(countries))

# 3 - sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
# print(sorted(countries))

# 4 - sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
# print(sorted(countries,reverse = True))

# 5 - Asl ro'yxatni qaytadan konsolga chiqaring
# print(countries)

# 6 - reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
# countries.reverse()
# print(countries)

# 7 - sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
# countries.sort()
# print(countries)
# countries.sort(reverse = True)
# print(countries)

# 8 - 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
# numbers = list(range(120,1201,2))
# print(numbers)

# 9 - Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
# summa = sum(numbers)
# print(summa)

# 10 - Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
# Min = min(numbers)
# Max = max(numbers)
# print(Max - Min)

# 11 - Ro'yxatdagi elementlar sonini hisoblang
# print(len(numbers))

# 12 - Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
# length = len(numbers)
# print(numbers[:20])
# print(numbers[length//2 - 10:length//2 + 10])
# print(numbers[-20:])
    
# 13 - taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
# taomlar = []
# taomlar.append("osh")
# taomlar.append("sho'rva")
# taomlar.append("makaron")
# taomlar.insert(3,"mastava")
# taomlar.insert(0, "moshxo'rda")
    
# 14 - nonushta degan yangi ro'yxatga taomlardan nusxa oling
# nonushta = taomlar[:] # qiymati o'zgarmasligi uchun

# 15 - Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
# nonushta.remove("sho'rva")
# nonushta.remove("makaron")
# nonushta.remove("mastava")
# nonushta.append("tuxum quymoq")
# nonushta.insert(0,"qallama")

# 16 - Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
# print(taomlar)
# print(nonushta)
    
# 17 - Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
# nonushta = tuple(nonushta)
# nonushta[0] = "qaymoq va non"  # 'tuple' object does not support item assignment
    