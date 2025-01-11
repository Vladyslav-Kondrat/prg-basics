class Bank:
    def __init__(self, total_money, initial_number):
        self.total_money = total_money
        self.initial_number = initial_number

    
    def change_the_number(self):
        self.initial_number = "12 3456 5555 9090 1111 0000 7722"

    def put_money(self):
        money = int(input("How much do you want to put on your account?: "))
        self.total_money += money
        print(f"Your account now has {self.total_money} PLN")

    def withdraw_money(self):
        money2 = int(input("How much do you want to withdraw from your account?: "))
        if self.total_money >= money2:
            self.total_money -= money2
            print(f"Your account now has {self.total_money} PLN")
        else:
            print("Not enough money on the account")

    def show_status(self):
        print(f"You have {self.total_money} PLN on your account")