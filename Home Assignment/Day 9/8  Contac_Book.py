contacts = {"Aditya" : 8857858968, "Piyush" : 7620007358, "Swapnil" : 7030036662}
print(f"Contacts : {contacts}")

contacts["Tejas"] = 9423575365 
print(f"Contacts after adding a new contact : {contacts}")

contacts["Aditya"] = 9923520356 
print(f"Contacts after updating one contact's number : {contacts}")

del contacts["Piyush"] 
print(f"Contacts after deleting one contact's number : {contacts}")