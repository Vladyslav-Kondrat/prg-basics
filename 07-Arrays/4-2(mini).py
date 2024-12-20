arr1 = [3,7,1,0,4]#
arr2 = [[2,3],[7,1],[0,4]]#
arr3 = [7 for i in range(5)]#
arr4 = [i for i in range(1,10)]#
arr5 = [i*2 for i in range(1,10)]

import random
arr6 = [random.randint(1,20) for i in range(10)]
arr7 = [[10, 20, 30] for i in range(5)]
arr8 = [[2 for i in range(2)] for j in range(4)]
arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
arr10 = [4, 0 , 3]  #an array with values: 4,0,3
arr11 = [0 for i in range (15)] #15-element array filled with zeros
arr12 = [i for i in range (1, 31)]# an array with integer values in the range of <1,30>
arr13 = [random.randint(0, 1) for i in range(20)]# 20-element array filled with 0 or 1 randomly

#arr14 = [False for i in range(1, 3)]
#def arr14(x, y, value):
    #return [[value for i in range(x)] for j in range (y)]
matrix = [[0]*2 for g in range(5)]
for row in range(5):
    for item in range(2):
        matrix[row][item] = False
        
        
print(matrix)

            
# two dimensional array with five rows and two columns filled with False


# print(arr1)
# print(arr2)
# print(arr3)
# print(arr4)
# print(arr5)
# print(arr6)
# print(arr7)
# print(arr8)
# print(arr9)
# print(arr10)
# print(arr11)
# print(arr12)
# print(arr13)
# for row in arr14(2, 5, False):
#     print(row)