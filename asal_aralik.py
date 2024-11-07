#Belirli bir aralıktaki Asal sayılar

alt = int(input("Test için başlangıç değeri nedir?"))
ust = int(input("Test için bitiş değeri nedir?"))

asal = []

for n in range(alt, ust+1):
    if n>1:
        for i in range(2, n):
            if (n % i) == 0:
                break
        else:
            asal.append(n)

print("Bu aralıkta", len(asal), "adet asal sayı vardır")