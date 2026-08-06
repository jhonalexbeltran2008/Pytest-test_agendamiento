import pytest
from datetime import time, date, datetime
from app.exceptions import InvalidCustomerError, InvalidServiceError, InvalidDurationError, InvalidReservationDateError, InvalidReservationTimeError, DuplicateReservationError
from app.validators import validate_customer_name, validate_service, validate_duration, validate_reservation_date, validate_reservation_time

def text_validate_customer_name_removes_whitespace_and_validates_lenght():
    result = validate_customer_name("  Jhon Beltran  ")
    assert result == "Jhon Beltran"
    
def test_validate_customer_name_rejects_short_names():
    with pytest.raises(InvalidCustomerError, match="Customer name must be at least 3 characters long."):
        validate_customer_name("Jh")

def text_validate_services_removes_whitespace():
    result = validate_service("  SOPORTE  ")
    assert result == "SOPORTE"
    