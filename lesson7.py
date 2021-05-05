
"""
Task 1
Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
The function should then print “My favorite movie is named {name}”.
"""


def favorite_movie(*name):
    for names in name:
        print(f"My favorite movie is named : {names} ")
favorite_movie("Oldboy", "borat")



def favorite_mov(film="LOTR"):
    print("My favorite movie is named " + film)
favorite_mov()
favorite_mov("Matrix")


"""Task 2
Creating a dictionary.
Create a function called make_country, which takes in a country’s name and capital as parameters. 
Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
Make the function print out the values of the dictionary to make sure that it works as intended.
"""

def make_country(country_name, capitals):
    country = {"country_name": country_name, "capitals": capitals}
    return country

Great_Britain = make_country("Great Britain", "London")
print(Great_Britain)



def make_countri(country_name, capitals):
    country = {"country_name": country_name, "capitals": capitals}
    return country

Great_Britain = make_countri("Great Britain", "London")
print(Great_Britain["country_name"])
print(Great_Britain["capitals"])

"""Task 3
A simple calculator.

Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter 
(to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) 
as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:

the call make_operation(‘+’, 7, 7, 2) should return 16
the call make_operation(‘-’, 5, 5, -10, -20) should return 30
the call make_operation(‘*’, 7, 6) should return 42  
"""

def make_operation(symbol, *args):
    x = 0
    if symbol == "+":
        for numbers in args:
            x += numbers
    elif symbol == "-":
        for numbers in args:
            x -= numbers
    elif symbol == "*":
        x = 1
        for numbers in args:
            x *= numbers
    return print(x)

make_operation("+", 7, 7, 2)
make_operation("-", 5, 5, -10, -20, )
make_operation("*", 6, 7)