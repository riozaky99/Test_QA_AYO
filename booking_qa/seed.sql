DELETE FROM bookings;
DELETE FROM venue_slots;

INSERT INTO bookings (id, booking_id, venue_id, user_id, date, start_time, end_time, price)
VALUES
  (1001, 'BK/000001', 15, 12, '2022-12-10', '09:00:00', '11:00:00', 1200000),
  (1005, 'BK/000005', 15, 12, '2022-12-10', '09:00:00', '11:00:00', 1000000);

INSERT INTO venue_slots (id, venue_id, date, start_time, end_time, price)
VALUES
  (11, 15, '2022-12-10', '07:00:00', '09:00:00', 800000),
  (12, 15, '2022-12-10', '09:00:00', '11:00:00', 1000000),
  (13, 15, '2022-12-10', '11:00:00', '13:00:00', 1200000);
