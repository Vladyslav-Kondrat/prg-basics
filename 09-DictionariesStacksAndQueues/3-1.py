import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""

# creates a stack
numbers = queue.LifoQueue()

# adds elements to the top of the stack
numbers.put(2)    
numbers.put(3)  
numbers.put(7)
numbers.put(4)
numbers.put(1) 
numbers.put(9) 
numbers.put(8)  
sum =0 
sum+= numbers.get() 
sum+= numbers.get()   
sum_2 = 0
while not numbers.empty():
    sum_2 +=numbers.get()

## prints number of elements of the stack
print('Number of stack elements:', numbers.qsize())


print(sum)
print(sum_2)

# removes and prints elements from the top of the stack
# while not numbers.empty():
#     card = numbers.get()
#     print(card)