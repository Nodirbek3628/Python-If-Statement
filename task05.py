amout = int(input("Omonat summasini kiriting:"))


if amout < 100000:
    print("5%")
if amout >= 100000 and amout <=500000:
    print("7% ")
if amout > 500000:
    print("10% ")