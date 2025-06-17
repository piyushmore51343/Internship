a = int (input("Enter a number: "))
b = int(input("Enter The Second Number"))

try :
    c = a / b
    print(f"Divison is {c}")
except ZeroDivisionError:
    print("Not Divisible By Zero")