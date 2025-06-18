try:
    num = int(input("Enter The Number  "))
    file = input("Enter The file Name")
    c = 100/num

    file_n = open(file,"r")
    print(f"Divison is {c}")

except ZeroDivisionError:
     print("Number cannot divide by 0")
    
except FileNotFoundError:
    print("File Not Found")


# except (ZeroDivisionError , FileNotFoundError) :

#     print("Number cannot divide by 100")
#     print("File Not Found")

