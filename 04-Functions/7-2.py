def month(n):
    months = [
        None, "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    if 1 <= n <= 12:
        return months[n]
    else:
        return "Invalid month number"

month_name = month(7)

print(f"The name of the month 7 is: {month_name}")