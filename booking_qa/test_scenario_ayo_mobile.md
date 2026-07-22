# Test Scenario - AYO Mobile App

## Background
AYO adalah aplikasi mobile untuk booking lapangan olahraga, mencari lawan sparring, dan bergabung dengan kompetisi. Pengujian mobile app memfokuskan pada 2 flow utama: **Book Venue** dan **Create Game Time**.

## Device Target
- iOS 26.5 Simulator: `iPhone 17 Pro`
- iOS 26.5 Simulator: `iPhone Air`
- Device fisik iOS dengan aplikasi AYO terinstall dari App Store

## Test Objectives
1. Memastikan alur booking venue berjalan lancar dari search sampai pembayaran.
2. Memastikan alur create game time berjalan lancar dari create event sampai partisipasi.
3. Memastikan UI/UX mobile responsif dan sesuai standar.
4. Memastikan integrasi fitur pencarian, filter, dan pembayaran bekerja.

## Flow 1: Book Venue

### Precondition
- Aplikasi AYO sudah terinstall dan dibuka.
- User sudah login atau dalam mode guest.

### Scenarios

| ID | Scenario | Expected Result |
|----|----------|-----------------|
| MV-01 | Buka aplikasi AYO | Landing screen menampilkan opsi Sewa Lapangan / Main Bareng |
| MV-02 | Klik menu Sewa Lapangan | Menampilkan halaman pencarian dan filter venue |
| MV-03 | Pilih cabang olahraga | Filter cabang olahraga berfungsi, venue di-filter sesuai pilihan |
| MV-04 | Pilih kota/lokasi | Daftar venue menyesuaikan lokasi yang dipilih |
| MV-05 | Tap venue card | Navigasi ke halaman detail venue |
| MV-06 | Lihat detail venue | Menampilkan informasi venue: nama, harga, rating, fasilitas, foto |
| MV-07 | Pilih tanggal booking | Date picker menampilkan tanggal yang tersedia |
| MV-08 | Pilih slot waktu | Slot waktu tersedia sesuai jadwal venue |
| MV-09 | Verifikasi harga | Harga booking sesuai slot waktu yang dipilih |
| MV-10 | Lanjut ke pembayaran | Navigasi ke halaman pembayaran |
| MV-11 | Pembayaran berhasil | Konfirmasi booking berhasil, booking masuk ke riwayat user |

## Flow 2: Create Game Time

### Precondition
- Aplikasi AYO sudah terinstall dan dibuka.
- User sudah login.

### Scenarios

| ID | Scenario | Expected Result |
|----|----------|-----------------|
| MG-01 | Klik menu Main Bareng | Menampilkan halaman event mabar |
| MG-02 | Cari event mabar | Search dan filter menampilkan event sesuai kriteria |
| MG-03 | Buat game time baru | Form create game time dapat diisi lengkap |
| MG-04 | Isi detail game time | Input cabang olahraga, tanggal, waktu, lokasi, kuota pemain |
| MG-05 | Save/Publish game time | Game time berhasil dibuat dan tampil di daftar event |
| MG-06 | Join game time | User dapat join game time yang dibuat |
| MG-07 | Verifikasi notifikasi | User menerima notifikasi untuk game time yang di-join |

## Cross-Cutting Concerns

### Auth & User
| ID | Scenario | Expected Result |
|----|----------|-----------------|
| AU-01 | Login dengan nomor HP + OTP | Login berhasil, user diarahkan ke home |
| AU-02 | Login dengan kredensial invalid | Error message muncul, user tidak bisa login |
| AU-03 | Register akun baru | Akun berhasil dibuat, user otomatis login |
| AU-04 | Logout | User di-logout dan kembali ke login screen |

### UI/UX & Responsif
| ID | Scenario | Expected Result |
|----|----------|-----------------|
| UX-01 | Jalankan di iPhone 17 Pro (small) | Layout menyesuaikan, tidak ada elemen terpotong |
| UX-02 | Jalankan di iPhone Air (medium) | Layout optimal, navigasi tetap mudah diakses |
| UX-03 | Rotasi landscape | UI menyesuaikan orientasi layar |
| UX-04 | Pull to refresh | Refresh data berfungsi tanpa crash |
| UX-05 | Offline mode | Pesan offline muncul, fitur yang membutuhkan network di-nonaktifkan |

### Performance & Stability
| ID | Scenario | Expected Result |
|----|----------|-----------------|
| PF-01 | Cold start aplikasi | Aplikasi dibuka dalam 3 detik |
| PF-02 | Navigasi antar screen | Transisi smooth tanpa lag |
| PF-03 | Scroll list venue/event | Scroll 60fps tanpa stutter |
| PF-04 | Crash recovery | Aplikasi tidak crash saat normal usage |

## Notes
- Pada tahap awal, pengujian native app difokuskan pada flow Book Venue dan Create Game Time.
- Fitur lain seperti Chat, Competition, dan Sponsor dapat ditambahkan setelah flow utama stabil.
- Mekanisme pengujian menggunakan XCUITest untuk iOS native automation.
