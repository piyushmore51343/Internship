a = int(input("Enter The First Number : "))
b = int(input("Enter The Second Number : "))

try :
    c = a / b
    print(f"Divison is {c}")
except ZeroDivisionError:
    print("Not Divisible By Zero")