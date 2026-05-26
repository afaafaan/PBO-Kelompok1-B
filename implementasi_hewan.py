from abstraksi_hewan import Hewan, BisaTerbang, BisaBerenang

class Burung(Hewan, BisaTerbang):
    def makan(self):
        print(f"{self.nama} sedang makan.")

    def terbang(self):
        print(f"{self.nama} sedang terbang.")

class Singa(Hewan):
    def makan(self):
        print(f"{self.nama} sedang makan.")

class Sapi(Hewan):
    def makan(self):
        print(f"{self.nama} sedang makan.")
