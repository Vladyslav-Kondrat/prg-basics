# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
coloumn_sum = [0, 0, 0]
for coloumn in range (len(monthly_expenses[0])):
    for row in range(len(monthly_expenses)):
        coloumn_sum[coloumn] += monthly_expenses[row][coloumn]


week_sum = [0, 0, 0, 0]
for row in range(len(monthly_expenses)):
    week_sum[row] = sum(monthly_expenses[row])

total_sum = sum(week_sum)
# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', {coloumn_sum[0]})
print('Transport:', {coloumn_sum[1]})
print('Utilities:', {coloumn_sum[2]})
# print('Week 1:', {week_sum[0]})
# print('Week 2:', {week_sum[1]})
# print('Week 3:', {week_sum[2]})
# print('Week 4:', {week_sum[3]})
# print('---------------')
# print('TOTAL:', {total_sum} )
for i in range[0, len(week_sum)-1]:
  print("week", {i+1},":",{week_sum[i]})