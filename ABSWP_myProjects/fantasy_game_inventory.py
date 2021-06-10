stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = {'gold coin': 42, 'rope': 1}

def displayInventory(inventory):
	print('Inventory:')
	item_total = 0
	for k, v in inventory.items():
		print(str(v)+' '+k)
		item_total+=v
	print('Total number od items: '+ str(item_total))

def addToInventory(inventory, addedItems):
	for a in addedItems:
		if a not in inventory.keys():
			inventory[a]=1
		else:
			inventory[a]+=1
	return inventory

displayInventory(inv)
print("\nYou've killed dragon!\n")
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)