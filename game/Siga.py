
from random import choice as randomChoice


def help():
	print('''the game: Siga

in which two players place three pieces on a 3x3 grids and moveDest a piece at a time.

the goal is to get your three pieces in a row

you're allowed to moveDest to the square next to you or the square after it, Horizontally, Vertically, or Diagonally. But you're not allowed to jump over the other player's piece.''')


def initialize():

	P1 = '^'
	P2 = 'v'
	comp = 'v'

	Board = {
		1:"v" , 2:"v" , 3:"v" ,
		4:" " , 5:" " , 6:" " ,
		7:"^" , 8:"^" , 9:"^" ,
	}
	
	# will make the player able to choose their symbol later.

	Y = ['Y', 'y', 'yes', 'Yes', 'YES']
	N = ['N', 'n', 'no', 'No', 'NO']

	while True:

		multi = input('Multiplayer? [Y/N]:  ')

		if multi in Y:
			multi = True
			break

		elif multi in N:
			multi = False
			break

		else:
			print('this isn\'t a correct choice!')
			continue

	while True:

		P1First = input('P1, wanna go first? [Y/N]:  ')

		if P1First in Y:
			P1First = True
			break

		elif P1First in N:
			P1First = False
			break

		else:
			print('this isn\'t a correct choice!')
			continue


	return {
		'Board':Board,
		'Multiplayer':multi,
		'P1First':P1First,
		'P1':P1,
		'P2':P2,
		'Computer':comp
		}


def showBoard(Board):

	print(
		'\n [1] | [2] | [3]\n  {}  |  {}  |  {} \n-----------------\n [4] | [5] | [6]\n  {}  |  {}  |  {} \n-----------------\n [7] | [8] | [9]\n  {}  |  {}  |  {} \n'.format(*Board.values())
		)


def playermoved(Board,currentPMark,otherPMark):

	corners1 = {1,9}
	corners2 = {3,7}

	# error dict
	# error action dict
	# for error in error dict:
	# if errordict[error]: 
	# 	exec(erroractiondict[error]) and return False 

	while True:

		moveOrigin = int(input('Choose a square where you have one of your pieces:  '))
		moveDest = int(input('Choose a square where you want it to go:  '))
		moveSpace = moveDest - moveOrigin

		cornerJumps = {moveOrigin,moveDest} == corners1 or {moveOrigin,moveDest} == corners2
		normalJumps = (abs(moveSpace) == 6 or abs(moveSpace) == 2) and moveOrigin != 5
		ambitious = abs(moveSpace) == 7 or abs(moveSpace) == 5

		if (moveOrigin not in Board) or (moveDest not in Board):

			print('you chose something that isn\'t on the Board to begin with.')
			continue

		elif Board[moveOrigin] != currentPMark:

			print('please choose one of your pieces')
			continue

		elif Board[moveDest] != " ":

			print('you can\'t move there!')
			continue

		elif ambitious:

			print('can\'t move this far!')
			continue

		elif (normalJumps or cornerJumps) and Board[(moveDest + moveOrigin)/2] == otherPMark:

			print('can\'t jump over the other player\'s piece!')
			continue

		else:
			Board[moveDest] = currentPMark
			Board[moveOrigin] = " "
			break

	del(corners1,corners2)
	return moveOrigin


def compumoved(Board,currentPMark,otherPMark):

	moveOrigins = []
	moveDests = []

	for square in Board:
		if Board[square] == ' ':
			moveDests.append(square)
		elif Board[square] == currentPMark:
			moveOrigins.append(square)
		else:
			pass

	corners1 = {1,9}
	corners2 = {3,7}

	while True:
	
		moveOrigin = randomChoice(moveOrigins)
		moveDest = randomChoice(moveDests)
		moveSpace = moveDest - moveOrigin

		cornerJumps = {moveOrigin,moveDest} == corners1 or {moveOrigin,moveDest} == corners2
		normalJumps = (abs(moveSpace) == 6 or abs(moveSpace) == 2) and moveOrigin != 5
		ambitious = abs(moveSpace) == 7 or abs(moveSpace) == 5

		if ambitious:
			continue

		elif (normalJumps or cornerJumps) and Board[(moveDest + moveOrigin)/2] == otherPMark:
			continue

		else:
			Board[moveDest] = currentPMark
			Board[moveOrigin] = " "
			break

	del(corners1,corners2)
	return moveOrigin


def wincheck(Board,player,allmoved=False):

	win = [{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7}]
	
	P = set()

	for square in Board:
		if Board[square] == player:
			P.add(square)

	if allmoved:

		if P in win:
			return True

	else:
		return False
		

def runGame():

	help()
	print()
	print()

	info = initialize()
	Board = info['Board']
	Y = ['Y', 'y', 'yes', 'Yes', 'YES']

	while True:
		
		if info['Multiplayer']:

			P1 = info['P1']
			P2 = info['P2']
			P1moved = {7:False,8:False,9:False}
			P2moved = {1:False,2:False,3:False}

			print()
			print('P1\'s piece is "^"')
			print('P2\'s is "v"')

			if info['P1First']:

				while True:

					print('P1\'s Turn:')
					showBoard(Board)
					P1moved[playermoved(Board,P1,P2)] = True
					
					if wincheck(Board,P1,all(P1moved.values())):
						showBoard(Board)
						print('P1 Won!')
						break
					
					print('P2\'s Turn:')
					showBoard(Board)
					P2moved[playermoved(Board,P2,P1)] = True
					
					if wincheck(Board,P2,all(P2moved.values())):
						showBoard(Board)
						print('P2 Won!')
						break
			
			elif not info['P1First']:

				while True:

					print('P2\'s Turn:')
					showBoard(Board)
					P2moved[playermoved(Board,P2,P1)] = True
					
					if wincheck(Board,P2,all(P2moved.values())):
						showBoard(Board)
						print('P2 Won!')
						break
					
					print('P1\'s Turn:')
					showBoard(Board)
					P1moved[playermoved(Board,P1,P2)] = True
					
					if wincheck(Board,P1,all(P1moved.values())):
						showBoard(Board)
						print('P1 Won!')
						break


		elif not info['Multiplayer']:

			P1 = info['P1']
			P2 = info['Computer']
			P1moved = {7:False,8:False,9:False}
			P2moved = {1:False,2:False,3:False}

			print()
			print('Computer\'s piece is "v"')

			if info['P1First']:

				while True:
					
					showBoard(Board)
					P1moved[playermoved(Board,P1,P2)] = True
					
					if wincheck(Board,P1,all(P1moved.values())):
						showBoard(Board)
						print('P1 Won!')
						break

					P2moved[compumoved(Board,P2,P1)] = True
					
					if wincheck(Board,P2,all(P2moved.values())):
						showBoard(Board)
						print('You lost to Ultron!')
						break
			
			elif not info['P1First']:

				while True:

					P2moved[compumoved(Board,P2,P1)] = True
					
					if wincheck(Board,P2,all(P2moved.values())):
						showBoard(Board)
						print('You lost to Ultron!')
						break
					
					showBoard(Board)
					P1moved[playermoved(Board,P1,P2)] = True
					
					if wincheck(Board,P1,all(P1moved.values())):
						showBoard(Board)
						print('P1 Won!')
						break


		again = input('Wanna play again? [Y/anykey]:  ')
		
		if again in Y:
			print()
			print('Alright! Another round!')
			continue
		else:
			print()
			print('Hope you enjoyed!')
			break



