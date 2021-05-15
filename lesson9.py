
"""TAsk1"""

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.lastname}, and I'm {self.age} years old")


person = Person("Ilia","Zhuravlevych", 30)

person.talk()



"""TAsk2"""

class Dog:
    def __init__(self, dog_age):
        self.age_factor = 7
        self.dog_age = dog_age
        self.human_age1 = self.dog_age * self.age_factor

    def human_age(self):
        print(f"{self.dog_age} years of dog's life is equal to {self.human_age1} years of human's life")


dog = Dog(10)
dog.human_age()