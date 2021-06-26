# import library socket karena akan menggunakan IPC socket
import socket

def cetakVersiSekarang(now_client):
    #Output Versi sekarang di Client
    print("Versi sekarang adalah : " + now_client)

def cetakHistoryVersion(history_client):
    #Output Versi yang pernah ada di Client
    print("History Versi yang pernah ada di Client adalah ")
    for i in range(0,len(history_client)):
        print(history_client[i])

def cekUpdate(now_client):
    # definisikan tujuan IP server, port, buffer size
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5005
    BUFFER_SIZE = 1024
    
    # buat socket TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # lakukan koneksi ke server dengan parameter IP dan Port yang telah didefinisikan
    s.connect((TCP_IP, TCP_PORT))

    #Melaukan cek update ke Server dengan Socket

    #Kirim
    s.send(now_client.encode())
    # terima pesan dari server
    now_server = s.recv(BUFFER_SIZE)

    if (now_server.decode() != now_client):
        #Jika nama versi berbeda, memberikan notif
        print("Update tersedia")
        return True
    else:
        print("Anda sudah memiliki versi terbaru")
        return False

    # tutup koneksi
    s.close()

def doUpdate(now_client, history_client, adaUpdate):
    # definisikan tujuan IP server, port, buffer size
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5005
    BUFFER_SIZE = 1024
    
    # buat socket TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # lakukan koneksi ke server dengan parameter IP dan Port yang telah didefinisikan
    s.connect((TCP_IP, TCP_PORT))

    #Melakukan update (masih error)

    if (not adaUpdate):
        print("Belum bisa Update karena belum periksa versi ke server ataupun karena versi client sudah terbaru")
    else:
        s.send(now_client.encode())
        # terima pesan dari server
        now_server = s.recv(BUFFER_SIZE)
        history_client.append(now_server.decode())
        now_client = now_server.decode()
        print("Berhasil melakukan update")

    return now_client

    # tutup koneksi
    s.close()


def menu():
    print("\nSelamat datang di sisi client, silakan pilih menu yang akan dipilih : ")
    print("1. Melihat Versi Sekarang")
    print("2. Melihat History Versi di Client")
    print("3. Cek Update")
    print("4. Melakukan Update")
    print("0. Keluar")

def pilihan(pil, history_client, now_client, adaUpdate):
    if (pil == 1):
        cetakVersiSekarang(now_client)
    elif (pil == 2):
        cetakHistoryVersion(history_client)
    elif (pil == 3):
        adaUpdate = cekUpdate(now_client)       #Ada Update bernilai True (jika ada) dan False (jika tidak ada)
    elif (pil == 4):
        now_client = doUpdate(now_client, history_client, adaUpdate)    #Mengganti now_client yang sekarang dengan baru
    else:
        print("Masukkan Angka yang valid!")

    return adaUpdate, now_client



#list history versi
history_client = ["1.1.1", "1.1.2", "1.1.3", "1.2.1", "1.2.4", "1.2.5"]

#versi client
now_client = "1.2.6"


#inisialisasi ada update, ganti kalau ada updatean dari server
adaUpdate = False

while True:
    menu()
    pil = int(input("Masukkan Pilihan Anda: "))
    if (pil == 0):
        break
    else:
        adaUpdate, now_client = pilihan(pil, history_client, now_client, adaUpdate)



