class My_Statistica:
    def __init__(self):
        self.array = []

    def add_number(self):
        flag = True
        while flag:
            self.array.append(int(input("Print the number you want to add: ")))
            yes_no = int(input("Do you want to add another number? 1 for yes, 0 for no: "))
            if yes_no == 0:
                flag = False


    def display_array(self):
        print(self.array)

    def maximum_value(self):
        maximum = max(self.array)
        print(maximum)

    def minimum_value(self):
        minimum = min(self.array)
        print(minimum)

    def arithmetic_mean(self):
        sum_all = 0
        for item in self.array:
            sum_all += item
        ar_mean = sum_all / len(self.array)
        print(f"The arithmetic mean of all values is: {ar_mean}")

    def median(self):
        mediana = (len(self.array) + 1) / 2
        print(f"The median of all values is: {mediana}")


    # def all_quantities(self):
    #     print("")