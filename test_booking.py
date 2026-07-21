"""
Automation Test: Booking Price Validation + Double Booking Detection
Dependency: pytest
Run: pytest test_booking.py -v
"""

from datetime import datetime


# ================= DATA =================

SCHEDULE = {
    ("2022-12-10", "09:00:00", "11:00:00"): 1000000,
    ("2022-12-10", "11:00:00", "13:00:00"): 1200000,
}

BOOKINGS = [
    {"id": 1001, "booking_id": "BK/000001", "venue_id": 15, "user_id": 12, "date": "2022-12-10", "start": "09:00:00", "end": "11:00:00", "price": 1200000},
    {"id": 1005, "booking_id": "BK/000005", "venue_id": 15, "user_id": 12, "date": "2022-12-10", "start": "09:00:00", "end": "11:00:00", "price": 1000000},
]


# ================= HELPERS =================

def time_to_seconds(t: str) -> int:
    return datetime.strptime(t, "%H:%M:%S").hour * 3600 + datetime.strptime(t, "%H:%M:%S").minute * 60


def overlaps(start1, end1, start2, end2) -> bool:
    return time_to_seconds(start1) < time_to_seconds(end2) and time_to_seconds(start2) < time_to_seconds(end1)


def find_slot_schedule(date, start, end):
    for (d, s, e), price in SCHEDULE.items():
        if d == date and s == start and e == end:
            return price
    return None


# ================= PYTEST TEST CASES =================

def test_booking_price_matches_schedule():
    """TC-001 & TC-002: Harga booking harus sama dengan harga slot jadwal."""
    for b in BOOKINGS:
        expected = find_slot_schedule(b["date"], b["start"], b["end"])
        assert expected is not None, f"Slot tidak ditemukan untuk booking {b['booking_id']}"
        assert b["price"] == expected, (
            f"{b['booking_id']} harga salah: expected {expected}, got {b['price']}"
        )


def test_double_booking_detected():
    """TC-003 & TC-007: Dua booking di venue/date/waktu yang sama harus terdeteksi."""
    conflicts = []
    for i in range(len(BOOKINGS)):
        for j in range(i + 1, len(BOOKINGS)):
            a, b = BOOKINGS[i], BOOKINGS[j]
            if (a["venue_id"] == b["venue_id"] and a["date"] == b["date"] and
                    overlaps(a["start"], a["end"], b["start"], b["end"])):
                conflicts.append((a["booking_id"], b["booking_id"]))
    assert len(conflicts) > 0, "Double booking tidak terdeteksi!"
    print(f"Double booking terdeteksi: {conflicts}")


def test_non_overlapping_booking_accepted():
    """TC-004: Booking yang tidak overlap harus valid."""
    a = BOOKINGS[0]
    b = {"start": "12:00:00", "end": "13:00:00", "date": a["date"]}
    assert not overlaps(a["start"], a["end"], b["start"], b["end"]), "Seharusnya tidak overlap"


def test_slot_not_found_rejected():
    """TC-005: Booking di slot yang tidak ada harus ditolak."""
    result = find_slot_schedule("2022-12-10", "13:00:00", "14:00:00")
    assert result is None, "Slot tidak valid harus ditolak oleh sistem"


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
