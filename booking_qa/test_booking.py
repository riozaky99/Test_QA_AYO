import sqlite3
import pytest
from datetime import time
from booking_qa.db_setup import get_conn, DB_PATH

def _row_to_dict(row):
    return dict(row)

def expected_price(venue_id, date, start):
    with get_conn() as conn:
        row = conn.execute(
            "SELECT price FROM venue_slots WHERE venue_id=? AND date=? AND start_time=?",
            (venue_id, date, start),
        ).fetchone()
        return row["price"] if row else None

def find_booking(booking_id):
    with get_conn() as conn:
        row = conn.execute("SELECT * FROM bookings WHERE booking_id=?", (booking_id,)).fetchone()
        return _row_to_dict(row) if row else None

def is_double_booking(venue_id, date, start, end, exclude_booking_id=None):
    start_sec = start.hour * 3600 + start.minute * 60
    end_sec = end.hour * 3600 + end.minute * 60
    with get_conn() as conn:
        rows = conn.execute(
            "SELECT * FROM bookings WHERE venue_id=? AND date=? AND booking_id<>?",
            (venue_id, date, exclude_booking_id or ""),
        ).fetchall()
        for b in rows:
            b_start_sec = int(b["start_time"].split(":")[0]) * 3600 + int(b["start_time"].split(":")[1]) * 60 + int(b["start_time"].split(":")[2])
            b_end_sec = int(b["end_time"].split(":")[0]) * 3600 + int(b["end_time"].split(":")[1]) * 60 + int(b["end_time"].split(":")[2])
            if start_sec < b_end_sec and end_sec > b_start_sec:
                return True
        return False

class TestBookingPriceValidation:
    def test_price_should_match_schedule(self):
        b = find_booking("BK/000001")
        assert b is not None
        exp = expected_price(b["venue_id"], b["date"], b["start_time"][:8])
        assert exp is not None, "Slot jadwal tidak ditemukan"
        assert int(b["price"]) == int(exp), f"Harga salah: expected {exp}, got {b['price']}"

    def test_double_booking_detected(self):
        new_start = time(9, 0)
        new_end = time(11, 0)
        assert is_double_booking(15, "2022-12-10", new_start, new_end, exclude_booking_id="BK/000001") is True

    def test_no_double_booking_when_slot_available(self):
        new_start = time(7, 0)
        new_end = time(9, 0)
        assert is_double_booking(15, "2022-12-10", new_start, new_end, exclude_booking_id="BK/000001") is False

    def test_price_invalid_for_slot(self):
        exp = expected_price(15, "2022-12-10", "09:00:00")
        assert exp == 1000000
