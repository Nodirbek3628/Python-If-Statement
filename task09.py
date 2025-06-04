number01 = int(input("1-tomonini kiriting:"))
number02 = int(input("2-tomonini kiriting:"))
number03 = int(input("3-tomonini kiriting:"))

if number01 == number02 and number02 == number03:
    print("Teng tomonli")
elif number01 == number02 or  number02 == number03 or number01 == number03:
    print("Teng yonli")
else:
    print("Turli tomonli")                   #T.O'.I