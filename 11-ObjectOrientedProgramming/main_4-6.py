from bank import Bank

def main():
    my_account = Bank(0, "11 1111 1111 1111 1111 1111 1111")

    my_account.change_the_number()
    my_account.show_status()
    my_account.put_money()
    my_account.show_status()
    my_account.withdraw_money()     #more than there is
    my_account.show_status()
    my_account.withdraw_money()     #enough
    my_account.show_status()


if __name__ == "__main__":
    main()