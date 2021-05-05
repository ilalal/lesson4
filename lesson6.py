"""Task1
Make a program that has some sentence (a string) on input and
returns a dict containing all unique words as keys and the number of occurrences as values.
"""

the_string = "This is the string , the string , unique words , words in the string"
the_dict = {word: the_string.count(word) for word in the_string.split()}

print(the_dict)





"""Task2
Create a function which takes as input two dicts with structure mentioned above, then computes
and returns the total price of stock.
"""

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def total_price(dict1, dict2):
    x = 0
    for value in dict1 and dict2:
        x += dict1[value] * dict2[value]
    print(x)


total_price(stock, prices)


"""Task 3
List comprehension exercise
Use a list comprehension to make a list containing tuples (i, j) 
where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.
"""
i = tuple(range(1, 11))
j = tuple(item * item for item in i)
my_list = [i, j]
print(my_list)