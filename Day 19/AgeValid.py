'''Task: Getters and Setters
Instructions:

Create a class Person.

Add a private attribute __age.

Create:

A method set_age(value) that validates if the age is a positive number.

A method get_age() to return the age.

Try setting both valid and invalid ages.'''

class Person():
    def __init__(self,age):
        self.__age =age
    def set_age(self,value):
        if value > 0:
            self.__age = value
        else:
            print("invalid age")
    def get_age(self):
        return self.__age
    
p = Person(25)
p.set_age(-10)
p.set_age(15)
print(p.get_age())