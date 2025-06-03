number = int(input("Raqam kiriting:"))           #Foydalanuvchidan son kiriting.
 
if number > 0:                                  #Agar son > 0 — "Ijobiy son": Agar son < 0 — "Manfiy son":
    print("Ijobiy son:")                        #Agar son = 0 — "Nol" deb chiqarilsin
if number < 0:
    print("Manfiy son: ")
if number == 0:
    print("Nol:")
