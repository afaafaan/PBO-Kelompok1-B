# Pembagian Tugas 

Abyan Farisa - Git Administrator & Integrator Code

Dafa Syahrul Syah Baharudin - Analis SOLID (Teori & Identifikasi Masalah)

Faradilla Sari - Developer Abstraksi & Interface (Prinsip OCP & ISP)

Muzni Mubarok Salim - Developer Implementasi Hewan (Prinsip LSP)

Jihan Sofia - Developer Sistem Kandang & Kebun Binatang (Prinsip SRP & DIP)

Niken Syafira Zulfarida - Pengujian kode


prinsip SOLID yang namanya Interface Segregation Principle (ISP) ini melarang kita buat bikin satu cetakan (class) raksasa yang serba bisa tapi malah bikin ribet nantinya. Makanya, keputusan buat memisahkan kemampuan BisaTerbang dan BisaBerenang secara terpisah itu udah pas banget, tujuannya biar nanti kalau mau bikin hewan yang cuma bisa berenang (kayak ikan hias),  gak bakal dipaksa buat masukin fungsi terbang yang emang gak dia butuhin. Hasilnya, struktur kode jadi jauh lebih bersih, gak saling tabrakan, dan gampang banget kalau mau ditambahin jenis hewan baru ke depannya.
