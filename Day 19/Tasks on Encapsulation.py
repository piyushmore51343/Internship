'''Tasks on Encapsulation
Task: Private Attribute and Method
Instructions:

Create a class Car.

Add a private attribute __speed.

Create a method accelerate(value) to increase the __speed.

Create a method get_speed() to return the current __speed.

Try accessing __speed directly (and understand why it doesn’t work).'''

class Car():
    def __init__(self,speed):
        self.__speed = speed

    def accelerate(self,value):
        self.__speed += value

    def get_speed(self):
        return self.__speed
    
c = Car(120)
c.accelerate(35)
print(c.get_speed())

