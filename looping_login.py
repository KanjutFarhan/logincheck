percobaan = 0
login_berhasil = False
admin = "admin"
password_admin = "12345"

while True:
    user = input("Masukan Username Anda: ")
    password = input("Masukan Password Anda: ")

    percobaan += 1
    
  # Cek login
    if user == admin and password == password_admin:
        print("✅ Selamat Datang!")
        login_berhasil = True
        break
    elif user != admin and password == password_admin:
        print("❌ Username salah")
    elif user == admin and password != password_admin:
        print("❌ Password salah")
    else:
        print("❌ Username dan Password salah")
        
    if percobaan >= 3:
        print("❌ Anda Sudah MEncoba 3 Kali Silahkan Coba Lagi Nanti!")
        break
        
if login_berhasil:
    bintang_segitiga = "*"
    baris_penuh = 9
# Ini Segetiga Nya
    for i in range(baris_penuh,0, -1):
        for jarak in range(baris_penuh - i):
            print(" ", end="")
            
        for bintang in range(2 * i - 1):
            print(bintang_segitiga, end="")
        print()
        
print("Anomali Segitiga Python!")