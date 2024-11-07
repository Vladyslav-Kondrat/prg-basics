###
# String manipulation
#

from itertools import count


movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print('Title in capital letters: ', movie.upper())
# print title in small letters
print('Title in small letters: ', movie.lower())

# print how many times the vowel "e" appears in the title
e = movie.count("e")
print('Number of times letter "e" appears in the title is ', (e))

# print where in the text is the word "Lord"
x = movie.find("Lord")
print('Word "Lord" is in position' , (x))
# print where in the text is the word "dragon"
y = movie.find("dragon")
