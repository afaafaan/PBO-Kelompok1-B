from abc import ABC, abstractmethod

# SEMENTARA
class Hewan(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def makan(self):
        pass

class BisaTerbang(ABC):
    @abstractmethod
    def terbang(self):
        pass

# TUGAS NO 4

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