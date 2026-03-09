def calculate_total(cart: list[dict], discount_code: str = "") -> float:
    if not isinstance(cart, list):
        raise TypeError("Cart must be a list of dictionaries")
    for item in cart:
        if not isinstance(item, dict):
            raise TypeError("Each item in the cart must be a dictionary")
        if "price" in item and not isinstance(item["price"], (int, float)):
            raise TypeError("Price must be a number")
        if "quantity" in item and not isinstance(item["quantity"], int):
            raise TypeError("Quantity must be an integer")
        if "price" not in item:
            raise ValueError("Each item must have a price")
        if "quantity" not in item:
            raise ValueError("Each item must have a quantity")
        
    total = sum(item.get("price", 0) * item.get("quantity", 1) for item in cart)
    
    if total <= 0:
        return 0.0
        
    if discount_code == "SAVE10":
        total *= 0.90
    elif discount_code == "SAVE20" and total >= 1000:
        total *= 0.80
        
    return round(total, 2)