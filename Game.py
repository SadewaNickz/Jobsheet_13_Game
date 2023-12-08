def guess_number():
    secret_number = 17
    guess = 0
    guess_count = 4

print("Tebak angka 1 - 20")
while guess < guess_count:
    User = int(input("Masukkan Angka : "))
    if int(User) == secret_number:
        print("Angkamu benar")
        break
    elif int(User) > secret_number:
        print("Angkamu terlalu tinggi")
        guess = guess + 1
    elif int(User) < secret_number:
        print("Angkamu terlalu rendah")
        guess = guess + 1
else:
    print("Kesempatan habis")