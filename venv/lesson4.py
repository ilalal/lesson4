import random
#chess
line = 1
while line < 23:
    print("b ch " * 4)
    line += 7
    while line < 8:
        print("KKK" * 4)
        line += 1
    else:
        print("ch b " * 4)

#Task 1
#Write a program that generates a random number between 1 and 10 and
#lets the user guess what number was generated. The result should be sent back to the user via a print statement.

print("play game?")
chosen_number = random.randint(1, 10)

while True:
    your_chose = int(input( "guess number: "))
    if chosen_number == your_chose:
        print(f"You win. yor number is {chosen_number}")
        break
    if chosen_number > your_chose:
        print("The int is bigger ")
    else:
        print("The int is smaller")

#task2
#Write a program that takes your name as input, and then your age as input and greets you with the following:
#“Hello <name>, on your next birthday you’ll be <age+1> years”

name = input("Yor name: ")
age = int(input("Your age: "))
while True:
    print(f"Hello {name}, on your next birthday you’ll be {age + 1} years")
    break

#task3
#Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.

#For example, the program obtained the word
#hello’, so it should print 5 random strings(words) that combine characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …

#Tips: Use random module to get random char from string)

import random
generator = (input("Type your string : "))
print("".join(random.sample(generator, len(generator))))
print("".join(random.sample(generator, len(generator))))
print("".join(random.sample(generator, len(generator))))
print("".join(random.sample(generator, len(generator))))
print("".join(random.sample(generator, len(generator))))

#task4
# Write a program that asks the answer for a mathematical expression, checks
# whether the user is right or wrong, and then responds with a message accordingly.

result = int(input("5 + 5 = "))
if result == 5 + 5:
    print("You are correct")
else:
    print("You are wrong!")



