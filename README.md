# Pembagian Tugas 

Abyan Farisa - Git Administrator & Integrator Code

Dafa Syahrul Syah Baharudin - Analis SOLID (Teori & Identifikasi Masalah)

Faradilla Sari - Developer Abstraksi & Interface (Prinsip OCP & ISP)

Muzni Mubarok Salim - Developer Implementasi Hewan (Prinsip LSP)

Jihan Sofia - Developer Sistem Kandang & Kebun Binatang (Prinsip SRP & DIP)

Niken Syafira Zulfarida - Pengujian kode


pada file abstraksi_hewan prinsip SOLID yang digunakan Interface Segregation Principle (ISP), ini melarang kita buat bikin satu cetakan (class) raksasa yang serba bisa tapi malah bikin ribet nantinya. Makanya, keputusan buat memisahkan kemampuan BisaTerbang dan BisaBerenang secara terpisah itu udah pas banget, tujuannya biar nanti kalau mau bikin hewan yang cuma bisa berenang (kayak ikan hias),  gak bakal dipaksa buat masukin fungsi terbang yang emang gak dia butuhin. Hasilnya, struktur kode jadi jauh lebih bersih, gak saling tabrakan, dan gampang banget kalau mau ditambahin jenis hewan baru ke depannya.

pada file implementsi_hewan penerapan ISP terlihat jelas karena kelas seperti Singa dan Sapi tidak dipaksa untuk mengimplementasikan kemampuan terbang atau berenang yang tidak mereka butuhkan, melainkan hanya mengambil fungsi makan() dari kelas induknya. Di saat yang sama, kode ini juga memenuhi prinsip OCP (Open/Closed Principle), di mana sistem sekarang "terbuka untuk dikembangkan, tapi tertutup untuk diubah". Ketika ingin menambah hewan baru dengan kombinasi kemampuan yang berbeda, cukup membuat kelas baru dan menggabungkan interface yang sudah ada tanpa perlu mengotak-atik atau merusak kode lama yang sudah berjalan dengan baik.

pada file manajemen_hewan menerapkan tiga prinsip SOLID sekaligus, dengan sorotan utama pada Dependency Inversion Principle (DIP) karena kelas KebunBinatang bergantung pada KandangAbstrak (abstraksi) bukan pada Kandang (konkrit), sehingga bisa dengan mudah mengganti jenis kandang tanpa merusak sistem. Selain itu, kode ini juga memenuhi Single Responsibility Principle (SRP) dengan memisahkan tugas pengelolaan hewan di Kandang, perawatan di KebunBinatang, dan kebersihan di PembersihKandang, serta mendukung Open/Closed Principle (OCP) karena fungsi rawat_semua_hewan otomatis bisa menangani hewan baru berkemampuan terbang atau berenang tanpa perlu membongkar atau mengubah struktur logika yang sudah ada.

