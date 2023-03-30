#Board variables
side = '||'
middle = '|'
empty = '       '
emptym = '   -   '
horizontal = '---------------------------'
#X
x1 = '  \\ /  '
x2 = '   X   '
x3 = '  / \\  '
#O
o1 = '  /\u203e\\  '
o2 = ' (   ) '
o3 = '  \\_/  '
#Box1
box10 = empty
box11 = emptym
box12 = empty
#Box2
box20 = empty
box21 = emptym
box22 = empty
#Box3
box30 = empty
box31 = emptym
box32 = empty
#Box4
box40 = empty
box41 = emptym
box42 = empty
#Box5
box50 = empty
box51 = emptym
box52 = empty
#Box6
box60 = empty
box61 = emptym
box62 = empty
#Box7
box70 = empty
box71 = emptym
box72 = empty
#Box8
box80 = empty
box81 = emptym
box82 = empty
#Box9
box90 = empty
box91 = emptym
box92 = empty


#Create the Board
def board():
	print (horizontal)
	print (side + box10 + middle + box20 + middle + box30 + side)
	print (side + box11 + middle + box21 + middle + box31 + side)
	print (side + box12 + middle + box22 + middle + box32 + side)
	print (horizontal)
	print (side + box40 + middle + box50 + middle + box60 + side)
	print (side + box41 + middle + box51 + middle + box61 + side)
	print (side + box42 + middle + box52 + middle + box62 + side)
	print (horizontal)
	print (side + box70 + middle + box80 + middle + box90 + side)
	print (side + box71 + middle + box81 + middle + box91 + side)
	print (side + box72 + middle + box82 + middle + box92 + side)
	print (horizontal)
#Solutions
def solutions():
	if box10 == box20 and box20 == box30 and box10 != empty and box20 != empty and box30 != empty:
		print("Winner!")
		win()
		quit()
	if box40 == box50 and box50 == box60 and box40 != empty and box50 != empty and box60 != empty:
		print("Winner!")
		win()
		quit()
	if box70 == box80 and box80 == box90 and box70 != empty and box80 != empty and box90 != empty:
		print("Winner!")
		win()
		quit()
	if box10 == box40 and box40 == box70 and box10 != empty and box40 != empty and box70 != empty:
		print("Winner!")
		win()
		quit()
	if box20 == box50 and box50 == box80 and box20 != empty and box50 != empty and box80 != empty:
		print("Winner!")
		win()
		quit()
	if box30 == box60 and box60 == box90 and box30 != empty and box60 != empty and box90 != empty:
		print("Winner!")
		win()
		quit()
	if box10 == box50 and box50 == box90 and box10 != empty and box50 != empty and box90 != empty:
		print("Winner!")
		win()
		quit()
	if box30 == box50 and box50 == box70 and box30 != empty and box50 != empty and box70 != empty:
		print("Winner!")
		win()
		quit()
#Winning picture
def win():
	#Thumbs up
	print ("★░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░★\n★░░░░░░░░░███░██░░░░░░░░░░░░░░░░░░░░★\n★░░░░░░░░░██░░░█░░░░░░░░░░░░░░░░░░░░★\n★░░░░░░░░░██░░░██░░░░░░░░░░░░░░░░░░░★\n★░░░░░░░░░░██░░░███░░░░░░░░░░░░░░░░░★\n★░░░░░░░░░░░██░░░░██░░░░░░░░░░░░░░░░★\n★░░░░░░░░░░░██░░░░░███░░░░░░░░░░░░░░★\n★░░░░░░░░░░░░██░░░░░░██░░░░░░░░░░░░░★\n★░░░░░░░███████░░░░░░░██░░░░░░░░░░░░★\n★░░░░█████░░░░░░░░░░░░░░███░██░░░░░░★\n★░░░██░░░░░████░░░░░░░░░░██████░░░░░★\n★░░░██░░████░░███░░░░░░░░░░░░░██░░░░★\n★░░░██░░░░░░░░███░░░░░░░░░░░░░██░░░░★\n★░░░░██████████░███░░░░░░░░░░░██░░░░★\n★░░░░██░░░░░░░░████░░░░░░░░░░░██░░░░★\n★░░░░███████████░░██░░░░░░░░░░██░░░░★\n★░░░░░░██░░░░░░░████░░░░░██████░░░░░★\n★░░░░░░██████████░██░░░░███░██░░░░░░★\n★░░░░░░░░░██░░░░░████░███░░░░░░░░░░░★\n★░░░░░░░░░█████████████░░░░░░░░░░░░░★\n★░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░★")
#Draw picture
def draw():
	#Thumbs down
	print ("░░░░░░░░░░░█████████████\n░░░░░░░░░███░███░░░░░░██\n███░░░░░██░░░░██░██████████\n████████░░░░░░████░░░░░░░██\n████░░░░░░░░░░██░░██████████\n████░░░░░░░░░░░███░░░░░░░░░██\n████░░░░░░░░░░░██░░██████████\n████░░░░░░░░░░░░████░░░░░░░░█\n████░░░░░░░░░░░░░███░░████░░█\n█████████░░░░░░░░░░████░░░░░█\n███░░░░░██░░░░░░░░░░░░░█████\n░░░░░░░░░███░░░░░░░██████\n░░░░░░░░░░░██░░░░░░██\n░░░░░░░░░░░░███░░░░░██\n░░░░░░░░░░░░░░██░░░░██\n░░░░░░░░░░░░░░░███░░░██\n░░░░░░░░░░░░░░░░░██░░░█\n░░░░░░░░░░░░░░░░░░█░░░█\n░░░░░░░░░░░░░░░░░░██░██\n░░░░░░░░░░░░░░░░░░░███")
#Player 1
def player1():
	print ('\nPlayer 1:\nChoose a box(1-9)')
	global box10
	global box11
	global box12
	global box20
	global box21
	global box22
	global box30
	global box31
	global box32
	global box40
	global box41
	global box42
	global box50
	global box51
	global box52
	global box60
	global box61
	global box62
	global box70
	global box71
	global box72
	global box80
	global box81
	global box82
	global box90
	global box91
	global box92
	try:	
		user_box = int(input())
		if user_box == 1 and box10 == empty:
			box10 = x1
			box11 = x2
			box12 = x3
			board()
			solutions()
		elif user_box == 1 and box10 != empty:
			player1()
		if user_box == 2 and box20 == empty:
			box20 = x1
			box21 = x2
			box22 = x3
			board()
			solutions()
		elif user_box == 2 and box20 != empty:
			player1()
		if user_box == 3 and box30 == empty:
			box30 = x1
			box31 = x2
			box32 = x3
			board()
			solutions()
		elif user_box == 3 and box30 != empty:
			player1()
		if user_box == 4 and box40 == empty:
			box40 = x1
			box41 = x2
			box42 = x3
			board()
			solutions()
		elif user_box == 4 and box40 != empty:
			player1()
		if user_box == 5 and box50 == empty:
			box50 = x1
			box51 = x2
			box52 = x3
			board()
			solutions()
		elif user_box == 5 and box50 != empty:
			player1()
		if user_box == 6 and box60 == empty:
			box60 = x1
			box61 = x2
			box62 = x3
			board()
			solutions()
		elif user_box == 6 and box60 != empty:
			player1()
		if user_box == 7 and box70 == empty:
			box70 = x1
			box71 = x2
			box72 = x3
			board()
			solutions()
		elif user_box == 7 and box70 != empty:
			player1()
		if user_box == 8 and box80 == empty:
			box80 = x1
			box81 = x2
			box82 = x3
			board()
			solutions()
		elif user_box == 8 and box80 != empty:
			player1()
		if user_box == 9 and box90 == empty:
			box90 = x1
			box91 = x2
			box92 = x3			
			board()
			solutions()
		elif user_box == 9 and box90 != empty:
			player1()
	except ValueError:
		print ("Loose your turn")
#Player 2
def player2():
	print ('\nPlayer 2:\nChoose a box(1-9)')
	global box10
	global box11
	global box12
	global box20
	global box21
	global box22
	global box30
	global box31
	global box32
	global box40
	global box41
	global box42
	global box50
	global box51
	global box52
	global box60
	global box61
	global box62
	global box70
	global box71
	global box72
	global box80
	global box81
	global box82
	global box90
	global box91
	global box92
	try:
		user_box = int(input())
		if user_box == 1 and box10 == empty:
			box10 = o1
			box11 = o2
			box12 = o3
			board()
			solutions()
		elif user_box == 1 and box10 != empty:
			player2()
		if user_box == 2 and box20 == empty:
			box20 = o1
			box21 = o2
			box22 = o3
			board()
			solutions()
		elif user_box == 2 and box20 != empty:
			player2()
		if user_box == 3 and box30 == empty:
			box30 = o1
			box31 = o2
			box32 = o3
			board()
			solutions()
		elif user_box == 3 and box30 != empty:
			player2()
		if user_box == 4 and box40 == empty:
			box40 = o1
			box41 = o2
			box42 = o3
			board()
			solutions()
		elif user_box == 4 and box40 != empty:
			player2()
		if user_box == 5 and box50 == empty:
			box50 = o1
			box51 = o2
			box52 = o3
			board()
			solutions()
		elif user_box == 5 and box50 != empty:
			player2()
		if user_box == 6 and box60 == empty:
			box60 = o1
			box61 = o2
			box62 = o3
			board()
			solutions()
		elif user_box == 6 and box60 != empty:
			player2()
		if user_box == 7 and box70 == empty:
			box70 = o1
			box71 = o2
			box72 = o3
			board()
			solutions()
		elif user_box == 7 and box70 != empty:
			player2()
		if user_box == 8 and box80 == empty:
			box80 = o1
			box81 = o2
			box82 = o3
			board()
			solutions()
		elif user_box == 8 and box80 != empty:
			player2()
		if user_box == 9 and box90 == empty:
			box90 = o1
			box91 = o2
			box92 = o3			
			board()
			solutions()
		elif user_box == 9 and box90 != empty:
			player2()
	except ValueError :
		print ("Loose your turn")

#Run the game, only 9 turns available
board()
player1()
player2()
player1()
player2()
player1()
player2()
player1()
player2()
player1()
print ("Draw :(")
draw()