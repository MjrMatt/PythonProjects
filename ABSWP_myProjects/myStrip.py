import re
text= "    To trzeba-przyciąć!    "
text2= r'%%%%%%%To-także należy przyciąć!%%%%%%%%'

def myStrip(text, char=' '):
	if char ==' ':
		regex = re.compile(r'^\s*([\S\s]+?)\s*$')
	else :
		regex =  re.compile(r'^['+char+r']*([\S\s]+?)['+char+r']*$')
	stripped = regex.search(text)
	return stripped.group(1)

print("T       : "+text)
print("strip(T): "+myStrip(text))
print('\n\n')
print("T       : "+text2)
print("strip(T): "+myStrip(text2, '%'))