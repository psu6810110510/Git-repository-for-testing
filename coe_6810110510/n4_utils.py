def calculate_total(cart: list[dict], discount_code: str = "") -> float:
    total = sum(item.get("price", 0) * item.get("quantity", 1) for item in cart)
    
    if total <= 0:
        return 0.0
        
    if discount_code == "SAVE10":
        total *= 0.90
    elif discount_code == "SAVE20" and total >= 1000:
        total *= 0.80
        
    return round(total, 2)