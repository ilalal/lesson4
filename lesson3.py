import random
#TASK 1
frase = "helloworld"
if len(frase) == 10:
    print(frase[0:2] + frase[-2:])
elif len(frase) < 2:
    print("")

frase01 = input("Type \"helloworld\": ")
if len(frase01) < 2:
    print("try again champ")
else:
    print(frase01[0:2] + frase01[-2:])

frase2 = "my"
if len(frase2) <= 2:
    print("mymy")

frase3 = "x"
if frase3:
    print("Empty String")


#TASK 2

nomer = input("i need your phone number pls: ")
while not (len(nomer) == 10 and nomer.isdigit()):
    print("Pay atention! Try again")
    nomer = input("i need your phone number pls: ")
else:
    print("well done!")


#TASK 3

x = "Illia"
y = input("what is your name").lower()
if x == y:
    print(x == y)







