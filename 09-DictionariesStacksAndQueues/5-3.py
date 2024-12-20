translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}
user_input = input("Enter the word you want to translate: ")
if user_input in translations:
        print(translations[user_input])
else:
        print("Your word can not be translated")


       
