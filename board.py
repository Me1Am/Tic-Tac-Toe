#Testing the appearance and inner-workings of the tictactoe boards
import tkinter as tk
import tkinter.font as font
from tkinter import *
from tkinter import ttk

#Board v1
def boardv1():
	box1 = '  -  '
	box2 = '  -  '
	box3 = '  -  '
	box4 = '  X  '
	box5 = '  -  '
	box6 = '  O  '
	box7 = '  -  '
	box8 = '  -  '
	box9 = '  -  '
	horizontal = '---------------------------'
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
#Board v2
def boardv2():
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
	#Boxes
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
	box40 = x1
	box41 = x2
	box42 = x3
	#Box5
	box50 = empty
	box51 = emptym
	box52 = empty
	#Box6
	box60 = o1
	box61 = o2
	box62 = o3
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

	#Board
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
#Board v3
def boardv3():
	empty = '       '
	emptym = '   -   '
	#X
	x1 = '  \\ /  '
	x2 = '   X   '
	x3 = '  / \\  '
	#O
	o1 = '  /\u203e\\  '
	o2 = ' (   ) '
	o3 = '  \\_/  '
	horizontal = '-------+-------+--------'
	board = {'box11': empty, 'box12': emptym, 'box13': empty,
			'box21': empty, 'box22': emptym, 'box23': empty,
			'box31': empty, 'box32': emptym, 'box33': empty,
            'box41': x1, 'box42': x2, 'box43': x3,
            'box51': empty, 'box52': emptym, 'box53': empty,
            'box61': o1, 'box62': o2, 'box63': o3,
            'box71': empty, 'box72': emptym, 'box73': empty,
            'box81': empty, 'box82': emptym, 'box83': empty,
            'box91': empty, 'box92': emptym, 'box93': empty}

	print(board['box11'] + '|' + board['box21'] + '|' + board['box31'])
	print(board['box12'] + '|' + board['box22'] + '|' + board['box32'])
	print(board['box13'] + '|' + board['box23'] + '|' + board['box33'])
	print(horizontal)
	print(board['box41'] + '|' + board['box51'] + '|' + board['box61'])
	print(board['box42'] + '|' + board['box52'] + '|' + board['box62'])
	print(board['box43'] + '|' + board['box53'] + '|' + board['box63'])
	print(horizontal)
	print(board['box71'] + '|' + board['box81'] + '|' + board['box91'])
	print(board['box72'] + '|' + board['box82'] + '|' + board['box92'])
	print(board['box73'] + '|' + board['box83'] + '|' + board['box93'])
#Board v4
def boardv4():
	app = tk.Tk()
	app.wm_title('Tic-Tac-Toe')
	app.geometry("450x465")
	app.minsize(450, 465)
	app.maxsize(450, 565)
	app.resizable(False, False)
	app.configure(bg='#fff')
	pixelVirtual = tk.PhotoImage(width=1, height=1)
	myFont = font.Font(family='Franklin Gothic', size=100, weight='bold')
	p1 = PhotoImage(file = 'icon.png')
	app.iconphoto(False, p1)

	box1 = tk.Button(app,
	       image=pixelVirtual,
	       width=100,
	       height=100,
	       bg='#fff',
	       borderwidth=0,
	       compound="c")
	box2 = tk.Button(app,
	        image=pixelVirtual,
	        width=100,
	        height=100,
	        bg='#fff',
	        borderwidth=0,
	        compound=tk.CENTER)
	box3 = tk.Button(app,
	        image=pixelVirtual,
	        width=100,
	        height=100,
	        bg='#fff',
	        borderwidth=0,
	        compound=tk.CENTER)
	box4 = tk.Button(app,
	        image=pixelVirtual,
	        width=100,
	        height=100,
	        bg='#fff',
	        borderwidth=0,
	        compound="c",)
	box5 = tk.Button(app,
	        image=pixelVirtual,
	        width=100,
	        height=100,
	        bg='#fff',
	        borderwidth=0,
	        compound=tk.CENTER)
	box6 = tk.Button(app,
	        image=pixelVirtual,
	        width=100,
	        height=100,
	        bg='#fff',
	        borderwidth=0,
	        compound=tk.CENTER)
	box7 = tk.Button(app,
	        image=pixelVirtual,
	        width=100,
	        height=100,
	        bg='#fff',
	        borderwidth=0,
	        compound="c")
	box8 = tk.Button(app,
	        image=pixelVirtual,
	        width=100,
	        height=100,
	        bg='#fff',
	        borderwidth=0,
	        compound=tk.CENTER)
	box9 = tk.Button(app,
	        image=pixelVirtual,
	        width=100,
	        height=100,
	        bg='#fff',
	        borderwidth=0,
	        compound=tk.CENTER)
	bar1 = tk.Canvas(app,
	        height=385,
	        width=10,
	        bg="#000"
	        )
	bar2 = tk.Canvas(app,
	        height=385,
	        width=10,
	        bg="#000"
	        )
	bar3 = tk.Canvas(app,
	        height=10,
	        width=385,
	        bg="#000"
	        )
	bar4 = tk.Canvas(app,
	        height=10,
	        width=385,
	        bg="#000"
	        )
	quit = tk.Button(app,
	        text="Quit",
	        image=pixelVirtual,
	        width=50,
	        height=25,
	        bg='#f05348',
	        compound=tk.CENTER,
	        command = app.destroy)
	play = tk.Button(app,
	        text="Play Again",
	        image=pixelVirtual,
	        width=50,
	        height=25,
	        bg='#d2fcdd',
	        compound=tk.CENTER)

	box4.configure(text='X')
	box4['font'] = myFont
	box6.configure(text='O')
	box6['font'] = myFont


	#Button placement(board)
	box1.place(x=50, y=50)
	box2.place(x=166, y=50)
	box3.place(x=280, y=50)
	box4.place(x=50, y=168)
	box5.place(x=166, y=168)
	box6.place(x=280, y=168)
	box7.place(x=50, y=284)
	box8.place(x=166, y=284)
	box9.place(x=280, y=284)
	bar1.place(x=155, y=25)
	bar2.place(x=271, y=25)
	bar3.place(x=25, y=155)
	bar4.place(x=25, y=271)
	quit.pack(side=tk.BOTTOM)
	play.place(x=295, y=732)

	app.mainloop()
#Print the boards
print ("board v1")
boardv1()
print ("board v2")
boardv2()
print ("board v3")
boardv3()
boardv4()