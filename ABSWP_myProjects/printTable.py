tableData = [['apples', 'oranges', 'cherries', 'banana'],
			 ['Alice', 'Bob', 'Carol', 'David'],
			 ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
	colWidth = [len(max(t, key=len)) for t in table]
	print('\n'+' your table '.upper().center(sum(colWidth)+len(colWidth)-1, '='))
	for i in range(len(table[0])): #0,1,2,3
		for j in range(len(table)): #0,1,2
			print(table[j][i].rjust(colWidth[j]), end=' ')
		print('')
	print(''.center(sum(colWidth)+len(colWidth)-1, '='))

printTable(tableData)