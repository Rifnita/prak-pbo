class Mahasiswa:
    def __init__(self, nim, nama, angkatan, ipk=0.0):
        self.__nim = nim
        self.__nama = nama
        self.angkatan = angkatan
        self.ipk = ipk

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def get_nim(self):
        return self.__nim

    def set_nim(self, nim):
        self.__nim = nim

    def info_mahasiswa(self):
        return f"NIM : {self.__nim}\nNama : {self.__nama}\nAngkatan : {self.angkatan}\nIPK : {self.ipk}"

    def tambah_ipk(self, tambahan_ipk):
        self.ipk += tambahan_ipk

    def hitung_rata_rata(self, ipk_lain):
        jumlah_ipk = self.ipk + ipk_lain
        return jumlah_ipk / 2

# Inisialisasi objek mahasiswa1 dengan IPK 3.5
mahasiswa1 = Mahasiswa("122230031", "Aimo", 2022, 3.5)
print("Mahasiswa 1")
print(mahasiswa1.info_mahasiswa())  
print("")  

# Inisialisasi objek mahasiswa2 dengan IPK 3.8
mahasiswa2 = Mahasiswa("122140031", "Rifnita", 2022, 3.8)
print("Mahasiswa 2")
print(mahasiswa2.info_mahasiswa())
print("")

# Menambahkan 0.2 ke IPK mahasiswa1
mahasiswa1.tambah_ipk(0.2)
print("Setelah menambahkan IPK")
print(mahasiswa1.info_mahasiswa())
print("")

# Menghitung rata-rata IPK mahasiswa1 dan mahasiswa2
rata_rata = mahasiswa1.hitung_rata_rata(mahasiswa2.ipk)
print("Rata-rata IPK dari mahasiswa1 dan mahasiswa2 =", rata_rata)
