letter = input("Harf kiriting: ")     #Agar harf katta bo‘lsa "Katta harf", kichik bo‘lsa "Kichik harf" deb chiqarilsin.


if letter.isupper():
    print("katta harf ") 
if letter.islower():
    print("Kichik harf ")
else:
    print("Mavjud emas:")