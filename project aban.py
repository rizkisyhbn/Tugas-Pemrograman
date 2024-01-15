class MataKuliah:
    def __init__(self, kode, nama, sks):
        self.kode = kode
        self.nama = nama
        self.sks = sks

def tambah_mahasiswa():
    print("Masukkan data mahasiswa:")
    nama = input("NAMA: ")
    nim = input("NIM: ")
    prodi = input("PRODI: ")

    mahasiswa[nim] = {
        'Nama': nama,
        'prodi': prodi
    }
    print("DATA MAHASISWA BERHASIL DITAMBAHKAN")

mahasiswa = {}

def input_matakuliah():
    jumlah_matkul = int(input("Masukkan jumlah mata kuliah yang ingin diambil: "))
    daftar_matkul = []

    for i in range(jumlah_matkul):
        print(f"Masukkan detail mata kuliah ke-{i + 1}:")
        kode = input("Kode Mata Kuliah: ")
        nama = input("Nama Mata Kuliah: ")
        sks = int(input("Jumlah SKS: "))
        matkul = MataKuliah(kode, nama, sks)
        daftar_matkul.append(matkul)

    return daftar_matkul

def hitung_total_sks(daftar_matkul):
    total_sks = 0
    for matkul in daftar_matkul:
        total_sks += matkul.sks
    return total_sks

def tampilkan_krs(daftar_matkul, total_sks):
    print("\nKartu Rencana Studi (KRS):")
    for i, matkul in enumerate(daftar_matkul, start=1):
        print(f"{i}. {matkul.kode} - {matkul.nama} ({matkul.sks} SKS)")
    print(f"Total SKS yang diambil: {total_sks}")

# Fungsi utama
def main():
    print("Selamat datang di Program Kartu Rencana Studi (KRS) Mahasiswa\n")
    daftar_matkul = input_matakuliah()
    total_sks = hitung_total_sks(daftar_matkul)
    tampilkan_krs(daftar_matkul, total_sks)

while True:
    print("\nPilihan Menu:")
    print("1. Tambah Data Mahasiswa")
    print("2. Tambah KRS")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan (1/2/3): ")

    if pilihan == '1':
        tambah_mahasiswa()
    elif pilihan == '2':
        main()
    elif pilihan == '2':
        print("Terima kasih!")
        break
    elif pilihan == '3':
        print("Terima kasih")
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")


if __name__ == "__main__":
    main()
