def detector(code_string):
    people_count = 0
    for sign in code_string:
        if sign == "+":
            people_count +=1
        elif sign == "-":
            people_count -=1
        if people_count >=3:
            break
    result = people_count>=3
    return result

a = detector("+-++-++-+---")
print(a)





#f("+-+++-+---") returns True
#f("+-+-+-+-") returns False
#f("+-++-+--") returns False
#f("+-++-++-+---") returns True
