# Lab-8.py

### Nama : Arifin Syahrul Azhadi Harahap

### NIM : 352310965

### Kelas : IE.23.C.13

### Mata Kuliah : Program Komputer + Praktek

### Dosen : Agung Nugroho, S.Kom., M.Kom.
---

## Membuat program sederhana dengan mengaplikasikan penggunaan class.

## A. Algoritma Program
1. **Inisialisasi Objek**:
   - Buat kelas `DaftarNilaiMahasiswa`.
   - Tambahkan atribut `data_mahasiswa` berupa dictionary kosong untuk menyimpan data mahasiswa.

#### Method `tambah(nama, nilai)`
2. Input:
   - `nama`: Nama mahasiswa.
   - `nilai`: Nilai mahasiswa.
3. Proses:
   - Tambahkan pasangan nama dan nilai ke dalam `data_mahasiswa`.
4. Output:
   - Cetak pesan konfirmasi bahwa data berhasil ditambahkan.

#### Method `tampilkan()`
5. Proses:
   - Periksa apakah `data_mahasiswa` kosong.
   - Jika kosong:
     - Cetak pesan "Belum ada data mahasiswa."
   - Jika tidak kosong:
     - Iterasi setiap pasangan nama dan nilai di dalam `data_mahasiswa`.
     - Cetak nama dan nilai mahasiswa.
6. Output:
   - Daftar mahasiswa dan nilainya.

#### Method `hapus(nama)`
7. Input:
   - `nama`: Nama mahasiswa yang ingin dihapus.
8. Proses:
   - Periksa apakah `nama` ada dalam `data_mahasiswa`.
   - Jika ada:
     - Hapus data berdasarkan `nama`.
     - Cetak pesan konfirmasi.
   - Jika tidak ada:
     - Cetak pesan bahwa data tidak ditemukan.

#### Method `ubah(nama, nilai_baru)`
9. Input:
   - `nama`: Nama mahasiswa yang ingin diubah nilainya.
   - `nilai_baru`: Nilai baru untuk mahasiswa.
10. Proses:
    - Periksa apakah `nama` ada dalam `data_mahasiswa`.
    - Jika ada:
      - Perbarui nilai mahasiswa dengan `nilai_baru`.
      - Cetak pesan konfirmasi.
    - Jika tidak ada:
      - Cetak pesan bahwa data tidak ditemukan.

### Contoh Penggunaan
11. **Tambahkan Data**:
    - Panggil `tambah` dengan nama dan nilai mahasiswa.
12. **Tampilkan Data**:
    - Panggil `tampilkan` untuk melihat daftar mahasiswa.
13. **Ubah Data**:
    - Panggil `ubah` dengan nama dan nilai baru untuk memperbarui data.
14. **Hapus Data**:
    - Panggil `hapus` dengan nama mahasiswa untuk menghapus data.
15. **Ulangi Proses**:
    - Ulangi langkah sesuai kebutuhan hingga selesai.

## B. Diagram Class

![Diagram Class Lab 8 py](https://github.com/user-attachments/assets/52cee21a-71cf-4ba8-9729-b1984c312fce)

   
## C. Gambar Flowchart Program

![Flow  Chart Lab 8 drawio](https://github.com/user-attachments/assets/bae01993-c7c8-426c-83a9-3107fc12423e)

## D. Menampilkan Program dan penjelasan Yang telah dibuat menggunakan program penggunaan "Class"

    ```python
    
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

#### Contoh penggunaan
mahasiswa1 = Mahasiswa("Arifin Syahrul")

mahasiswa1.tambah_nilai(80, 75, 90)

mahasiswa1.tambah_nilai(70, 80, 85)

mahasiswa1.tampilkan_nilai()

mahasiswa1.hapus_nilai(0)

mahasiswa1.tampilkan_nilai()

mahasiswa1.ubah_nilai(0, 85, 90, 95)

mahasiswa1.tampilkan_nilai()

---

Berikut penjelasan programnya;

### Penjelasan Program
Program ini menggunakan konsep **Object-Oriented Programming (OOP)** untuk membuat aplikasi sederhana yang dapat menyimpan, menampilkan, mengubah, dan menghapus data nilai mahasiswa. Setiap mahasiswa direpresentasikan dengan pasangan `nama` (sebagai key) dan `nilai` (sebagai value), disimpan dalam sebuah dictionary.

Program ini dibangun dalam bentuk **class**, yang memiliki:
1. **Atribut (`data_mahasiswa`)**: Dictionary untuk menyimpan data mahasiswa.
2. **Methods (Fungsi)**:
   - `tambah`: Menambahkan data mahasiswa ke dalam dictionary.
   - `tampilkan`: Menampilkan semua data mahasiswa.
   - `hapus`: Menghapus data mahasiswa berdasarkan nama.
   - `ubah`: Mengubah nilai mahasiswa berdasarkan nama.

---

### Cara Pembuatan Program
1. **Buat Class**
   - Mulai dengan mendefinisikan class `DaftarNilaiMahasiswa`:
     ```python
     class DaftarNilaiMahasiswa:
         def __init__(self):
             self.data_mahasiswa = {}
     ```
   - Method `__init__` adalah konstruktor yang digunakan untuk menginisialisasi atribut `data_mahasiswa` sebagai dictionary kosong.

2. **Buat Method Tambah**
   - Tambahkan method untuk menyimpan data ke dictionary:
     ```python
     def tambah(self, nama, nilai):
         self.data_mahasiswa[nama] = nilai
         print(f"Data {nama} dengan nilai {nilai} berhasil ditambahkan.")
     ```

3. **Buat Method Tampilkan**
   - Method ini akan menampilkan semua data mahasiswa yang tersimpan:
     ```python
     def tampilkan(self):
         if not self.data_mahasiswa:
             print("Belum ada data mahasiswa.")
         else:
             print("Daftar Nilai Mahasiswa:")
             for nama, nilai in self.data_mahasiswa.items():
                 print(f"Nama: {nama}, Nilai: {nilai}")
     ```

4. **Buat Method Hapus**
   - Method ini akan menghapus data mahasiswa berdasarkan nama:
     ```python
     def hapus(self, nama):
         if nama in self.data_mahasiswa:
             del self.data_mahasiswa[nama]
             print(f"Data {nama} berhasil dihapus.")
         else:
             print(f"Data dengan nama {nama} tidak ditemukan.")
     ```

5. **Buat Method Ubah**
   - Method ini akan memperbarui nilai mahasiswa berdasarkan nama:
     ```python
     def ubah(self, nama, nilai_baru):
         if nama in self.data_mahasiswa:
             self.data_mahasiswa[nama] = nilai_baru
             print(f"Nilai {nama} berhasil diubah menjadi {nilai_baru}.")
         else:
             print(f"Data dengan nama {nama} tidak ditemukan.")
     ```

6. **Gunakan Program**
   - Inisialisasi objek dan gunakan method sesuai kebutuhan:
     ```python
     daftar = DaftarNilaiMahasiswa()
     daftar.tambah("Arifin Syahrul", 80, 75, 90)
     daftar.tampilkan()
     daftar.ubah("Arifin Syahrul", 80, 90, 95)
     daftar.tampilkan()
     daftar.tampilkan()
     ```

---

### Output Program
Berikut contoh hasil eksekusi:
```
Data Arifin Syahrul dengan nilai 80, 75, 90 berhasil ditambahkan.
Daftar Nilai Mahasiswa:
Nama: Arifin Syharul, Nilai: 80, 75, 90
Nilai Arifin Syahrul berhasil diubah menjadi 80, 90, 95.
```

## E. Hasil OutPut Program

![Output Lab 8 py](https://github.com/user-attachments/assets/9008f5c8-e44f-430d-8b1f-fee10e62d4f1)

### Selesai


