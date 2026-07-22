# AYO Technical Test - Automation QA

Repo ini berisi automation test untuk studi kasus QA AYO Technical Test, meliputi validasi booking, web checks, dan skenario mobile app.

## Studi Kasus 1 - Booking Validation

Terdapat data booking yang disimpan di tabel database dengan masalah:

- Booking `BK/000001` salah harga: terjadwal di slot `09:00-11:00` seharga 1.000.000, tapi tersimpan `1.200.000`.
- Double booking: `BK/000001` dan `BK/000005` bertabrakan di venue, tanggal, dan waktu yang sama.

Kedua masalah ini dapat terdeteksi lebih awal menggunakan automation test dalam repo ini.

### Test Scenario

| ID | Scenario | Expected Result |
|----|----------|-----------------|
| SC-01 | Booking venue 15, tanggal `2022-12-10`, start `09:00`, end `11:00` | Harga sesuai jadwal `1.000.000` |
| SC-02 | Booking baru di waktu yang sama setelah `BK/000001` | Sistem menolak / mendeteksi double booking |
| SC-03 | Booking di slot yang tidak ada | Sistem menolak / tidak valid |
| SC-04 | Booking tidak overlap dengan booking lain | Sistem menerima booking |

## Studi Kasus 2 - Web Checks (`ayo.co.id`)

Automation test untuk website AYO menggunakan Playwright dan static HTML checks.

### `/venues` - Daftar Venue
- Venue listing menampilkan jumlah venue tersedia.
- Filter cabang olahraga bekerja.
- Pagination dapat berpindah ke halaman 2.
- FAQ dapat di-expand.
- CTA `Daftarkan Venue` dapat diklik.

### `/main-bareng` - Event Mabar
- Halaman menampilkan heading `EVENT MAIN BARENG`.
- Daftar event mabar tampil.
- Tombol `Cari mabar` dan `Filter` tersedia.
- Navigasi pagination event aktif.
- Mobile viewport `375x812` divalidasi.

## Studi Kasus 3 - Mobile App AYO

Skenario pengujian untuk aplikasi mobile AYO di iOS.

### Book Venue Booking
- Search venue
- Filter cabang olahraga dan kota
- Pilih tanggal dan slot waktu
- Verifikasi harga
- Pembayaran

### Create Game Time
- Buat game time baru
- Isi detail cabang olahraga, tanggal, waktu, lokasi, kuota
- Publish dan verifikasi tampil di daftar
- Join game time

## Struktur File

- `booking_qa/test_scenario.md` - Dokumen test scenario Studi Kasus 1.
- `booking_qa/test_booking.py` - Kasus test berbasis database SQLite.
- `booking_qa/test_web_ayo.py` - Automation web checks menggunakan Playwright untuk Studi Kasus 2.
- `booking_qa/test_ayo_static.py` - Static HTML checks untuk halaman AYO.
- `booking_qa/test_scenario_venues.md` - Test scenario lanjutan untuk `/venues`.
- `booking_qa/test_scenario_ayo_mobile.md` - Test scenario untuk mobile app AYO (Studi Kasus 3).
- `booking_qa/AYOiOS/` - Kerangka XCUITest project untuk iOS native automation.
- `booking_qa/db_setup.py` - Fungsi inisialisasi database.
- `booking_qa/schema.sql` - Definisi tabel booking.
- `booking_qa/seed.sql` - Data seed untuk reproduksi masalah.
- `test_booking.py` - Skrip verifikasi standalone tanpa database.

## Prasyarat

- Python 3.11+
- Virtualenv sudah dibuat di `.venv`
- Dependensi: `pytest`
- Browser untuk Playwright: `playwright install chromium`

## Menjalankan Test

Aktifkan virtualenv lalu jalankan pytest:

```bash
cd /Users/RioZ/Ayo_technical_test
source .venv/bin/activate
pytest -q
```

Jalankan file spesifik:

```bash
pytest booking_qa/test_booking.py -q
pytest booking_qa/test_web_ayo.py -q
pytest booking_qa/test_ayo_static.py -q
```

Jalankan file standalone:

```bash
python test_booking.py
```

## Menjalankan dari IDE (VSCode)

1. Buka folder `/Users/RioZ/Ayo_technical_test`.
2. Pilih interpreter Python: `.venv/bin/python`.
3. Install dependensi jika belum:
   ```bash
   pip install pytest playwright beautifulsoup4 requests
   playwright install chromium
   ```
4. Buka file test yang ingin dijalankan, misal:
   - `booking_qa/test_booking.py`
   - `booking_qa/test_web_ayo.py`
   - `booking_qa/test_ayo_static.py`
5. Untuk menjalankan semua test: gunakan panel Test Explorer atau jalankan perintah `pytest -q` di terminal.
6. Untuk debug: klik di sebelah nomor baris untuk menambahkan breakpoint, lalu pilih `Run > Start Debugging`.

## Catatan Hasil Test

Saat ini ada 2 test yang sengaja diharapkan **FAIL** untuk mendeteksi bug booking:
- Harga booking `BK/000001` tidak sesuai jadwal.
- Double booking antar booking di venue/tanggal/waktu yang sama.
