###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:

    # add one to the character's code
    shift = ord(char) + 1
    # replace new character code with its
    # corresponding character (use chr())
    replace = chr(shift)
    # add encrypted character to encrypted text
    encrypted_text += replace

print(f"The sentence before incoding is: {plain_text}")
print(f"The sentence after incoding is: {encrypted_text}")