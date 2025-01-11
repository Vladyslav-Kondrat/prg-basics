names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']

sort = sorted(names, key = lambda item: len(item))
print(sort)