import queue

def division(number):
    binary_numbers = queue.LifoQueue()
    while number > 0:
        division_result = number % 2
        binary_numbers.put(division_result)
        number = number // 2
        
    while not binary_numbers.empty():
        item = binary_numbers.get()
        print(item, end = "")    


    # count = 0
    # while not binary_numbers.empty():
    #     binary_numbers.get()
    #     count += 1
    # print(count)

division(18)