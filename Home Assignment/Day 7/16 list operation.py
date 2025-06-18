list1 = []
for i in range(5):
    list1.append(int(input(f"Enter Number {i+1}: ")))

sum = 0
for i in range(len(list1)):
    sum += list1[i]
print("\nSum =",sum)

max = 0
for i in range(len(list1)):
    if list1[i] > max:
        max = list1[i]
print("Max =", max)

min = list1[i]
for i in range(len(list1)):
    if list1[i] < min:
        min = list1[i]
print("Min =", min)
list1.sort()
print("Sorted List :", list1 )