import random
import time
    
class KuisMusik:
    def __init__(self, lagu):
        self.lagu = lagu
        self.potongan_lirik = {
            "Come on now, follow my lead": "Shape of You",
            "Don't forget me": "Someone Like You",
            "Loving can hurt": "Photograph",
            "Feeling blue and alone": "December",
            "We all need someone to stay": "Someone To Stay"
        }

    def __del__(self):
        print("Selamat Datang di Tebak Lagu!")

    def tebak_lagu(self):
        potongan = random.choice(list(self.potongan_lirik.keys()))
        print(f"Potongan lirik\n'{potongan}'")
        judul_lagu = self.potongan_lirik[potongan]
        waktu_klip = self.lagu[judul_lagu]
        print(f"Waktu klip lirik: {waktu_klip} detik")
        while True:
            print("Apa judul lagu ini?")
            tebakan = input("Tebakan Anda: ")
            if tebakan.lower() == judul_lagu.lower():
                print("Selamat! Anda Telah berhasil menebak dengan benar.\n")
                break
            else:
                print(f"Maaf, tebakan Anda '{tebakan}' salah.\nSilahkan Coba lagi.")

    def __del__(self):
        print("Sesi kuis musik telah berakhir. Sampai jumpa lagi :) !")

daftar_lagu = {
    "Shape of You": 5,
    "Someone Like You": 6,
    "Photograph": 7,
    "December": 8,
    "Someone To Stay": 9
}
kuis = KuisMusik(daftar_lagu)
kuis.tebak_lagu()
