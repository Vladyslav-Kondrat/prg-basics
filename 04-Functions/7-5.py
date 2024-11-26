def hide():
    masked_card = card_number[:2] + '*' * 10 + card_number[-4:]
    return masked_card


card_number = "1234567812345678"
masked_number = hide()
print(f"Masked credit card number: {masked_number}")