#!/bin/bash
set -e
cd "$(dirname "$0")/booking_qa"
[ -f test.db ] || python3.11 -m booking_qa.db_setup
python3.11 -m pytest booking_qa/test_booking.py -v
