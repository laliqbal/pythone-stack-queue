stack=[]
def Tambah_barang(stack,barang_baru):
    stack.append(barang_baru)
    print(f"{barang_baru}berhasil di tambahkan ke dalam stack")
    
def hapus_barang_terakhir(stack):
    if len(stack)==0:
        print("stack kosong tidak ada barang yang di hapus")
    else:
        barang_terakhir = stack.pop()
        print(f"{barang_terakhir}berhasil di hapus dari stack")
    
def Tampilkan_barang_teratas(stack):
    if len(stack)==0:
        print("stack kosong. tidak ada barang yang dapat di tampilkan")
    else:
        barang_teratas = stack[-1]
        print(f"barang teratas di dalam stack adalah{barang_teratas}")
        
while True:
    print("\nGudang saat ini:",stack)
    print("Menu:")
    print("1. tambah barang")
    print("2. Hapus barang terakhir")
    print("3. Tampilkan barang teratas")
    print("4. Keluar")
    
    pilihan=input("Masuki pilihan anda (1/2/3/4):")
    if pilihan == "1":
        barang_baru=input("Masukan nama baraang yang ingin di tambahkan: ")
        Tambah_barang(stack, barang_baru)
    elif pilihan == "2":
        hapus_barang_terakhir(stack)
    elif pilihan == "3":
        Tampilkan_barang_teratas(stack)
    elif pilihan == "4":
        print("Terimakasi telah menggunakan program ini.")
        break
    else:
        print("pilihan tidak valid silakan masukan pilihan yang benar")
