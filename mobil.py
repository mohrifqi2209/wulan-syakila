# Kelas induk (Parent Class)
class Kendaraan:
    def _init_(self, merk, tahun):
        self.__merk = merk  # Atribut privat
        self.__tahun = tahun  # Atribut privat

    # Getter untuk merk
    def get_merk(self):
        return self.__merk

    # Setter untuk merk
    def set_merk(self, merk):
        self.__merk = merk

    # Getter untuk tahun
    def get_tahun(self):
        return self.__tahun

    # Setter untuk tahun
    def set_tahun(self, tahun):
        if tahun > 1885:  # Tahun pertama mobil dibuat
            self.__tahun = tahun
        else:
            print("Tahun tidak valid!")

# Kelas turunan (Child Class)
class MobilSport(Kendaraan):
    def _init_(self, merk, tahun, kecepatan_max):
        super()._init_(merk, tahun)  # Memanggil konstruktor kelas induk
        self.__kecepatan_max = kecepatan_max  # Atribut privat

    # Getter untuk kecepatan_max
    def get_kecepatan_max(self):
        return self.__kecepatan_max

    # Setter untuk kecepatan_max
    def set_kecepatan_max(self, kecepatan_max):
        if kecepatan_max > 0:
            self.__kecepatan_max = kecepatan_max
        else:
            print("Kecepatan maksimal harus lebih dari 0")

# Membuat objek dari kelas MobilSport
mobil = MobilSport("Ferrari", 2023, 350)

# Menggunakan getter untuk menampilkan informasi
print(f"Merk: {mobil.get_merk()}")
print(f"Tahun: {mobil.get_tahun()}")
print(f"Kecepatan Maksimal: {mobil.get_kecepatan_max()} km/h")

# Mengubah nilai menggunakan setter
mobil.set_merk("Lamborghini")
mobil.set_tahun(2024)
mobil.set_kecepatan_max(400)

# Menampilkan informasi setelah perubahan
print("\nSetelah perubahan:")
print f"Merk: {mobil.get_merk()}")
print(f"Tahun: {mobil.get_tahun()}")
print(f"Kecepatan Maksimal: {mobil.get_kecepatan_max()} km/h")