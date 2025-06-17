data = [10,20,30]

try:
    index = int(input("Enter The Index Number"))
    val = float(data[index])
    print(val)
except (IndexError , ValueError) as e :
    print(e)
    # print("Index Value cannot found")
    # print("Wrong input")