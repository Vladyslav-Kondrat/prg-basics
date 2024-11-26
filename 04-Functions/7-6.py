def binary_number(code):
    code = str(code)
    for char in code:
        if char == "0" or char == str(1):
            continue
        else:
            return False
    return True
print(binary_number("100100010001sinvuksuhvosj11100101 ,101"))