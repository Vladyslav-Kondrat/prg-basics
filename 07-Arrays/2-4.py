###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[-1])
print('Last but one value', arr[len(arr)-2])
print('Sum of first and last values', arr[0] + arr[-1])
print('The middle value of an array', arr[len(arr)//2])
print('The middle value of an array', arr[int(len(arr)/2)])
print('All array values separated by a single space:')
for item in arr:
    print(item, end=' ')