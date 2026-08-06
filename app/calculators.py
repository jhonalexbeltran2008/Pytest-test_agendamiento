def calculate_subtotal(unit_price: float, quantity: int) -> float:
    if unit_price < 0:
        raise ValueError("Unit price cannot be negative.")
    if quantity <= 0:
        raise ValueError("Quantity cannot be zero or negative.")
    return unit_price * quantity

def calculate_discount(subtotal: float, discount_percentage: float) -> float:
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative.")
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100.")
    
    return subtotal * (discount_percentage / 100)

def  calculate_total(unit_price: float, quantity: int, discount_percentage: float = 0) -> float:
    subtotal = calculate_subtotal(unit_price, quantity)
    discount = calculate_discount(subtotal, discount_percentage)
    return subtotal - discount



def test_calculate_discount_accepts_zero_porcent():
    pass


def test_calculate_discount_accepts_one_hundred_percent():
    pass

def test_calculate_discount_rejects_percemntaje():
    pass