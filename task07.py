email = input("Emailingizni kiriting: ")                   #Email manzilini tekshirish

if "@" in email and "." in email and " " not in email:
    print("Email manzil to'g'ri: ")
else:
    print("Email manzil notug'ri: ")