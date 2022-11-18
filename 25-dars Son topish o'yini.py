"""
Sana : 16/11/2022
Sobirjonov Khusanboy
#25 - dars : "Son topish" o'yini
Amaliyot
"""
import random
def son_top(son = 10):
    x = random.randint(1, son + 1)
    print(f"1 dan {son} gacha son o'yladim. Topa olasizmi?:")
    taxminiy_urinishlar = 0
    while True:
        n = int(input(">>> "))
        taxminiy_urinishlar += 1
        if x > n:
            print("Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling:\n>>")
        elif x < n:
            print("Xato, men o'ylagan son bundan kichikroq. Yana harakat qiling:\n>>")
        else:
            break
    print(f"TOPDINGIZ! {x} sonini o'ylagan edim. {taxminiy_urinishlar} ta taxmin bilan topdingiz. Tabriklayman!!")
    return taxminiy_urinishlar
    
def son_top_pc(son = 10):
      print(f"1 dan {son} gacha son o'ylang. Men topishga harakat qilaman.")
      input("Son o'ylagan bo'lsangiz istalgan tugmani bosing. ")
      taxminiy_urinishlar = 0
      son1 = 1
      while True:
          taxminiy_urinishlar += 1
          x = random.randint(son1, son)
          n = input(f"Siz {x} sonini o'yladingiz: to'g'ri (T), men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)??\n>> ")
          if n == '+':
              son1 = x
          elif n == '-':
              son = x
          else:
              break
      print(f"Soningizni {taxminiy_urinishlar} ta taxmin bilan topdim!")
      return taxminiy_urinishlar
    
def umumiy_natija(x = 10):
    taxminUser = son_top(x)
    taxminPC = son_top_pc(x)
    if taxminUser < taxminPC:
        print("Tabriklayman!", f"Siz {taxminUser} ta taxmin bilan yutdingiz!")
    elif taxminUser > taxminPC:
        print("G'alaba!", f"Men {taxminPC} ta taxmin bilan yutdim!")
    else:
        print("Durrang", f"Ikkalamizda ham {taxminPC} ta taxmin.")
    
son = int(input("Oraliq olinuvchi sonni kiriting: "))
umumiy_natija(son)


















    