import pyinputplus as pyip
anotherorder = 'yes'
total = 0
orders = []
print("Hello, Sir/Madam. I'll prepare your sandwich(es)!\n")
while anotherorder == 'yes':
	breadPrices = {'wheat':2, 'white':1, 'sourdough':2.5}
	proteinPrices = {'chicken':5, 'turkey':4.5, 'ham':3.5, 'tofu': 6}
	cheesePrices = {'cheddar':1, 'Swiss':2, 'mozzarella':0.5, 'no':0}
	bread = pyip.inputMenu(list(breadPrices.keys()), numbered=True)
	protein = pyip.inputMenu(list(proteinPrices.keys()), numbered=True)
	cheese = pyip.inputYesNo('Do you want me to add cheese to your sandwich?')
	if cheese == 'yes':
		cheese = pyip.inputMenu(list(cheesePrices.keys())[:-1], numbered=True)
	quantity = pyip.inputInt('How many sandwiches with these parameters you need?', min=1)
	anotherorder = pyip.inputYesNo('Do you want to order any other sandwich?')
	print(anotherorder)
	price = breadPrices[bread]+proteinPrices[protein]+cheesePrices[cheese]
	orders.append((quantity, bread, protein, cheese, price))
	total += quantity*price
print('\nThank You, Sir/Madam! Your order is:')
for o in orders:
	print(f'{o[4]*o[0]} PLN for {o[0]} x sandwich on {o[1]} bread with {o[2]} protein with {o[3]} cheese, {o[4]} PLN each ')
print(f'That\'ll be {total} PLN in total.')