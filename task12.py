
num01 = input("Parolni kiriting: ")                 #Foydalanuvchi  ikki marta parol kiritadi.
num02 = input("Parolni qayta kiriting:")     #Agar parollar bir xil bo‘lsa “Parol qabul qilindi”, aks holda “Parollar mos emas” deb chiqarilsin.

if num01 == num02:
    print("Parol qabul qilindi")
else:
    print("Parollar mos emas")