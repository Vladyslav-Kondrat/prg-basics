age = int(input("Enter your age: "))

if 0 <= age <=13:
    age_group = ("Child")
elif 14 <= age <= 19:
    age_group = ("Teen")
elif 20 <= age <= 64:
    age_group = ("Adult")
elif age > 64:
    age_group = ("Senior")

print(age_group)