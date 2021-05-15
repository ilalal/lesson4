
"""
Task 1
School
Make a class structure in python representing people at school. Make a base class called Person,
a class called Student, and another one called Teacher. Try to find as many methods and attributes
as you can which belong to different classes, and keep in mind which are common and which are not. For example,
the name should be a Person attribute, while salary should only be available to the teacher.
"""

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def info(self):
        print(f"name: {self.name}\n"
              f"surname: {self.surname}\n"
              f"age : {self.age}")


class Student(Person):
    def __init__(self, name, surname, age, group, specialization):
        super().__init__(name, surname, age)
        self.group = group
        self.specialization = specialization

    def full_info(self):
        self.info()
        print(f"group : {self.group}\n"
              f"specialization : {self.specialization}")


class Teacher(Person):
    def __init__(self, name, surname, age, salary, subject):
        super().__init__(name, surname, age)
        self.salary = salary
        self.subject = subject

    def full_info(self):
        self.info()
        print(f"salary : {self.salary}\n"
              f"subject : {self.subject}")


koval = Student("Vadik", "Koval", "25", "110a", "Plumber")
bob = Teacher("Sanya", "Bob", "30", "5000", "fishing")

koval.info()

bob.info()

koval.full_info()

bob.full_info()

"""Task 2

Mathematician
Implement a class Mathematician which is a helper class for doing math operations on lists
The class doesn't take any attributes and only has methods:
square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive numbers
filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
```
class Mathematician:
    pass
m = Mathematician()
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
"""

class Mathematician:
    def __init__(self):
        pass

    def square_nums(self, some_list):
        self.some_list = some_list
        new_list = [num * num for num in self.some_list]
        return new_list

    def remove_positives(self, some_list):
        self.some_list = some_list
        new_list = [num for num in self.some_list if num < 0]
        return new_list

    def filter_leaps(self, some_list):
        self.some_list = some_list
        new_list = [num for num in self.some_list if num % 4 == 0 and num % 100 != 0 or num % 400 == 0 and num % 4 == 0]
        return new_list


m = Mathematician()
print(m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16])
print(m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90])
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020, 2000, 2400]) == [1884, 2020, 2000, 2400])

"""task4
Create your custom exception named `CustomException`, you can inherit from base Exception class, 
but extend its functionality to log every error message to a file named `logs.txt`. 
Tips: Use __init__ method to extend functionality for saving messages to file
``
class CustomException(Exception):
def __init__(self, msg):
...
```
"""

class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        with open(file="myfile.txt", mode="w") as file:
            file.write(msg)

error = CustomException("OMG WHAT ARE YOU DOING???")
raise error