def tanbah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return "error: pembagian oleh nol"
    return x /y

def kalkulator():
    while True:
        print("\n--- Kalkulator Sederhana ---")
        print("1. Tambah")
        print("2. Kurang")
        print("3. Kali")
        print("4. Bagi")
        print("5. Keluar")

        pilihan = input("masukkan pilihan(1-5):")
        if pilihan == '5':
            print("Terima kasih sudah menggunakan kalkulator ini!")
            break

        if pilihan not in ['1', '2', '3', '4']:
            print("Input yang anda masukkan salah! Silahkan coba lagi.")
            continue

        try:
            angka1 = float(input("masukkan angka pertana:"))
            angka2 = float(input("Masukkan angka kedua:"))
        except ValueError:
            print("Input yang anda masukkan bukan angka! Silahkan coba lagi.")
            continue

        if pilihan == '1':
            hasil = tanbah(angka1, angka2)
            print(f"hasil: {angka1} + {angka2} = {hasil}")
        elif pilihan == '2':
            hasil = kurang(angka1, angka2)
            print(f"Hasil: {angka1} - {angka2} = {hasil}")
        elif pilihan == '3':
            hasil = kali(angka1, angka2)
            print(f"Hasil: {angka1} x {angka2} = {hasil}")
        elif pilihan == '4':
            hasil = bagi(angka1, angka2)
            print(f"Hasil: {angka1} ÷ {angka2} = {hasil}")

    if __name__ == '__main__':
        kalkulator()