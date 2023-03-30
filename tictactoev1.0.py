#Variables for spaces (1-9)
box1 = '  -  '
box2 = '  -  '
box3 = '  -  '
box4 = '  -  '
box5 = '  -  '
box6 = '  -  '
box7 = '  -  '
box8 = '  -  '
box9 = '  -  '
horizontal = '---------------------------'	#Horizontal lines

#Create the Board
def board():
	print (horizontal)
	print ('||\t |\t |\t ||')
	print ('||', box1, '|', box2, '|', box3, '||')
	print ('||\t |\t |\t ||')
	print (horizontal)
	print ('||\t |\t |\t ||')
	print ('||', box4, '|', box5, '|', box6, '||')
	print ('||\t |\t |\t ||')
	print (horizontal)
	print ('||\t |\t |\t ||')
	print ('||', box7, '|', box8, '|', box9, '||')
	print ('||\t |\t |\t ||')
	print (horizontal)
#Solutions
def solutions():
	if box1 == box2 and box2 == box3 and box1 != '  -  ' and box2 != '  -  ' and box3 != '  -  ':
		print("Winner!")
		win()
		quit()
	if box4 == box5 and box5 == box6 and box4 != '  -  ' and box5 != '  -  ' and box6 != '  -  ':
		print("Winner!")
		win()
		quit()
	if box7 == box8 and box8 == box9 and box7 != '  -  ' and box8 != '  -  ' and box9 != '  -  ':
		print("Winner!")
		win()
		quit()
	if box1 == box4 and box4 == box7 and box1 != '  -  ' and box4 != '  -  ' and box7 != '  -  ':
		print("Winner!")
		win()
		quit()
	if box2 == box5 and box5 == box8 and box2 != '  -  ' and box5 != '  -  ' and box8 != '  -  ':
		print("Winner!")
		win()
		quit()
	if box3 == box6 and box6 == box9 and box3 != '  -  ' and box6 != '  -  ' and box9 != '  -  ':
		print("Winner!")
		win()
		quit()
	if box1 == box5 and box5 == box9 and box1 != '  -  ' and box5 != '  -  ' and box9 != '  -  ':
		print("Winner!")
		win()
		quit()
	if box3 == box5 and box5 == box7 and box3 != '  -  ' and box5 != '  -  ' and box7 != '  -  ':
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
	global box1
	global box2
	global box3
	global box4
	global box5
	global box6
	global box7
	global box8
	global box9
	try:	
		user_box = int(input())
		if user_box == 1 and box1 == '  -  ':
			box1 = '  X  '
			board()
			solutions()
		elif user_box == 1 and box1 != '  -  ':
			player1()
		if user_box == 2 and box2 == '  -  ':
			box2 = '  X  '
			board()
			solutions()
		elif user_box == 2 and box2 != '  -  ':
			player1()
		if user_box == 3 and box3 == '  -  ':
			box3 = '  X  '
			board()
			solutions()
		elif user_box == 3 and box3 != '  -  ':
			player1()
		if user_box == 4 and box4 == '  -  ':
			box4 = '  X  '
			board()
			solutions()
		elif user_box == 4 and box4 != '  -  ':
			player1()
		if user_box == 5 and box5 == '  -  ':
			box5 = '  X  '
			board()
			solutions()
		elif user_box == 5 and box5 != '  -  ':
			player1()
		if user_box == 6 and box6 == '  -  ':
			box6 = '  X  '
			board()
			solutions()
		elif user_box == 6 and box6 != '  -  ':
			player1()
		if user_box == 7 and box7 == '  -  ':
			box7 = '  X  '
			board()
			solutions()
		elif user_box == 7 and box7 != '  -  ':
			player1()
		if user_box == 8 and box8 == '  -  ':
			box8 = '  X  '
			board()
			solutions()
		elif user_box == 8 and box8 != '  -  ':
			player1()
		if user_box == 9 and box9 == '  -  ':
			box9 = '  X  '
			board()
			solutions()
		elif user_box == 9 and box9 != '  -  ':
			player1()
	except ValueError:
		print ("Loose your turn")
#Player 2
def player2():
	print ('\nPlayer 2:\nChoose a box(1-9)')
	global box1
	global box2
	global box3
	global box4
	global box5
	global box6
	global box7
	global box8
	global box9
	try:
		user_box = int(input())
		if user_box == 1 and box1 == '  -  ':
			box1 = '  O  '
			board()
			solutions()
		elif user_box == 1 and box1 != '  -  ':
			player2()
		if user_box == 2 and box2 == '  -  ':
			box2 = '  O  '
			board()
			solutions()
		elif user_box == 2 and box2 != '  -  ':
			player2()
		if user_box == 3 and box3 == '  -  ':
			box3 = '  O  '
			board()
			solutions()
		elif user_box == 3 and box3 != '  -  ':
			player2()
		if user_box == 4 and box4 == '  -  ':
			box4 = '  O  '
			board()
			solutions()
		elif user_box == 4 and box4 != '  -  ':
			player2()
		if user_box == 5 and box5 == '  -  ':
			box5 = '  O  '
			board()
			solutions()
		elif user_box == 5 and box5 != '  -  ':
			player2()
		if user_box == 6 and box6 == '  -  ':
			box6 = '  O  '
			board()
			solutions()
		elif user_box == 6 and box6 != '  -  ':
			player2()
		if user_box == 7 and box7 == '  -  ':
			box7 = '  O  '
			board()
			solutions()
		elif user_box == 7 and box7 != '  -  ':
			player2()
		if user_box == 8 and box8 == '  -  ':
			box8 = '  O  '
			board()
			solutions()
		elif user_box == 8 and box8 != '  -  ':
			player2()
		if user_box == 9 and box9 == '  -  ':
			box9 = '  O  '
			board()
			solutions()
		elif user_box == 9 and box9 != '  -  ':
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