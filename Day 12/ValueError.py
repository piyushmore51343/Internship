try :
    a = int(input("Enter The Number  "))
    print(a)
except ValueError:
    print("Cannot Convert str to int")

except TypeError:
    print("Type Error Occured")   
    