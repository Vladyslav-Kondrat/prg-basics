temperatures = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
positive = list(filter(lambda temp: temperatures[temp] > 0, temperatures))
print(positive)