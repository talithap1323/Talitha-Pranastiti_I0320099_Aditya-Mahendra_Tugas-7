import math
print("FUNGSI NUMERIK")
print("="*23)

print("\nPILIHAN"
      "\n1. Menemukan Nilai Mutlak"
      "\n2. Pembulatan Angka"
      "\n3. Menemukan Nilai Maksimum dan Minimum"
      "\n4. Menghitung Akar Kuadrat")

perlakuan = int(input("Apa yang ingin Anda lakukan? "))

print("-"*23)
if perlakuan == 1:
    angka1 = float(input("\nMasukkan angka: "))
    print("-"*23)
    print("\nNilai Mutlak adalah:")
    print("", math.fabs(angka1))
elif perlakuan == 2:
    angka2 = float(input("\nMasukkan angka: "))
    bulat = int(input("\n1. Pembulatan ke Atas"
                      "\n2. Pembulatan ke Bawah"
                      "\nMasukkan Pilihan: "))
    if bulat == 1:
        print("-"*23)
        print("\nHasil Pembulatan ke atas adalah:")
        print("", math.ceil(angka2))
    elif bulat == 2:
        print("-"*23)
        print("\nHasil Pembulatan ke bawah adalah:")
        print("", math.floor(angka2))
    else:
        print("-"*23)
        print("\n>>>PILIHAN TIDAK DITEMUKAN<<<")
elif perlakuan == 3:
    n = int(input("\nMasukkan banyaknya angka yang akan diinput: "))
    numerik = []
    jumlah = 0
    for i in range(0, n):
        angka = float(input("\nMasukkan angka ke- %d: " % (i + 1)))
        numerik.append(angka)
        jumlah += numerik[i]
    print("\n", numerik)
    maxmin = int(input("\n1. Nilai Maksimum"
                      "\n2. Nilai Minimum"
                      "\nMasukkan Pilihan: "))
    if maxmin == 1:
        print("-"*23)
        print("Nilai Maksimum dari", numerik, "adalah:")
        print("", max(numerik))
    elif maxmin == 2:
        print("-"*23)
        print("Nilai Minimum dari", numerik, "adalah:")
        print("", min(numerik))
    else:
        print("-"*23)
        print("\n>>>PILIHAN TIDAK DITEMUKAN<<<")
elif perlakuan == 4:
    angka4 = float(input("\nMasukkan Angka: "))
    print("-"*23)
    print("Angka %d setelah diakar kuadratkan adalah:" %angka4)
    print("", math.sqrt(angka4))
else:
    print("\n>>>PILIHAN TIDAK DITEMUKAN<<<")
