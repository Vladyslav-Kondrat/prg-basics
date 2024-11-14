###
# Sums numbers entered by user
#
total_sum = 0
entry_count = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    entry_count += 1


arithm_mean = total_sum / entry_count

print(f"The total sum of the numbers is: {total_sum}")
print(f"And a arithmetic mean of those numbers is: {arithm_mean}")