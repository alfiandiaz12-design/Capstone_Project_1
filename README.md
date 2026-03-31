## **HR Management System**

Program manajemen data karyawan yang dibangun menggunakan Python. Program ini memungkinkan pengguna untuk mengelola data karyawan dengan fitur CRUD (Create, Read, Update, Delete) dan perhitungan KPI (Key Performance Indicator).



###### **Fitur**

* **Tabel Karyawan** — Menampilkan seluruh data karyawan dalam format tabel
* **Tambah Karyawan** — Menambahkan data karyawan baru dengan validasi input
* **Update Karyawan** — Mengubah data karyawan yang sudah ada (departemen, jabatan, status, nilai)
* **Hapus Karyawan** — Menghapus data karyawan dengan konfirmasi
* **Hitung KPI** — Menghitung nilai KPI karyawan berdasarkan Hard Skill, Soft Skill, dan Kedisiplinan



###### **Struktur Data Karyawan**

|**Field**|**Tipe**|**Keterangan**|
|-|-|-|
|ID Karyawan|String|Format KYM-XXX, unik|
|Nama|String|Nama lengkap karyawan|
|Departemen|String|Nama departemen|
|Jabatan|String|Jabatan karyawan|
|Status Pekerjaan|String|Aktif / Resign / Cuti|
|Nilai Evaluasi|Float|Rentang 0–100|





###### **Perhitungan KPI**

KPI dihitung berdasarkan 3 komponen dengan bobot sebagai berikut:

|**Komponen**|**Bobot**|
|-|-|
|Hard Skill / Target Achieved|50%|
|Soft Skill / Teamwork|30%|
|Kedisiplinan / Attendance|20%|



**Rumus KPI:** (Hard Skill × 0.5) + (Soft Skill × 0.3) + (Disiplin × 0.2)



**Kategori hasil:**

* EXCELLENT → KPI > 90
* GOOD → KPI ≥ 75
* FAIR → KPI ≥ 65
* POOR → KPI < 65

