keys = ["name", "age", "city"]

values = ["Sam", 30, "Delhi"]
person = {}
for i in range(len(keys)):
    person[keys[i]] = values[i]
print(person)