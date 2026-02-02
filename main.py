import json
from datetime import datetime

saldo = 0
pemasukan = []
pengeluaran = []
FILE_SALDO = "saldo.json"

def simpan_saldo():
    with open(FILE_SALDO, "w") as file:
        json.dump({
            "saldo": saldo,
            "pemasukan": pemasukan,
            "pengeluaran": pengeluaran
        }, file, indent=2)

def muat_saldo():
    global saldo, pemasukan, pengeluaran
    try:
        with open(FILE_SALDO, "r") as file:
            data = json.load(file)
            saldo = data["saldo"]
            pemasukan = data.get("pemasukan", [])
            pengeluaran = data.get("pengeluaran", [])
    except FileNotFoundError:
        saldo = 0
        pemasukan = []
        pengeluaran = []

def tambah_pemasukan():
    global saldo, pemasukan
    jumlah = float(input("Masukkan jumlah pemasukan: "))
    keterangan = input("Keterangan (opsional): ") or "Pemasukan"
    saldo += jumlah
    pemasukan.append({
        "jumlah": jumlah,
        "keterangan": keterangan,
        "tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    simpan_saldo()
    print(f"Pemasukan sebesar Rp{jumlah:,.0f} berhasil ditambahkan!")

def tambah_pengeluaran():
    global saldo, pengeluaran
    jumlah = float(input("Masukkan jumlah pengeluaran: "))
    keterangan = input("Keterangan (opsional): ") or "Pengeluaran"
    if jumlah > saldo:
        print(f"⚠️ Saldo tidak cukup! Saldo Anda: Rp{saldo:,.0f}")
    else:
        saldo -= jumlah
        pengeluaran.append({
            "jumlah": jumlah,
            "keterangan": keterangan,
            "tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        simpan_saldo()
        print(f"Pengeluaran sebesar Rp{jumlah:,.0f} berhasil dicatat!")

def lihat_saldo():
    print("\n" + "="*40)
    print(f"💰 Saldo Anda: Rp{saldo:,.0f}")
    print("="*40 + "\n")

def lihat_laporan():
    print("\n" + "="*50)
    print("📊 LAPORAN PEMASUKAN DAN PENGELUARAN")
    print("="*50)
    
    total_pemasukan = sum(p["jumlah"] for p in pemasukan)
    total_pengeluaran = sum(p["jumlah"] for p in pengeluaran)
    
    print(f"\n📈 PEMASUKAN (Total: Rp{total_pemasukan:,.0f})")
    print("-"*50)
    if pemasukan:
        for i, p in enumerate(pemasukan, 1):
            print(f"{i}. {p['keterangan']}: Rp{p['jumlah']:,.0f}")
            print(f"   Tanggal: {p['tanggal']}")
    else:
        print("Belum ada pemasukan")
    
    print(f"\n📉 PENGELUARAN (Total: Rp{total_pengeluaran:,.0f})")
    print("-"*50)
    if pengeluaran:
        for i, p in enumerate(pengeluaran, 1):
            print(f"{i}. {p['keterangan']}: Rp{p['jumlah']:,.0f}")
            print(f"   Tanggal: {p['tanggal']}")
    else:
        print("Belum ada pengeluaran")
    
    print(f"\n💰 SALDO AKHIR: Rp{saldo:,.0f}")
    print("="*50 + "\n")

def menu():
    print("=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Lihat laporan")
    print("5. Keluar")

muat_saldo()

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pemasukan()
    elif pilihan == "2":
        tambah_pengeluaran()
    elif pilihan == "3":
        lihat_saldo()
    elif pilihan == "4":
        lihat_laporan()
    elif pilihan == "5":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid")