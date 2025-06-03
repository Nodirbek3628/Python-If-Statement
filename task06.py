number = input("Telefon raqamni kiriting:")
code = number[0:2]

if code == "91" or code ==" 90":
    print("Beeline")
else:
    if code == "93" or code == "94":
        print("Ucell")
    else:
       if code == "95" or code == "97":
           print("Uzmobile")
       else:
           if code == "88" or code == "99":
               print("MobiUz")
           else:
               print("Nom'lum operator.")
               




