import tkinter as tk
import tkinter.font as font
from tkinter import *
from tkinter.ttk import Label

#Create window (475x465px)
app = tk.Tk()
app.wm_title('Tic-Tac-Toe')
app.geometry("450x465")
app.minsize(450, 465)
app.maxsize(450, 665)
app.configure(bg='#fff')
pixelVirtual = tk.PhotoImage(width=1, height=1)
myFont = font.Font(family='Franklin Gothic', size=100, weight='bold')
p1 = PhotoImage(file = 'icon.png')
app.iconphoto(False, p1)

def changex1():
    global box10
    global turn
    if box10 == empty:
        if (turn % 2) == 0:  
            box1.configure(text='O')
            box10 = 0
        else:  
            box1.configure(text='X')
            box10 = 1
        box1['font'] = myFont
        turn = turn + 1
def changey2():
    global box20
    global turn
    if box20 == empty:
        if (turn % 2) == 0:  
            box2.configure(text='O')
            box20 = 0
        else:  
            box2.configure(text='X')
            box20 = 1
        box2['font'] = myFont
        turn = turn + 1
def changex3():
    global box30
    global turn
    if box30 == empty:
        if (turn % 2) == 0:  
            box3.configure(text='O')
            box30 = 0
        else:  
            box3.configure(text='X')
            box30 = 1
        box3['font'] = myFont
        turn = turn + 1
def changey4():
    global box40
    global turn
    if box40 == empty:
        if (turn % 2) == 0:  
            box4.configure(text='O')
            box40 = 0
        else:  
            box4.configure(text='X')
            box40 = 1
        box4['font'] = myFont
        turn = turn + 1
def changex5():
    global box50
    global turn
    if box50 == empty:
        if (turn % 2) == 0:  
            box5.configure(text='O')
            box50 = 0
        else:  
            box5.configure(text='X')
            box50 = 1
        box5['font'] = myFont
        turn = turn + 1
def changey6():
    global box60
    global turn
    if box60 == empty:
        if (turn % 2) == 0:  
            box6.configure(text='O')
            box60 = 0
        else:  
            box6.configure(text='X')
            box60 = 1
        box6['font'] = myFont
        turn = turn + 1
def changex7():
    global box70
    global turn
    if box70 == empty:
        if (turn % 2) == 0:  
            box7.configure(text='O')
            box70 = 0
        else:  
            box7.configure(text='X')
            box70 = 1
        box7['font'] = myFont
        turn = turn + 1
def changey8():
    global box80
    global turn
    if box80 == empty:
        if (turn % 2) == 0:  
            box8.configure(text='O')
            box80 = 0
        else:  
            box8.configure(text='X')
            box80 = 1
        box8['font'] = myFont
        turn = turn + 1
def changex9():
    global box90
    global turn
    if box90 == empty:
        if (turn % 2) == 0:  
            box9.configure(text='O')
            box90 = 0
        else:  
            box9.configure(text='X')
            box90 = 1
        box9['font'] = myFont
        turn = turn + 1
def solutions():
    app.after(20, solutions)
    if box10 == box20 and box20 == box30 and box10 != empty and box20 != empty and box30 != empty:
        win()
    if box40 == box50 and box50 == box60 and box40 != empty and box50 != empty and box60 != empty:
        win()
    if box70 == box80 and box80 == box90 and box70 != empty and box80 != empty and box90 != empty:
        win()
    if box10 == box40 and box40 == box70 and box10 != empty and box40 != empty and box70 != empty:
        win()
    if box20 == box50 and box50 == box80 and box20 != empty and box50 != empty and box80 != empty:
        win()
    if box30 == box60 and box60 == box90 and box30 != empty and box60 != empty and box90 != empty:
        win()
    if box10 == box50 and box50 == box90 and box10 != empty and box50 != empty and box90 != empty:
        win()
    if box30 == box50 and box50 == box70 and box30 != empty and box50 != empty and box70 != empty:
        win()
def win():
    global turn
    myFont = font.Font(family='Franklin Gothic',
                        size=50,
                        weight='bold')
    app.geometry("450x565")
    winner = 'x'
    if (turn % 2) == 0:  
        winner = 'X'
    else:  
        winner = 'O'
    quit.configure(
        height=150,
        width=450,
        text=winner + " Wins!",
        bg="#d2fcdd",
        border=0,
        font=myFont)

#Create buttons
box1 = tk.Button(app,
                           image=pixelVirtual,
                           width=100,
                           height=100,
                           bg='#fff',
                           borderwidth=0,
                           compound="c",
                           command = changex1)
box2 = tk.Button(app,
                           image=pixelVirtual,
                           width=100,
                           height=100,
                           bg='#fff',
                           borderwidth=0,
                           compound=tk.CENTER,
                           command = changey2)
box3 = tk.Button(app,
                           image=pixelVirtual,
                           width=100,
                           height=100,
                           bg='#fff',
                           borderwidth=0,
                           compound=tk.CENTER,
                           command = changex3)
box4 = tk.Button(app,
                           image=pixelVirtual,
                           width=100,
                           height=100,
                           bg='#fff',
                           borderwidth=0,
                           compound="c",
                           command = changey4)
box5 = tk.Button(app,
                           image=pixelVirtual,
                           width=100,
                           height=100,
                           bg='#fff',
                           borderwidth=0,
                           compound=tk.CENTER,
                           command = changex5)
box6 = tk.Button(app,
                           image=pixelVirtual,
                           width=100,
                           height=100,
                           bg='#fff',
                           borderwidth=0,
                           compound=tk.CENTER,
                           command = changey6)
box7 = tk.Button(app,
                           image=pixelVirtual,
                           width=100,
                           height=100,
                           bg='#fff',
                           borderwidth=0,
                           compound="c",
                           command = changex7)
box8 = tk.Button(app,
                           image=pixelVirtual,
                           width=100,
                           height=100,
                           bg='#fff',
                           borderwidth=0,
                           compound=tk.CENTER,
                           command = changey8)
box9 = tk.Button(app,
                           image=pixelVirtual,
                           width=100,
                           height=100,
                           bg='#fff',
                           borderwidth=0,
                           compound=tk.CENTER,
                           command = changex9)
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
empty = ''
box10 = empty
box20 = empty
box30 = empty
box40 = empty
box50 = empty
box60 = empty
box70 = empty
box80 = empty
box90 = empty
turn = 1

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

solutions()
app.mainloop()