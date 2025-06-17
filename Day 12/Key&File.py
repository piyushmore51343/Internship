prices = {"apple":10 , "banana":5}
try:
    fruit = input("Enter The Fruit Name  ")
    file = input("Enter The Name of File  ")

    print(f"The name of Fruit is {fruit} and price is {prices[fruit]}")
    with open(file,"r")  :
        file.read()     
except KeyError as e:
    print("Invalid Key : ", e)
except FileNotFoundError :
    print("File Does Not exists ")