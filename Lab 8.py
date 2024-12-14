class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama
        self.nilai = []

    def tambah_nilai(self, nilai_tugas, nilai_uts, nilai_uas):
        self.nilai.append((nilai_tugas, nilai_uts, nilai_uas))

    def tampilkan_nilai(self):
        print(f"Nilai untuk {self.nama}:")
        for i, nilai in enumerate(self.nilai):
            print(f"Nilai {i+1}: Tugas={nilai[0]}, UTS={nilai[1]}, UAS={nilai[2]}")

    def hapus_nilai(self, index):
        if 0 <= index < len(self.nilai):
            del self.nilai[index]
        else:
            print("Index tidak valid")

    def ubah_nilai(self, index, nilai_tugas, nilai_uts, nilai_uas):
        if 0 <= index < len(self.nilai):
            self.nilai[index] = (nilai_tugas, nilai_uts, nilai_uas)
        else:
            print("Index tidak valid")

# Contoh penggunaan
mahasiswa1 = Mahasiswa("Arifin Syahrul")
mahasiswa1.tambah_nilai(80, 75, 90)
mahasiswa1.tambah_nilai(70, 80, 85)

mahasiswa1.tampilkan_nilai()

mahasiswa1.hapus_nilai(0)

mahasiswa1.tampilkan_nilai()

mahasiswa1.ubah_nilai(0, 85, 90, 95)

mahasiswa1.tampilkan_nilai()


