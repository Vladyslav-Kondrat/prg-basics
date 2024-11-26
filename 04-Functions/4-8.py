def time_string(hours, minutes, time_format):
    if time_format == 24:
        print(f"{hours}:{minutes}")
    elif time_format == 12:
        if hours < 12:
            print(f"{hours}:{minutes}am")
        elif hours == 12:
            print(f"{hours}:{minutes}pm")
        else:
            print(f"{hours-12}:{minutes}pm")
    else:
        print("Error")

time_string(15, 42, 24)
h = int(input("Enter hours: "))
m = int(input("Enter minutes: "))
t_f = int(input("Enter time format: "))
time_string(h, m, t_f)





