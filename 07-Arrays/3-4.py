# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]

# Returns a week day name
def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]

# Returns a string with day meal names
# separated by comma
def day_meal_plan(meal_plan, day_number):
   day_name = weekday(day_number)
   day_meals_array = meal_plan[day_number-1]
   delimeter = ", "
   day_meal_str = delimeter.join(day_meals_array)
   result = str(day_name) + ": " + day_meal_str
   return result
   #return str(weekday(day_number)) + " : " + ", ".join(meal_plan[day_number-1])   

for day_number in range(1, 8):
   print(day_meal_plan(meal_plan, day_number))

    


        

# Prints weekly meal plan
