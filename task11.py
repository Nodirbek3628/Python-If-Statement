number = int(input("Oy raqamini kiriting:"))        #Foydalanuvchidan oy raqamini (1 dan 12 gacha) kiritiladi.

if number > 0  and  number <= 2 or number == 12:            # Oyga qarab faslni aniqlanadi:
    print("Qish")

if number > 2 and number <= 5:
    print("Bahor")

if number > 5 and number <= 8:
    print("Yoz")

if number > 8 and number <= 11:
    print("Kuz")
