#test boards
board0 = {'1a': 'bking'}

#valid boards
board1 = {'1h': 'bking', '6c' : 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking' }

#not valid boards
board2 = {'1h': 'wking', '1z': 'bking'}
board3 = {'1h': 'wking', '8h': 'wking'}

pieces = {'king': 1, 'queen': 1, 'bishop': 2, 'rook': 2, 'knight': 2, 'pawn': 8}

def generateSpaces():
	spaces = []
	alpha = "abcdefgh"
	for num in range(1,9):
		for a in alpha:
			spaces.append(str(num)+a)
	return spaces

def colorPieces(color):
	cpieces = {}
	for k in pieces.keys():
		cpieces[color+k] = pieces[k]
	return cpieces

def isValidChessBoard(board):
	spaces = generateSpaces()
	allowedPieces = pieces.keys()
	whitePieces = colorPieces('w')
	blackPieces = colorPieces('b')

	for bkey in board.keys():
		if bkey not in spaces:
			return False #wrong spaces on board
		color = board[bkey][0]
		piece = board[bkey][1:]
		if piece not in allowedPieces:
			return False #wrong piece name
		if color == 'b':
			blackPieces[color+piece]-=1
		elif color == 'w':
			whitePieces[color+piece]-=1
		else:
			return False #wrong color
	for key in whitePieces.keys():
		if whitePieces[key]<0:
			return False #invalid number of white pieces
	for key in blackPieces.keys():
		if blackPieces[key]<0:
			return False #invalid number of black pieces

	return True

print(isValidChessBoard(board0))

print(isValidChessBoard(board1))
print(isValidChessBoard(board2))
print(isValidChessBoard(board3))

