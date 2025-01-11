def avg_speed(distance,hours,minutes):
    total_hours = hours + minutes / 60
    avarage_speed = distance / total_hours
    return avarage_speed



distance = int(input("Enter the distance in km: "))
hours = int(input("Enter the amount of hours traveled: "))
minutes = int(input("Enter the amount of minutes traveled: "))

print(avg_speed(distance, hours, minutes))