from tabulate import tabulate

daftar_karyawan = [
    ["KYM-001","Dudi", "Human Resources", "Staff", "Aktif", 75],
    ["KYM-002", "Sule", "Digital Marketing", "Spesialis", "Aktif", 90],
    ["KYM-003", "Ibe", "Socmed Specialist", "Staff", "Resign", 80],
    ["KYM-004", "Wynne", "Kol", "Staff", "Aktif", 85],
    ["KYM-005", "Barto", "Human Resources", "Manager", "Resign", 60],
    ["KYM-006", "Rifki", "Finance", "Manager", "Cuti", 90]
]
kolom = ["ID Karyawan", "Nama", "Departemen", "Jabatan", "Status Pekerjaan", "Nilai Evaluasi"]

#Helper 
def cek_id():
  while True:
    cari_karyawan =  input ("Masukan ID Karyawan (Jika Tidak Ada, Ketik '-'): ").upper()
    if cari_karyawan == '-':
      return 
    elif len(cari_karyawan) != 7 or '-' not in cari_karyawan:
      print("ID Harus berjumlah 7 Karakter dan dipisahkan oleh tanda '-' (KYM-001)")
      continue
    elif cari_karyawan[:3] != 'KYM':
      print("ID salah karena tidak sesuai dengan kode karyawan perusahaan (KYM)")
      continue
    elif not cari_karyawan[4:].isdigit():
      print("Tiga karakter setelah tanda '-' harus angka (KYM-001)")
      continue
    return cari_karyawan


#CRUD
def TabelKaryawan(data_karyawan = None): #READ
  if data_karyawan is None:  #Semua daftar karyawan
    print("\n Tabel Karyawan")
    baris = [karyawan for  karyawan in daftar_karyawan]
  else: #Data karyawan tertentu (Parameter terisi)
    baris = data_karyawan
  print(tabulate(baris, headers=kolom, tablefmt='fancy_grid', stralign='center', numalign='center'))
  return

def TambahKaryawan(): #CREATE
  TabelKaryawan()
  while True:
    input_id = cek_id()
    if input_id is None:
      print("Program Dibatalkan") 
      return

    list_id = [karyawan[0] for karyawan in daftar_karyawan]
    if input_id in list_id:    
        print("ID Karyawan Sudah Terdaftar")
        continue
    else:
        nama_karyawan = input("Masukan Nama Karyawan: ").title()
        dep_karyawan = input("Masukan Nama Departemen: ").title()   
        jab_karyawan = input("Masukan Jabatan Karyawan: ").title()
        
        while True:
          stat_karyawan = input("Masukan Status Pekerjaan (Aktif/Resign/Cuti): ").title()
          if stat_karyawan in ['Aktif', 'Resign', 'Cuti']:
            break
          else:
            print("Status hanya dapat di input dengan Aktif/Resign/Cuti ")

        while True:
          try: 
            nilai_karyawan = float(input("Masukan Nilai Evaluasi Karyawan: "))
            if 0 <= nilai_karyawan <= 100:
              break
            else:
              print("Nilai harus di antara 0 hingga 100!")
          except ValueError:
            print("Input salah, Harap masukan angka bulat atau desimal yang dipisahkan oleh titik (contoh: 80 atau 80.5) ")
          
        daftar_karyawan.append([input_id, nama_karyawan, dep_karyawan, jab_karyawan, stat_karyawan, nilai_karyawan])
        print("\nDaftar Karyawan\n")
        TabelKaryawan()
        print(f"\nData karyawan {nama_karyawan} berhasil di tambahkan")
        return


def UpdateKaryawan(): #UPDATE
    TabelKaryawan()
    while True:
      input_id = cek_id()
      if input_id is None:
        print("Program Dibatalkan") 
        return
      
      data_id = [karyawan[0] for karyawan in daftar_karyawan]
      if input_id in data_id: #Validasi input id di data_id
        index_id = data_id.index(input_id)
        print("ID Karyawan ditemukan")
        break
      else:
        print(f"Data karyawan dengan ID {input_id} tidak ditemukan, silakan coba kembali")

    hasil_data = [daftar_karyawan[index_id]]
    TabelKaryawan(hasil_data)
      
    dep_baru = input("Masukan Departemen Karyawan yang ingin diubah (Jika Tidak Ada Perubahan, Ketik '-'): ").title()
    if dep_baru == '-':
      print("Update departemen dibatalkan")
    else:
      daftar_karyawan[index_id][2] = dep_baru
      print("Data perubahan departemen karyawan berhasil di update")
      
    jab_baru = input("Masukan Jabatan Karyawan yang ingin diubah  (Jika Tidak Ada Perubahan, Ketik '-'): ").title()
    if jab_baru == '-':
      print("Update jabatan dibatalkan") 
    else:
      daftar_karyawan[index_id][3] = jab_baru
      print("Data perubahan jabatan karyawan berhasil di update")
    
    while True:      
      stat_baru = input("Masukan Status Pekerjaan yang ingin diubah menjadi Aktif/Resign/Cuti (Jika Tidak Ada Perubahan, Ketik '-'): ").title()
      if stat_baru == '-':
        print("Update status pekerjaan dibatalkan")
        break
      elif stat_baru not in ['Aktif', 'Resign', 'Cuti']:
        print("Status hanya dapat diinput dengan Aktif/Resign/Cuti")
        continue
      else:
        daftar_karyawan[index_id][4] = stat_baru
        print("Data perubahan status pekerjaan karyawan berhasil di update")
        break
      
    while True:
      nilai_baru = input("Masukan Nilai Karyawan yang ingin diubah (Jika Tidak Ada Perubahan, Ketik '-'):")
      if nilai_baru == '-':
        print("Update nilai KPI dibatalkan")
        break
      else:
        try:
          nilai_float = float(nilai_baru)
          if 0 <= nilai_float <= 100:
            daftar_karyawan[index_id][5] = nilai_float
            print("Data perubahan nilai evaluasi berhasil di update")
            break
          else:
            print("Nilai harus di antara 0 hingga 100!")
        except ValueError:
          print("Input salah, Harap masukan angka bulat atau desimal yang dipisahkan oleh titik (contoh: 80 atau 80.5)")
    print("\nData Karyawan Setelah Diupdate")
    TabelKaryawan([daftar_karyawan[index_id]])
    return


def DeleteKaryawan(): #DELETE
  TabelKaryawan()
  while True:
    input_id = cek_id()
    if input_id is None:
      print("Program Dibatalkan") 
      return
      
    data_id = [karyawan[0] for karyawan in daftar_karyawan]
    if input_id in data_id: #Validasi input id di data_id
      index_id = data_id.index(input_id)
      print("ID Karyawan ditemukan")
      break
    else:
        print(f"Data karyawan dengan ID {input_id} tidak ditemukan, silakan coba kembali")

  hapus_karyawan = daftar_karyawan[index_id]
  print(f"Data yang akan dihapus --> ID Karyawan: {hapus_karyawan[0]} / Nama:{hapus_karyawan[1]}")
  while True:
    pilihan = input("Apakah anda yakin ingin menghapus data karyawan ini (Ya/Tidak): ").capitalize()
    if pilihan == "Ya":
      daftar_karyawan.pop(index_id)
      print("Data Karyawan Berhasil Dihapus")
      TabelKaryawan()
      return
    elif pilihan == "Tidak":
      print("Penghapusan Data Karyawan Dibatalkan")
      return
    else:
      print("Input tidak valid, harap ketik Ya/Tidak")
       
       
def HitungKPI(): #FITUR TAMBAHAN
  TabelKaryawan()
  while True:
    input_id = cek_id()
    if input_id is None:
      print("Program Dibatalkan") 
      return
      
    data_id = [karyawan[0] for karyawan in daftar_karyawan]
    if input_id in data_id: #Validasi input id di data_id
      index_id = data_id.index(input_id)
      print("ID Karyawan ditemukan")
      break
    else:
        print(f"Data karyawan dengan ID {input_id} tidak ditemukan, silakan coba kembali")

  data_karyawan = [daftar_karyawan[index_id]]
  TabelKaryawan(data_karyawan)
   
  hard_skill = 0.5 
  soft_skill = 0.3 
  disiplin = 0.2 

  while True:
    try:
      hard = float(input("Masukan Nilai Hard Skill/Target Achieved: "))
      if 0 <= hard <= 100:
        break
      else:
        print("Nilai harus di antara 0 hingga 100!")
    except ValueError:
      print("Input salah, Harap masukan angka bulat atau desimal yang dipisahkan oleh titik (contoh: 80 atau 80.5) ")

  while True:
    try:
      soft = float(input("Masukan Nilai Soft SKill/Teamwork: "))
      if 0 <= soft <= 100:
        break
      else:
        print("Nilai harus di antara 0 hingga 100!")
    except ValueError:
      print("Input salah, Harap masukan angka bulat atau desimal yang dipisahkan oleh titik (contoh: 80 atau 80.5) ")

  while True:
    try:   
      disc = float(input("Masukan Nilai Kedisiplinan/Attendance: "))
      if 0 <= disc <= 100:
        break
      else:
        print("Nilai harus di antara 0 hingga 100!")
    except ValueError:
      print("Input salah, Harap masukan angka bulat atau desimal yang dipisahkan oleh titik (contoh: 80 atau 80.5) ")

  hitung_kpi = round((hard * hard_skill) + (soft * soft_skill) + (disc * disiplin), 2)
  nama_karyawan = daftar_karyawan[index_id][1] 
  daftar_karyawan[index_id][5] = hitung_kpi #Menggantikan nilai KPI lama di tabel utama
  
  if hitung_kpi > 90:
    print(f"Status Evaluasi: EXCELLENT - Karyawan {nama_karyawan} menunjukan performa luar biasa dan melebihi target, dengan skor akhir: {hitung_kpi}")
  elif hitung_kpi >= 75:
    print(f"Status Evaluasi: GOOD - Karyawan {nama_karyawan} menunjukan performa yang stabil dan memenuhi standar, dengan skor akhir: {hitung_kpi}")
  elif hitung_kpi >= 65:
    print(f"Status Evaluasi: FAIR - Karyawan {nama_karyawan} cukup, namun butuh peningkatan, dengan skor akhir: {hitung_kpi}")
  else:
    print(f"Status Evaluasi: POOR - Karyawan {nama_karyawan} di bawah standar perusahaan, dengan skor akhir: {hitung_kpi}") 
  return


while True:
  print("Selamat Datang di Program HR")
  print("List Menu")
  print("1.Tabel Karyawan")
  print("2.Tambah Karyawan")
  print("3.Update Karyawan")
  print("4.Hapus Karyawan")
  print("5.Hitung Nilai KPI")
  print("6.Exit Program")
  daftar_menu = input("Pilih Menu: ")

  
  if daftar_menu == '1': TabelKaryawan()
  elif daftar_menu == '2': TambahKaryawan()
  elif daftar_menu == '3': UpdateKaryawan()
  elif daftar_menu == '4': DeleteKaryawan()
  elif daftar_menu == '5': HitungKPI()
  elif daftar_menu == '6': 
    print("Terima kasih telah menggunakan program ini!")
    break
  else:
    print("Input diluar menu yang sudah ditentukan, silahkan melakukan input ulang")






