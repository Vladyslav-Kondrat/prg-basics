medals = [
    {"country":"Denmark","gold":2,"silver":4,"bronze":6},
    {"country":"Finland","gold":5,"silver":0,"bronze":4},
    {"country":"USA","gold":12,"silver":5,"bronze":11},
    {"country":"Peru","gold":0,"silver":1,"bronze":7}
]

number = list(filter(lambda dict: dict["gold"] + dict["silver"] + dict["bronze"] > 10, medals))
#print(number)
for country2 in number:
    total_medals = f"{country2["country"]}: {country2["gold"]}, {country2["silver"]}, {country2["bronze"]}"
    print(total_medals)












#dict["gold"] + dict["silver"] + dict["bronze"]
#sum(dict["gold"], dict["silver"], dict["bronze"])