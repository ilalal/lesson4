
"""
Task 1
Write a Python program to get the largest number from a list of random numbers with the length of 10
Constraints: use only while loop and random module to generate numbers
"""

import random

num = [random.randint(0, 10)]
i = 0
while True:
    print(max(num))
    break


"""
Task 2
Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing
the common integers between the 2 initial lists without any duplicates.
Constraints: use only while loop and random module to generate numbers
"""
import random

list1 = (random.randint(1, 10))
list2 = (random.randint(1, 10))
i = 0
while i < 10:
    list3 = random.randint(list1 , list2)
    print(list3)
    i += 1


"""
Task3
Make a list that contains all integers from 1 to 100, then find all integers from the list that are 
divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.
Constraint: use only while loop for iteration 
"""

list100 = []
for x in range(0, 100):
    if (x%7==0) and (x%5!=0):
        list100.append(str(x))
        result = (",".join(list100))
        result = list100
print(result)




