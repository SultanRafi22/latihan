#menerima inputan angka
bil1 = input("")
bil2 = input("")

#fungsi membalik inputan pertama
def balik_angka(num):
    return int(str(num)[::-1])

#fungsi membalik inputan kedua
def angka_balik(num):
    return int(str(num)[::-1])

#menjumlahkan inputan pertama dan inputan kedua yang sudah dibalik
hasil = balik_angka(bil1) + angka_balik(bil2)

#membalik hasil penjumlahan
def balik(num):
    return int(str(num)[::-1])

#menampilkan hasil
print(balik(hasil))