lock = False
try:
    lock = True
    div = 10/0
except ZeroDivisionError as e:
    print("Cannot divide by zero")
finally:
    lock = False
    print("Lock released")