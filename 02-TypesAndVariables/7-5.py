###
# Vehicle registration numbers in Krakow start
# with the letters KR or KK. Write a program that checks
# whether the vehicle registration number entered
# from the keyboard means a vehicle from Krakow.
# Print True whether a car is from Krakow or False otherwise.
#

#Constants
krakow_identifier1 = "kk"
krakow_identifier2 = "kr"

car_number = input('Enter car registration number: ')
city_id = car_number[0:2]
is_krakow = (city_id == krakow_identifier1 or city_id == krakow_identifier2)
print(f'Car with city identifier {city_id} is from Krakow: {is_krakow}')