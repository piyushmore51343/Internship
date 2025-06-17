try:
    num = int(input("Enter The Number  "))
    file = input("Enter The file Name")
    c = 100/num

    file_n = open(file,"r")
    

except ZeroDivisionError:
     print("Number cannot divide by 0")
    
except FileNotFoundError:
    print("File Not Found")
else :
    print("Division is ",c)
    print("File Open Successful")
