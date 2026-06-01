if __name__ == "__main__":
    from implementasi_hewan import Burung, Singa, Sapi, Bebek
 
    kandang = Kandang()
    kandang.tambah_hewan(Burung("Kakaktua"))
    kandang.tambah_hewan(Singa("Simba"))
    kandang.tambah_hewan(Sapi("Moo"))
    kandang.tambah_hewan(Bebek("Donald"))
 
    print("=== Daftar Hewan ===")
    kandang.lihat_hewan()
 
    print("\n=== Merawat Semua Hewan ===")
    kebun = KebunBinatang(kandang)
    kebun.rawat_semua_hewan()
 
    print("=== Membersihkan Kandang ===")
    PembersihKandang().bersihkan()
