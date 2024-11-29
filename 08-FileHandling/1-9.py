###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.txt'

# Position
job_title = 'Software Engineer'

counter = 0
with open("it_company.csv", "r") as file:
   for line in file:
      if job_title in line:
        counter += 1
        
print(counter)


#You can check if a string is contained within another string using the 'in' operator