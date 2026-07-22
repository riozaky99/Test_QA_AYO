# Test Scenario - Booking Validation

## Background
Terdapat data booking yang menyimpan harga dan jadwal venue. Data yang terinput harus sesuai dengan tabel jadwal/price, dan tidak boleh terjadi double booking untuk venue, tanggal, dan waktu yang sama.

## Test Objectives
1. Memastikan harga booking sesuai dengan jadwal yang tersimpan.
2. Memastikan sistem menolak/men-error saat ada double booking (venue + tanggal + rentang waktu bertabrakan).

## Test Data
### Jadwal Venue (venue_id = 15, tanggal = 2022-12-10)
- 07:00 - 09:00 => 800.000
- 09:00 - 11:00 => 1.000.000
- 11:00 - 13:00 => 1.200.000

### Booking Issue
- BK/000001: 2022-12-10 09:00-11:00, price 1.200.000 (expected 1.000.000)
- BK/000005: 2022-12-10 09:00-11:00, price 1.000.000 (double booking dengan BK/000001)

## Scenarios

| ID | Scenario | Expected Result |
|----|----------|-----------------|
| SC-01 | Booking dengan venue_id=15, tanggal=2022-12-10, start=09:00, end=11:00 | Harga yang disimpan harus **1.000.000** |
| SC-02 | Booking dengan venue_id=15, tanggal=2022-12-10, start=09:00, end=11:00 (sudah ada BK/000001) | Sistem mengembalikan error/menolak booking baru (double booking) |
| SC-03 | Booking di luar rentang jadwal (misal 08:00-10:00) | Sistem mengembalikan error/tidak valid |

## Notes
- Validasi harga dilakukan berdasarkan `start_time` yang cocok dengan slot jadwal.
- Double booking ditentukan dengan memeriksa irisan waktu (`start < existing.end` dan `end > existing.start`).
