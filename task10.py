number = int(input("Ballarni kiriting: "))      #Foydalanuvchidan imtihon ballini kiritadi (0 dan 100 gacha).
                                                #Quyidagi baholash tizimiga asoslanib, bahoni chiqarsin:
if number >= 90 and number <= 100:
    print("A")
if number >= 80 and number <=89:
    print("B")
if number >= 70 and number <= 79:
    print("C")
if number >= 60 and number <= 69:
    print("D")
if number >= 0 and number <= 59:
    print("F")