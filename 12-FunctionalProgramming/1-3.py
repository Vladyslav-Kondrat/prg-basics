def ms_to_kmh(ms):
    return ms * 3.6


speed = 35
km_per_hour = ms_to_kmh(speed)
print(f"{speed}m/s = {km_per_hour}km/h")