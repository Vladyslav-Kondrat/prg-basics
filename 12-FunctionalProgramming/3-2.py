sentence = "I completely agree with you"
splited = sentence.split(" ")
result = list(map(lambda x: len(x), splited))
print(result)