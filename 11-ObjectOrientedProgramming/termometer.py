class Termometer:
    def __init__(self, brand):
        self.is_on = False
        self.brand = brand


    def termometer_on(self):
        self.is_on = True


    def termometer_off(self):
        self.is_on = False


    def degree_meter(self):
        import random
        if self.is_on == True:
            temperature = random.uniform(34, 42)  #randint
            if temperature >= 41:
                print(f"Your temperature is {temperature}, and above 41 degrees. Critical condition!")
            elif temperature >= 37:
                print(f"Your temperature is {temperature}, and above 37 degrees. Fever.")
            else:
                print(f"Your temperature is {temperature} degrees.")
        else:
            print("Turn your termometer on first")