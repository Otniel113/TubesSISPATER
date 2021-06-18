# import library socket karena akan menggunakan IPC socket
import socket

def cetakVersiSekarang(now_server):
    #Output versi sekarang di server
    print("Versi sekarang adalah : " + now_server)

def cetakHistoryVersionServer(history_server):
    #Output seluruh versi di server
    print("History Versi di Server adalah ")
    for i in range(0,len(history_server)):
        print(history_server[i])

def namaVersiSama(history_server, new_server):
    #Cek apakah nama versi sudah pernah ada di history, jika sama return True dan sebaliknya
    for i in range(0,len(history_server)):
        if (history_server[i] == new_server):
            return True
    return False

def rilisVersiBaru(history_server, now_server):
    #Memasukkan versi baru server
    new_server = input("Masukkan nama versi baru yang akan dirilis: ")
    if (not namaVersiSama(history_server, new_server) and (new_server != now_server)):
        history_server.append(now_server)
        print("Versi baru berhasil ditambahkan")
    else:
        print("Gagal menambahkan Versi, karena nama Versi sudah ada")
    return new_server

def listenDariClient(now_server):
    #Melakukan Listen dari Client kalau Client melakukan menu 3 atau 4

    # menerima koneksi
    conn, addr = s.accept()
	
	# menampilkan koneksi berupa IP dan port client yang terhubung menggunakan print
    print("\nBerhasil menerima dari Client dengan Address: ", addr)
	
	# menerima data berdasarkan ukuran buffer
    now_client = conn.recv(BUFFER_SIZE)
	
	# mengirim kembali data yang diterima dari client kepada client
    conn.send(now_server.encode())

    # menutup koneksi
    conn.close()

def menu():
    print("\nSelamat datang di sisi server, silakan pilih menu yang akan dipilih : ")
    print("1. Melihat Versi Sekarang")
    print("2. Melihat History Versi di Server")
    print("3. Rilis Versi Baru")
    print("4. Listening dari Client")
    print("0. Keluar")

def pilihan(pil, history_server, now_server):
    new_server = now_server     #inisialisasi new server, kalau tidak ada perubahan maka new server akan tetap sama dengan sekarang
    if (pil == 1):
        cetakVersiSekarang(now_server)
    elif (pil == 2):
        cetakHistoryVersionServer(history_server)
    elif (pil == 3):
        new_server = rilisVersiBaru(history_server, now_server)         #menampung new server berisi versi server baru
    elif (pil == 4):
        listenDariClient(now_server)
    else:
        print("Masukkan Angka yang valid!")
    return new_server   #melakukan return versi server

# definisikan alamat IP binding, port, buffer size  yang akan digunakan 
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

#list history versi
history_server = ["1.1.1", "1.1.2", "1.1.3", "1.2.1", "1.2.4", "1.2.5", "1.2.6"]

#versi server
now_server = "1.2.7"

# buat socket bertipe TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan bind
s.bind((TCP_IP, TCP_PORT))

# server akan listen menunggu hingga ada koneksi dari client
s.listen(1)

# lakukan loop forever
while True:
    menu()
    pil = int(input("Masukkan pilihan Anda: "))
    if (pil == 0):
        break
    else:
        now_server = pilihan(pil, history_server, now_server)

# tutup koneksi
s.close()