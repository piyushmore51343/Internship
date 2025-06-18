inventory = {"pen" : 500, "notebook" : 270, "eraser" : 100}

def update_stock(item, quantity):
    inventory[item] = quantity
    return inventory

print("Updating Stock: ", update_stock("pencil", 150))
print("Updating Stock: ", update_stock("eraser", 150))
print("Current Inventory: ", inventory)
