def menu():
    print("\n--- MENU ANTRIAN KLINIK ---")
    print("1. Cek ID Database")
    print("2. Cek Status Urutan")
    print("3. Isi Daftar Pasien")
    print("4. Lihat Nama Pasien")
    print("5. Selesai")

def main():
    a = [0] * 5 
    running = True
    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka!")
        if choice == 1:
            print(f"ID Database: {id(a)}")
        elif choice == 2:
            for i in range(5):
                print(f"Urutan {i} ID: {id(a[i])}")
        elif choice == 3:
            print("Masukkan 5 Nama Pasien:")
            for i in range(5):
                a[i] = input(f"Antrian ke-{i}: ")
        elif choice == 4:
            print("Daftar Pasien:")
            for i in range(5):
                print(f"Antrian {i}: {a[i]}")
        elif choice == 5:
            running = False
            print("Program keluar.")
        else:
            print("Pilihan tidak ada.")

if __name__ == "__main__":
    main()