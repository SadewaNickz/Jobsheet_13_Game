#Konversi berat
konversi = 2.20462


weight = int(input("Masukkan beratnya : "))
types = input("Lbs(L) or Kg(K) : ")
lbs = weight * konversi
kg = weight / konversi

if (types == "K"):
    print(weight / konversi)
else:
    print(weight * konversi)
