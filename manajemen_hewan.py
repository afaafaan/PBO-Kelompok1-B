from abstraksi_hewan import BisaTerbang, BisaBerenang

class KandangAbstrak:
    def tambah_hewan(self, hewan):
        pass

    def get_semua_hewan(self):
        pass

class Kandang(KandangAbstrak):
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)

    def get_semua_hewan(self):
        return self.hewan_list

    def lihat_hewan(self):
        for hewan in self.hewan_list:
            print(f"- {hewan.nama}")

class PembersihKandang:
    def bersihkan(self):
        print("Kandang dibersihkan.")

class KebunBinatang:
    def __init__(self, kandang: KandangAbstrak):
        self.kandang = kandang

    def rawat_semua_hewan(self):
        for hewan in self.kandang.get_semua_hewan():
            hewan.makan()
            if isinstance(hewan, BisaTerbang):
                hewan.terbang()
            if isinstance(hewan, BisaBerenang):
                hewan.berenang()
