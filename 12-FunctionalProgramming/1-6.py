distance = int(input("Enter the distance in km: "))
hours = int(input("Enter the amount of hours traveled: "))
minutes = int(input("Enter the amount of minutes traveled: "))

total_hours = hours + minutes / 60

print((lambda x, y: x / y)(distance, total_hours))