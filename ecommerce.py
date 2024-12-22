def calculate_total_price(c):
    if not c:
        return "Cart is empty. Total Price: $0"

    total_price = sum(c.values())
    if len(c) > 5:
        total_price *= 0.9
    return f"Total Price: {int(total_price)}"


cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
print(calculate_total_price(cart_items))