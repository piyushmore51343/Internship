
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union of a and b: ", a.union(b)) 
print("Intersection of a and b: ", a.intersection(b))
print("Difference of a and b: ", (a-b))
print("Difference od b anda: ", (b-a))

demo_set = {10, 20, 30, 40, 50, 60, 70}
print("\nSet before removing a element :", demo_set)
demo_set.remove(20)
demo_set.discard(50)
print("Set after removing a element :", demo_set)

demo_set.discard(20) 