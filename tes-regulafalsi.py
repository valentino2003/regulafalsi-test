# Definisi fungsi
def f(x):
    return eval(fx)

# Metode Regula Falsi
def regulafalsi(x0, x1, e):
    step = 1
    condition = True
    while condition:
        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        print('Iterasi-%d, x2 = %0.6f dan f(x2) = %0.6f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step += 1
        condition = abs(f(x2)) > e

    return x2

# Fungsi utama aplikasi
def main():
    global fx
    fx = input("Masukkan f(x): ")

    while True:
        print("\nMENU:")
        print("1. Hitung Akar Fungsi")
        print("2. Keluar")

        choice = input("Pilih opsi (1/2): ")

        if choice == '1':
            x0 = float(input('Tebakan pertama: '))
            x1 = float(input('Tebakan kedua: '))
            e = float(input('Toleransi kesalahan: '))

            if f(x0) * f(x1) > 0.0:
                print('Tebakan awal tidak menghasilkan akar')
                print('Coba lagi dengan nilai tebakan yang berbeda')
            else:
                result = regulafalsi(x0, x1, e)
                print('Akar yang dihasilkan adalah: %0.8f' % result)
        elif choice == '2':
            print("Terima kasih telah menggunakan aplikasi.")
            break
        else:
            print("Pilihan tidak valid. Pilih 1 atau 2.")

if __name__ == '__main__':
    main()
