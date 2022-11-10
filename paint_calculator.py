from tkinter import *

root = Tk()
global errInvOp
errInvOp = "Not a valid operator please choose from the buttons provided."
root.title("Paint Calculator") # might not work come back later.

#e.insert(0, "Enter your name") don't need an entry box text
'''
def myClick():
	hello = "Hello " + e.get()
	myLabel = Label(root, text=hello)
	myLabel.pack()
'''
'''
walls_width_north.delete(0, END)
walls_height_north.delete(0, END)
walls_width_east.delete(0, END)
walls_height_east.delete(0, END)
walls_width_south.delete(0, END)
walls_height_south.delete(0, END)
walls_width_west.delete(0, END)
walls_height_west.delete(0, END)

walls_width_north.get(), 
walls_height_north.get(), 
walls_width_east.get(), walls_height_east.get(),	
walls_width_south.get(), walls_height_south.get(), 
walls_width_west.get(), 
walls_height_west.get(),  # get current stuff inputted
'''
def buttonClick(number):
	#e.delete(0, END)
	current = e.get()
	
	

	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def buttonClear():
	e.delete(0, END)

def buttonPlus():
	num1 = e.get()
	global num01
	global math
	math = "plus"
	num01 = int(num1)
	e.delete(0, END)

def buttonEqual():
	num2 = e.get()
	e.delete(0, END)
	if math == "plus":
		e.insert(0, num01 + int(num2))
	elif math == "minus":
		e.insert(0, num01 - int(num2))
	elif math == "times":
		e.insert(0, num01 * int(num2))
	elif math == "divide":
		e.insert(0, num01 / int(num2))
	else:
		return err1InvOp

def buttonMinus():
	num1 = e.get()
	global num01
	global math
	math = "minus"
	num01 = int(num1)
	e.delete(0, END)

def buttonTimes():
	num1 = e.get()
	global num01
	global math
	math = "times"
	num01 = int(num1)
	e.delete(0, END)

def buttonDivide():
	num1 = e.get()
	global num01
	global math
	math = "divide"
	num01 = int(num1)
	e.delete(0, END)


#myButton = Button(root, text = "Submit", command = myClick)

# e define entry box

area_label=Label(root, text="Area of floor(metres)")
e = Entry(root, width=35, borderwidth= 5) #area of floor

paint_req_label= Label(root, text="Paint required (metres)")
paint_req = Entry(root, width=35, borderwidth=5)

vol_room_label= Label(root, text="Total volume of room (metres)")
vol_room = Entry(root, width=35, borderwidth=5)



#left walls
#define variables
north_width_label = Label(root, text="width of north wall")
walls_width_north = Entry(root, width=10, borderwidth = 5)

north_height_label = Label(root, text="height of north wall")
walls_height_north = Entry(root, width=10, borderwidth = 5)

east_width_label = Label(root, text="width of east wall")
walls_width_east = Entry(root, width=10, borderwidth = 5)

east_height_label = Label(root, text="height of east wall")
walls_height_east = Entry(root, width=10, borderwidth = 5)

south_width_label = Label(root, text="width of south wall")
walls_width_south = Entry(root, width=10, borderwidth = 5)

south_height_label = Label(root, text="height of south wall")
walls_height_south = Entry(root, width=10, borderwidth = 5)

west_width_label = Label(root, text="width of west wall")
walls_width_west = Entry(root, width=10, borderwidth = 5)

west_height_label = Label(root, text="height of west wall")
walls_height_west = Entry(root, width=10, borderwidth = 5)

# define entry boxes
#walls_width_north =tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd)

# define buttons

button1 = Button(root, text = "1", padx=40, pady=20, command=lambda: buttonClick(1))
'''
button2 = Button(root, text = "2", padx=40, pady=20, command=lambda: buttonClick(2))
button3 = Button(root, text = "3", padx=40, pady=20, command=lambda: buttonClick(3))

button4 = Button(root, text = "4", padx=40, pady=20, command=lambda: buttonClick(4))
button5 = Button(root, text = "5", padx=40, pady=20, command=lambda: buttonClick(5))
button6 = Button(root, text = "6", padx=40, pady=20, command=lambda: buttonClick(6))

button7 = Button(root, text = "7", padx=40, pady=20, command=lambda: buttonClick(7))
button8 = Button(root, text = "8", padx=40, pady=20, command=lambda: buttonClick(8))
'''
#button9 = Button(root, text = "9", padx=40, pady=20, command=lambda: buttonClick(9))

#button0 = Button(root, text = "0", padx=138, pady=20, command=lambda: buttonClick(0))
buttonClear = Button(root, text = "Clear",padx=31,pady=20,command= buttonClear)

#buttonPlus = Button(root, text = "+", padx=39, pady=52, command= buttonPlus)
#buttonEquals = Button(root, text = "=", padx=39, pady=52, command= buttonEqual)

#buttonMinus = Button(root, text = "-", padx=39, pady=20, command= buttonMinus)
#buttonTimes = Button(root, text = "x", padx=39, pady=20, command= buttonTimes)
#buttonDivide = Button(root, text = "÷", padx=39, pady=20, command= buttonDivide)

# put buttons on the screen

area_label.grid(row=0, column=0)
e.grid(row = 0, column = 1, columnspan = 5, padx=10, pady=10) #area of floor

paint_req_label.grid(row=1, column=0)
paint_req.grid(row = 1, column = 1, columnspan = 5, padx=10, pady=10)

vol_room_label.grid(row=2, column=0)
vol_room.grid(row = 2, column = 1, columnspan = 5, padx=10, pady=10)
#height*width*depth
#buttonClear.grid(row = 1, column = 1)
'''
buttonDivide.grid(row = 1, column = 2)
buttonTimes.grid(row = 1, column = 3)
buttonMinus.grid(row = 1, column = 4)

buttonPlus.grid(row = 2, column = 4, rowspan = 2)
buttonEquals.grid(row = 4, column = 4, rowspan = 2)
'''
north_width_label.grid(row= 3, column= 0)
walls_width_north.grid(row = 3, column = 1)

north_height_label.grid(row= 4,column= 0)
walls_height_north.grid(row= 4, column= 1)

east_width_label.grid(row= 3, column = 2)
walls_width_east.grid(row= 3, column = 3)

east_height_label.grid(row= 4, column= 2)
walls_height_east.grid(row= 4, column= 3)

south_width_label.grid(row= 5, column= 0)
walls_width_south.grid(row= 5, column= 1)

south_height_label.grid(row= 6, column= 0)
walls_height_south.grid(row= 6, column = 1)

west_width_label.grid(row= 5, column= 2)
walls_width_west.grid(row= 5, column= 3)

west_height_label.grid(row= 6, column= 2)
walls_height_west.grid(row= 6, column= 3)

#button1.grid(row = 4, column = 1)

#button0.grid(row = 5, column = 1, columnspan = 3)









root.mainloop()
