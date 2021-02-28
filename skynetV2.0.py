# App SkyNet
import function
function.loading()
while True:
    print("# Menu")
    print("1. Lacak Nomor       - Lokasi yang di lacak adalah lokasi terkini")
    print("2. Data Nomor        - Memeriksa Data registrasi Nomor HP")
    print("0. Exit              - Keluar")

    menu = input("Pilih Menu : ")

    if menu == "0":
        break
    elif menu == "1":
        nomor = input("Masukan Nomor Telepon : ")
        print(f"Melacak {nomor}")
        function.lacak()
    elif menu == "2":
        function.datanomor()
    else:
        print("Menu tidak tersedia")
print("Good Bye!")