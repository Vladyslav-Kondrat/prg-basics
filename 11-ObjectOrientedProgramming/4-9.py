class Employee:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority


    def data(self):
        self.name = input("Enter the name: ")
        self.surname = input("Enter the surname: ")
        self.age = int(input("Enter the age: "))
        self.seniority = input("Enter the year worked: ")


    def initials(self):
        initials_string = ""
        initials_string += self.surname
        initials_string += self.name[0]
        initials_string += self.seniority
        if self.age < 18:
            print(str.lower(initials_string))
        elif self.age >= 18:
            print(str.upper(initials_string))




def main():
    employee = Employee("", "", 0, 0)

    employee.data()
    employee.initials()

if __name__ == "__main__":
    main()

