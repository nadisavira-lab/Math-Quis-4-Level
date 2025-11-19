# function: kumpulan urutan coding yang sesuai dengan aturan sintaks bahasa pemrograman tertentu 

# def nama():
#   isi dari function

# dipanggil fungsinya

def  menu():
    print("1. luas Persegi panjang")
    print("2. luas Persegi")
    print("3. luas Segitiga")  
    print("4. Luas Lingkaran")
def luas_persegi_panjang():
    P = int(input("Panjangnya? "))
    L = int(input("Lebarnya? "))
    rumus = P * L
    print("Luas Persegi Panjang adalah:", rumus)
def luas_persegi():
    S_pertama = int(input("Sisi pertamanya? "))
    S_kedua = int(input("Sisi keduanya? ")) 
    rumus = S_pertama * S_kedua
    print("Luas Persegi adalah:", rumus)
def luas_segitiga():
    A = float(input("Alasnya? "))
    T = float(input("Tingginya? "))
    rumus = 0.5 * A * T
    print("Luas Segitiga adalah:", rumus)
def luas_lingkaran():
    r = float(input("Jari-jarinya? "))
    rumus = 3.14 * r * r
    print("Luas Lingkaran adalah:", rumus)

menu()
choice = int(input("= "))
if choice == 1:
    luas_persegi_panjang()
elif choice == 2:
    luas_persegi()
elif choice == 3:
    luas_segitiga()
elif choice == 4:
    luas_lingkaran()    
