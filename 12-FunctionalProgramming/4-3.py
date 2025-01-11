grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]
sorted_grades = list(filter(lambda item: item > 2.0, grades))
average = sum(sorted_grades) / len(sorted_grades)
print(average)
