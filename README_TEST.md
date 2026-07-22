## Studi Kasus 1 - Booking Validation

Terdapat data booking yang disimpan di tabel database dengan masalah:

- Booking `BK/000001` salah harga: terjadwal di slot `09:00-11:00` seharga 1.000.000, tapi tersimpan `1.200.000`.
- Double booking: `BK/000001` dan `BK/000005` bertabrakan di venue, tanggal, dan waktu yang sama.

Kedua masalah ini dapat terdeteksi lebih awal menggunakan automation test dalam repo ini.

## Test Scenario

| ID | Scenario | Expected Result |
|----|----------|-----------------|
| SC-01 | Booking venue 15, tanggal `2022-12-10`, start `09:00`, end `11:00` | Harga sesuai jadwal `1.000.000` |
| SC-02 | Booking baru di waktu yang sama setelah `BK/000001` | Sistem menolak / mendeteksi double booking |
| SC-03 | Booking di slot yang tidak ada | Sistem menolak / tidak valid |
| SC-04 | Booking tidak overlap dengan booking lain | Sistem menerima booking |

## Struktur File

- `booking_qa/test_scenario.md` - Dokumen test scenario.
- `booking_qa/test_booking.py` - Kasus test berbasis database SQLite.
- `booking_qa/db_setup.py` - Fungsi inisialisasi database.
- `booking_qa/schema.sql` - Definisi tabel booking.
- `booking_qa/seed.sql` - Data seed untuk reproduksi masalah.
- `test_booking.py` - Skrip verifikasi standalone tanpa database.

## Prasyarat

- Python 3.11+
- Virtualenv sudah dibuat di `.venv`
- Dependensi: `pytest`

## Menjalankan Test

Aktifkan virtualenv lalu jalankan pytest:

```bash
cd /Users/RioZ/Ayo_technical_test
source .venv/bin/activate
pytest booking_qa/test_booking.py -q
```

Jalankan file standalone:

```bash
python test_booking.py
```

## Menjalankan dari IDE (VSCode)

1. Buka folder `/Users/RioZ/Ayo_technical_test`.
2. Pilih interpreter Python: `.venv/bin/python`.
3. Buka file `booking_qa/test_booking.py`.
4. Untuk menjalankan semua test: gunakan panel Test Explorer atau jalankan perintah `pytest booking_qa/test_booking.py -q` di terminal.
5. Untuk debug: klik di sebelah nomor baris untuk menambahkan breakpoint, lalu pilih `Run > Start Debugging`.
