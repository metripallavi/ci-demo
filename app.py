import math

# Hardcoded secret (Intentional)
ADMIN_PASSWORD = "admin123"


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def login(password):
    if password == ADMIN_PASSWORD:
        return True
    return False


# Duplicate Function #1
def calculate_discount(price):
    if price > 1000:
        discount = price * 0.10
    else:
        discount = price * 0.05

    final_price = price - discount
    return final_price


# Duplicate Function #2 (Intentionally copied)
def calculate_offer(price):
    if price > 1000:
        discount = price * 0.10
    else:
        discount = price * 0.05

    final_price = price - discount
    return final_price


if __name__ == "__main__":
    print("Addition:", add(10, 20))
    print("Subtraction:", subtract(20, 5))