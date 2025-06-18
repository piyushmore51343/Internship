
t1 = (10, 20, 30, 40, 50)
print("First Element :", t1[0])
print("Last Element :", t1[-1])
print("Elements from Index 1 to 3 :", t1[1:4])



person = ("Alice", 25, 5.4, "Engineer")
print("\nMixed Data type Tuple :", person)


print("\nAll Elements of Tuple t1 :-")
for i in range(len(t1)):
    print(f"Element {i+1} : {t1[i]}")


t = ("Python",)

'''The comma is necessary when we are going to create a single element tuple.
If we did not give a comma it will declare it as a str data type (in the given example).'''