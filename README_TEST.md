# Dokumentasi Penggunaan Automation Test - AYO Technical Test

## Versi Python yang digunakan
- Python 3.11.15
- Pytest 9.1.1
- SQLite3 (built-in)

## Test Case: Studi Kasus 1
Memastikan:
- Booking price sesuai slot jadwal (`venue_slots`)
- Double booking terdeteksi untuk `venue_id + date + rentang waktu`

## Struktur Folder
```
booking_qa/
├── __init__.py
├── db_setup.py        # Init schema + seed SQLite
├── schema.sql         # DDL untuk bookings + venue_slots
├── seed.sql           # Data sample (mencerminkan bug harga + double booking)
├── test_booking.py    # Test suite berbasis DB
└── test.db            # SQLite database (dibuat otomatis)
```

## Setup Database
```bash
python3.11 booking_qa/db_setup.py
```

## Menjalankan Test
```bash
python3.11 -m pytest booking_qa/test_booking.py -v
```

Expected result:
```
FAILED booking_qa/test_booking.py::TestBookingPriceValidation::test_price_should_match_schedule
  -> Harga booking BK/000001 salah (expected 1000000, got 1200000)
PASSED booking_qa/test_booking.py::TestBookingPriceValidation::test_double_booking_detected
PASSED booking_qa/test_booking.py::TestBookingPriceValidation::test_no_double_booking_when_slot_available
PASSED booking_qa/test_booking.py::TestBookingPriceValidation::test_price_invalid_for_slot
```

## Menambahkan Data Baru
Edit `booking_qa/seed.sql`, lalu jalankan ulang:
```bash
python3.11 booking_qa/db_setup.py  # overwrite test.db
```

## Catatan
- Jika folder migration terpisah, tambahkan ke `schema.sql`
- Semua test berbasis SQLite (`booking_qa/test.db`), tidak perlu server FastAPI
