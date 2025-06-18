numbers = [1, 2, 2, 3, 4, 4, 5]
print(f"\nOriginal List: {numbers}")
num_set = set(numbers) 
print(f"Removed Duplicates (list converted into set): {num_set}") 

print("All items of set :",end = " ")
for i in num_set:
    print(i,end = " ")