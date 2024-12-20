# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.id = "00 00 00"
def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.id = "09 87 32"
    student2.name = "Olivia"
    student2.age = 21
    student2.id = "67 05 81"

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, ID is: {student1.id}')
    print(f'{student2.name}, {student2.age} years old, ID is: {student2.id}')

if __name__ == "__main__":
    main()