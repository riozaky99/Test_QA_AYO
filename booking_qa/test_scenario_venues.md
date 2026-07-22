# Test Scenario - Venue Listing (`ayo.co.id/venues`)

## Background
Halaman `/venues` menampilkan daftar venue olahraga yang tersedia untuk booking. Pengguna dapat mencari, memfilter, mengurutkan, dan menelusuri pagination venue. Terdapat juga FAQ dan CTA untuk pendaftaran venue.

## Test Objectives
1. Memastikan listing venue menampilkan data yang valid dan konsisten.
2. Memastikan fitur pencarian, filter, sort, dan pagination berfungsi sesuai ekspektasi.
3. Memastikan elemen pendukung seperti FAQ dan CTA dapat diakses.
4. Memastikan halaman responsif di berbagai ukuran viewport.

## Test Scenarios

### Listing & Data
| ID | Scenario | Expected Result |
|----|----------|-----------------|
| V-01 | Buka halaman `/venues` | Halaman menampilkan heading `BOOKING LAPANGAN ONLINE TERBAIK`, jumlah venue tersedia, dan minimal 1 kartu venue |
| V-02 | Verifikasi teks jumlah venue | Terlihat teks bertipe `Menampilkan X venue tersedia` |
| V-03 | Verifikasi kartu venue minimal | Minimal 1 elemen link/ kartu venue dengan atribut `href` mengandung `/venues/` |
| V-04 | Verifikasi data venue | Kartu venue menampilkan nama venue, rating, kota, cabang olahraga, dan harga `/sesi` |

### Search & Filter
| ID | Scenario | Expected Result |
|----|----------|-----------------|
| V-05 | Klik `Pilih Cabang Olahraga` dan pilih `Padel` | Daftar venue diperbarui sesuai filter cabang olahraga |
| V-06 | Filter `Padel` aktif | Jumlah venue yang ditampilkan berubah; tetap ada minimal 1 venue |
| V-07 | Kombinasi filter lain | Setiap filter cabang olahraga yang tersedia dapat dipilih tanpa error |

### Sort
| ID | Scenario | Expected Result |
|----|----------|-----------------|
| V-08 | Urutkan berdasarkan `Popularitas` | Urutan kartu venue berubah atau tetap konsisten tanpa error |

### Pagination
| ID | Scenario | Expected Result |
|----|----------|-----------------|
| V-09 | Klik nomor halaman pagination (misal `2`) | URL berubah menjadi `/venues?page=2` dan daftar venue diperbarui |
| V-10 | Klik `Next page` | Navigasi ke halaman berikutnya berhasil |
| V-11 | Halaman terakhir | Pagination menampilkan halaman maksimal yang valid |

### FAQ
| ID | Scenario | Expected Result |
|----|----------|-----------------|
| V-12 | Klik pertanyaan FAQ pertama | FAQ membuka/menampilkan jawaban |
| V-13 | Klik kembali pertanyaan FAQ yang sama | FAQ menutup jawaban |
| V-14 | Semua FAQ | Semua pertanyaan FAQ dapat di-expand/collapse tanpa error |

### CTA
| ID | Scenario | Expected Result |
|----|----------|-----------------|
| V-15 | Klik `Daftarkan Venue` | CTA dapat diklik dan mengarahkan ke halaman/form pendaftaran venue |
| V-16 | Klik logo AYO di header | Mengarah kembali ke homepage `ayo.co.id` |

### Responsif & Non-Functional
| ID | Scenario | Expected Result |
|----|----------|-----------------|
| V-17 | Buka `/venues` di viewport mobile (375x812) | Layout menyesuaikan, konten tetap dapat diakses |
| V-18 | Buka `/venues` di viewport desktop (1280x900) | Layout menampilkan daftar venue optimal |
| V-19 | Load time halaman `/venues` | Halaman dapat diakses dalam waktu wajar tanpa error kritis |

## Notes
- Test automation menggunakan Playwright untuk interaksi UISearch, filter, sort, dan pagination dapat diuji dengan locator berbasis teks dan URL pattern.
- Beberapa elemen seperti kontrak harga detail dan ketersediaan slot sebenarnya membutuhkan akses data backend atau halaman detail venue; pada tahap ini fokus pengujian adalah UI listing.
