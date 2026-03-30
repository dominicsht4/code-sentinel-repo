
# Missing test coverage — no tests exist for this module
def calculate_discount(price, discount_percent):
    if discount_percent > 100:
        discount_percent = 100
    return price * (1 - discount_percent / 100)

def format_currency(amount, currency="USD"):
    return f"{currency} {amount:.2f}"
