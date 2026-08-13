import pytest
from datetime import time, date, datetime, timedelta
from app.exceptions import InvalidCustomerError, InvalidServiceError, InvalidDurationError, InvalidReservationDateError, InvalidReservationTimeError, DuplicateReservationError
from app.validators import validate_customer_name, validate_service, validate_duration, validate_reservation_date, validate_reservation_time, CLOSING_TIME, OPENING_TIME

def test_validate_customer_name_removes_whitespace_and_validates_lenght():
    result = validate_customer_name("  Jhon Beltran  ")
    assert result == "Jhon Beltran"
    
def test_validate_customer_name_rejects_short_names():
    with pytest.raises(InvalidCustomerError, match="Customer name must be at least 3 characters long."):
        validate_customer_name("Jh")

def test_validate_services_removes_whitespace():
    result = validate_service("  SOPORTE  ")
    assert result == "SOPORTE"

def test_validate_not_others_services():
    with pytest.raises (InvalidServiceError):
        validate_service("CAPACITACION")


def test_validate_duration_time_ninety():
    result = validate_duration(90)
    assert result == 90

def test_validate_others_durations():
    with pytest.raises(InvalidDurationError):
        validate_duration(35)


def test_validate_reservation_date_rejects_past_date():
    past_date = date.today() - timedelta(days=1)
    with pytest.raises(InvalidReservationDateError):
        validate_reservation_date(past_date)

def test_validate_reservation_date_rejects_weekend_date():
    today = date.today()
    if today.weekday() >= 6:
     result = InvalidReservationDateError(today)
     assert result == today

def test_validate_reservation_time_accepts_time_within_business_hours():
    result = validate_reservation_time(time(10, 0))
    assert result == time(10, 0)

def test_validate_reservation_time_rejects_time_before_opening():
    with pytest.raises(InvalidReservationTimeError):
        validate_reservation_time(time(8, 0))
