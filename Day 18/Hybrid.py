'''Task:
Create a parent class Number.

Create SumNumber and ProductNumber classes that inherit from Number.

Create a final class FinalCalculator that inherits from both.

Call parent methods directly:

SumNumber.sum(self, a, b).

ProductNumber.product(self, a, b).

Test:

FinalCalculator().sum(5, 10) → 15

FinalCalculator().product(3, 4) → 12'''

class Number():
        pass
class SumNumber(Number):
   
    def sum(self ,a,b):
        return a+b
    
class ProductNumber(Number):
    
    def product(self,a,b):
        return a*b

class Finalcalculator(SumNumber,ProductNumber):
    def __init__(self):
         pass
    
print(Finalcalculator().sum(5, 10))
print(Finalcalculator().product(3,4))
