from contact import Contact
class Contact_List:
    def __init__(self):
        self.contact_list = []
        
        
    def adding_contact(self):
        self.name = input("Plase insert the name: ")
        self.email = input("Please insert the email: ")
        self.telephone = int(input("Plase insert the phone number: "))
        self.contact_list.append(self.name)
        self.contact_list.append(self.email)
        self.contact_list.append(self.telephone)
        print(self.contact_list)
            

