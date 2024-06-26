import math

class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi
        
    def hitung_luas(self):
        return self.sisi**2
        
class Lingkaran:
    def __init__(self,jari_jari):
        self.jari_jari = jari_jari
        
    def hitung_luas(self):
        return math.pi*self.jari_jari**2
        
persegi = Persegi(5)
lingkaran = Lingkaran(3)

print(f"Luas Persegi : {persegi.hitung_luas()}")
print(f"Luas Lingkaran : {lingkaran.hitung_luas()}")