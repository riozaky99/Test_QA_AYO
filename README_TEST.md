# Dokumentasi Penggunaan Automation Test

## 1. Python (pytest)

### Instalasi
```bash
pip3.11 install pytest
```

### Menjalankan Test
```bash
python3.11 -m pytest /Users/RioZ/Ayo_technical_test/test_booking.py -v
```

### Daftar Test Case
- `test_booking_price_matches_schedule` — Validasi harga booking sesuai harga slot jadwal
- `test_double_booking_detected` — Deteksi booking ganda di venue/date/waktu yang sama
- `test_non_overlapping_booking_accepted` — Pastikan booking tanpa overlap diterima
- `test_slot_not_found_rejected` — Pastikan booking di slot tidak valid ditolak

### Cara Menambahkan Data Baru
Edit bagian `BOOKINGS` dan `SCHEDULE` di awal file.
Format waktu harus `HH:MM:SS` dan tanggal `YYYY-MM-DD`.

---

## 2. JavaScript (Cypress)

### Instalasi
```bash
cd /Users/RioZ/Ayo_technical_test/cypress
npm install
```

### Menjalankan Test (GUI)
```bash
npm run cypress:open
```

### Menjalankan Test (Headless)
```bash
npm run cypress:run
```

### Konfigurasi
- `cypress.config.js` — Ganti `baseUrl` dengan URL aplikasi kamu
- `cypress/e2e/booking-validation.cy.js` baris 7 — Ganti `BOOKING_API` dengan endpoint API booking kamu

### Daftar Test Case
- `TC-001/TC-002` — Harga booking sesuai schedule
- `TC-003/TC-007` — Deteksi double booking
- `TC-004` — Booking tanpa overlap valid
- `TC-005` — Slot tidak ada ditolak
- **Integration** — API rejected duplikat & harga salah

---

## Catatan
Pastikan server FastAPI kamu berjalan sebelum menjalankan Cypress integration test.
Python tidak butuh server, hanya data dalam file.
