###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = True # False - switch off, True - switch on
light_switch2 = False
bulbs_on = 0
if light_switch1 or light_switch2:
    bulbs_on += 1
if light_switch2 and light_switch1:
    bulbs_on += 3
print(f"Bulbs are lit: {bulbs_on}")