#Asal sayı hesaplayan program

num = int(input("Test için bir sayı girin: "))

flag = False

if num == 0 or num == 1:
    print(num, "Asal bir sayı DEĞİLDİR")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

    if flag:
        print(num, "Asal bir sayı DEĞİLDİR")
    else:
        print(num, "Asal bir sayıdır")