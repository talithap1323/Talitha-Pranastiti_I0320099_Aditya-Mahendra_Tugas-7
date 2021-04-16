print("FUNGSI STRING")
print("="*23)

string = input("\nMasukkan string: ")

print("\nPERLAKUAN:"
      "\n1. Mengubah Huruf Pertama Menjadi Huruf Kapital"
      "\n2. Menghitung Banyaknya Substring yang Muncul pada String"
      "\n3. Mencari substring dalam String"
      "\n4. Mengganti Substring"
      "\n5. Mengubah Seluruh Huruf dalam String Menjadi Kapital atau Kecil")

perlakuan = int(input("Apa yang ingin Anda Lakukan? "))

print("-"*23)
if perlakuan == 1:
    print("\nString Anda menjadi:"
          "\n", string.capitalize())
elif perlakuan == 2:
    substr2 = input("\nMasukkan substring yang akan dihitung: ")
    x = string.count(substr2)
    print("Jumlah %s pada String Anda adalah:" %substr2)
    print("",x)
elif perlakuan == 3:
    substr3 = input("\nMasukkan substring yang akan dicari: ")
    y = string.index(substr3)
    print("Substring %s pada string Anda ada pada index: " %substr3)
    print("", y)
elif perlakuan == 4:
    old = input("\nMasukkan substring yang akan diganti: ")
    new = input("Masukkan substring baru: ")
    z = string.replace(old, new)
    print("\nString Anda menjadi:"
          "\n", z)
elif perlakuan == 5:
    print("\n1. Huruf Kapital"
          "\n2. Huruf Kecil")
    choice = int(input("Masukkan pilihan Anda: "))
    if choice == 1:
        a = string.upper()
        print("\nString Anda menjadi:"
              "\n", a)
    elif choice == 2:
        b = string.lower()
        print("\nString Anda menjadi:"
              "\n", b)
    else:
        print("\n>>>PILIHAN TIDAK DITEMUKAN<<<")
else:
    print("\n>>>PERLAKUAN TIDAK DITEMUKAN<<<")
