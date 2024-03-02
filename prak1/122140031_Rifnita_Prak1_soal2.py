def luas(r):
    return 3.14*r*r
def keliling(r):
    return 2*3.14*r

r=float(input("Jari-jari : "))

if r>0:
    print("Luas :", luas(r))
    print("Keliling :", keliling(r))
else:
    print("Jari-jari lingkaran tidak boleh negatif")
