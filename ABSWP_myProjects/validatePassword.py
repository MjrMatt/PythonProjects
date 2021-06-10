import re

passwords = ['Dobre12%','TorkiDorrki1', 'mikolaj12', 'a7yB3(dq0f@', 'Python', 'Password321', 'I7*bardowski12#']

def validatePasswords(passes):
	valid = []
	invalid = []
	check_long = re.compile(r'[!@#$%^&*\(\)\\/?><,\.;:\'"\{\}\[\]+-_=\w\d]{8,}')
	check_upper = re.compile(r'[A-Z]')
	check_lower = re.compile(r'[a-z]')
	check_number = re.compile(r'\d')
	check_special = re.compile(r'[^a-zA-Z0-9]')
	for p in passes:
		if check_long.search(p) is None : invalid.append((p, 'Too short')) 
		elif check_upper.search(p) is None : invalid.append((p, 'No uppercase'))
		elif check_lower.search(p) is None : invalid.append((p, 'No lowercase'))
		elif check_number.search(p) is None : invalid.append((p, 'No number'))
		elif check_special.search(p) is None : invalid.append((p, 'No special'))
		else : valid.append(p)
	return valid, invalid

print('\nSpośród haseł: ')
for i in passwords:
	print(i,end=' ')

v, n = validatePasswords(passwords)

print('\n\nPoniższe hasła spełniają kryteria: ')
for i in v:
	print(i,end=' ')

print('\n\nPoniższe hasła nie spełaniają kryteriów: ')
for i in n:
	print(i[0]+' - '+i[1]+'!')