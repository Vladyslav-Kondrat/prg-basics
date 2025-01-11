# class Battery:
#     def __init__(self):
#         self.start_time = None
#         self.end_time = None

#     def start(self):
#         self.start_time - time.time(30)

#     def end(self):
#         self.end_time(0)


class Contact():
    import csv
    def __init__(self, name, number):
        self.name = name
        self.number = number
        




class Phone():
    import csv
    def __init__(self, brand):
        self.battery_level = 100
        self.brand = brand
        self.current_app = None
        # contact_hanna = Contact("Hanna", "4893675018")
        # contact_pablo = Contact("Pablo", "4820255017")
        self.list_of_contacts = []
        with open("1-6_contact-list.csv", "r") as file:
            list_of_contacts_str = file.read().split(",")
            print(f"PRINT TEST {list_of_contacts_str}")
        print(f"File read: {self.list_of_contacts}")            #[contact_hanna, contact_pablo]
        self.apps = [["Music", "Telegram", "Google Maps"],
                ["Notes", "Calls", "Wallet"],
                ["Stopwatch", "Teams", "Gmail"]]

    def call(self):
        if self.current_app == "Telegram" or self.current_app == "Calls":
            print("Who do you want to call to?")
            print()
            print(self.list_of_contacts)
            last_contact_index = len(self.list_of_contacts)-1
            input_contact = int(input(f"Choose from 0 to {last_contact_index}: "))
            choosed_contact = self.list_of_contacts[input_contact]
            print(f"Calling {choosed_contact}...")
        else:
            print("Select an app you can call from")

    def add_contact(self):
        new_name = input("Please, insert name: ")
        new_number = input("Please, insert number: ")
        new_contact = Contact(new_name, new_number)
        #self.list_of_contacts.append(new_contact)
        csv_str = 
        with open("1-6_contact-list.csv", 'a', ) as file:
            file.write(csv_str)
        print(f"New contact with name {new_contact.name} and with number {new_contact.number} has been created.")
        


    def show_list_of_contacts(self):
        print("Your contact list:")
        print()
        for item in self.list_of_contacts:
            print(f"Name: {item.name}, and number: {item.number}")


    def app(self):
        import webbrowser
        link = "https://play.google.com/store/search?q="
        for row in self.apps:
            print(row)
        print()
        choosing = input("What do you want to work with today? ")
        print(choosing)
        found_flag = False
        for row in self.apps:
            for item in row:
                if item == choosing:
                    print(f"'Booting {item}...'")
                    found_flag = True
                    return    #break
            # if found_flag:
            #     break
        if not found_flag:
            print("You do not have this app on your smartphone. Please install it first.")
            download = input(f"Do you want to install {choosing}? Write *Yes* or *No*: ")
            if download == "Yes" or download == "yes":
                search = f"{link}{choosing.replace(" ", "+")}"
                webbrowser.open(search)
            elif download == "No" or download == "no":
                print("Welp, alright then")
            else:
                print("Can you even read what I'm writing you? Just follow the instructions.")
    

def main():
    smartphone = Phone("Redmi Note 11 Pro")
    smartphone.battery_level = "100% maximum"
    smartphone.brand = "Redmi"
    smartphone.current_app =  "Telegram"

    
    smartphone.add_contact()
    smartphone.show_list_of_contacts()
    
    
    #smartphone.call()
    #smartphone.app()
    # smartphone.battery_charge()



if __name__ == "__main__":
    main()


#STATES
#Battery level
#Brand
#Current app running

#BEHAVIOURS
#Make a call
#Open an app
#Charge the phone