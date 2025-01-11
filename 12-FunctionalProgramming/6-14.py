all_bottles = [508,500,512,499,492,511,503,476,501,509]
nominal = 500
tolerance = 0.02
minimum_tolerance = nominal * (1-tolerance)
maximum_tolerance = nominal * (1+tolerance)
incorrectly_filled = list(filter(lambda bottle: bottle < minimum_tolerance or bottle > maximum_tolerance, all_bottles))
persentage = (len(incorrectly_filled) / len(all_bottles)) * 100
print(persentage)