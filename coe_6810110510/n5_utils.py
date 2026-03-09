def calculate_taxi_fare(distance_km: float, wait_time_min: int) -> int:
    if distance_km < 0 or wait_time_min < 0:
        raise ValueError("Distance and wait time cannot be negative")
    
    base_fare = 35
    distance_fare = 0
    
    if distance_km > 1:
        if distance_km <= 10:
            distance_fare = (distance_km - 1) * 6
        else:
            distance_fare = (9 * 6) + ((distance_km - 10) * 10)
            
    wait_fare = wait_time_min * 2
    
    total_fare = base_fare + distance_fare + wait_fare
    return int(total_fare)