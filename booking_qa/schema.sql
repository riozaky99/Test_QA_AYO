-- bookings table
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY,
    booking_id TEXT,
    venue_id INTEGER,
    user_id INTEGER,
    date TEXT,
    start_time TEXT,
    end_time TEXT,
    price INTEGER
);

-- schedule slots
CREATE TABLE IF NOT EXISTS venue_slots (
    id INTEGER PRIMARY KEY,
    venue_id INTEGER,
    date TEXT,
    start_time TEXT,
    end_time TEXT,
    price INTEGER
);
