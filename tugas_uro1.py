# Deskripsi
# Program mengidentifikasi
# Identifikasi kelulusan dengan syarat salah satu nilai tidak boleh lebih kecil sama dengan 50 atau rata-rata nilai harus lebih besar sama dengan 70

# KAMUS
# Nilai 1 : int
# Nilai 2 : int
# Nilai 3 : int
# Nilai 4 : int

# Algoritma

# Memasukkan input nilai
Nilai_1 = int(input("Masukkan nilai ujian 1: "))
Nilai_2 = int(input("Masukkan nilai ujian 2: "))
Nilai_3 = int(input("Masukkan nilai ujian 3: "))
Nilai_4 = int(input("Masukkan nilai ujian 4: "))

# Menghitung rata-rata nilai
Rata_Rata = (Nilai_1+Nilai_2+Nilai_3+Nilai_4)/4

# Mengidentifikasi apakah ada salah satu nilai yang kurang sama dengan 50 sehingga tidak lulus
if Nilai_1 <= 50 or Nilai_2 <= 50 or Nilai_3 <= 50 or Nilai_4 <= 50:
    Hasil = "tidak lulus"

# Mengidentifikasi apakah rata-rata kurang dari 70 sehingga tidak lulus
elif Rata_Rata < 70:
    Hasil = "tidak lulus"

# Jika nilai memenuhi standar yang diberikan, maka lulus
else:
    Hasil = "lulus"

# Tampilkan hasilnya
print("Tuan Kil " + Hasil + " kelas Tuan Leo")