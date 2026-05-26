from abc import ABC, abstractmethod

class Hewan(ABC):
    def __init__(self, nama: str):
        self.nama = nama

    @abstractmethod
    def makan(self):
        "Setiap hewan memiliki cara makan yang berbeda-beda"
        pass

class BisaTerbang(ABC):
    @abstractmethod
    def terbang(self):
        "Hanya diimplementasikan oleh hewan yang benar-benar bisa terbang"
        pass

class BisaBerenang(ABC):
    @abstractmethod
    def berenang(self):
        "Hanya diimplementasikan oleh hewan yang bisa berenang"
        pass
