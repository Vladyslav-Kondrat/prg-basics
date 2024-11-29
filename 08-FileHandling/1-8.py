###
# Reads the entire contents of a file
#
def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

# reads the entire file and splits lines into array
file_content = read_from_file('pets.txt')
splited_text = file_content.split()

for i in range(len(splited_text)):
   words= i

print(words)







# total_letters = 0
# for word in splited_text:
#    letters_in_word = len(word)
# total_letters = sum(letters_in_word)
# print(total_letters)