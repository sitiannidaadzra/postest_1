user = "annidadzra" 
nim = "2309116013"
pw = "653498"

# BUAT INPUT UNTUK MEMASUKAN USERNAME, NIM DAN PASSWORD
username_input = input("Masukkan Username: ")  
nim_input = input("Masukkan NIM: ")
password_input= input("Masukkan Password: ")

# Memeriksa username, NIM, dan password
if username_input == user and nim_input == nim and password_input == pw:
    print(20*"=")
    print("ANDA BERHASIL LOGIN")
    print(20*"=")
    
    print("Masukan Pilihan")
    print("pilihan 1 = alas")
    print("pilihan 2 = sisi tegak")
    print("pilihan 3 = sisi miring ")
    print("pilihan 4 = keluar ")
    
    pilihan = int(input("masukan pilihan (1/2/3/4) : "))
    if pilihan == 1:
        sisi_miring = float(input('Masukkan sisi miring: '))
        sisi_tegak = float(input('Masukkan sisi tegak: '))
        rumus_alas = (sisi_miring**2 - sisi_tegak**2)**0.5
        print(f'Hasil alas adalah: {rumus_alas}')

    if pilihan == 2:
        sisi_miring = float(input('Masukkan sisi miring: '))
        sisi_alas = float(input('Masukkan sisi alas: '))
        rumus_tegak = (sisi_miring**2 - sisi_alas**2)**0.5
        print(f'Hasil alas adalah: {rumus_tegak}')

    if pilihan == 3:
        sisi_tegak = float(input('Masukkan sisi tegak: '))
        sisi_alas = float(input('Masukkan sisi alas: '))
        rumus_miring = (sisi_tegak**2 + sisi_alas**2)**0.
        print(f'Hasil alas adalah: {rumus_miring}')
        
    if pilihan == 4:
        print('Terima kasih')

else:
    print(20*"=")
    print("DATA YANG DIMASUKKAN SALAH")
    print(20*"=")
    
#Code diatas merupakan program login sederhana yang berisi username/nama, nim dan password. Setelah itu program akan memeriksa apakah hasil input
#sesuai dengan data yang telah ditentukan sebelumnya, jika input sesuai maka program akan berjalan dan user di anggap berhasil login, jika input 
#tidak sesuai dengan data yang telah ditentukan, maka program akan menampilkan pesan bahwa data yang dimasukkan salah. 

#Terdapat 4 pilihan program yang bisa dipilih, 
#1. Di pilihan 1 program akan meminta user untuk memasukkan nilai panjang sisi miring dan sisi tegak segitiga, kemudian akan menampilkan hasil 
# dari panjang alas segitiga
#2. Di pilihan 2 program akan meminta user untuk memasukkan nilai panjang sisi miring dan sisi alas segitiga, kemudian akan menampilkan hasil 
# dari panjang sisi tegak segitiga
#3. Di pilihan 3 program akan meminta user untuk memasukkan nilai panjang sisi tegak dan sisi alas segitiga, kemudian akan menampilkan hasil 
# dari panjang sisi miring segitiga
#4. Di pilihan 4 program akan menampilkan pesan terimakasih dan berakhir.