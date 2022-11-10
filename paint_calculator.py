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
walls_length_north.delete(0, END)
walls_width_east.delete(0, END)
walls_length_east.delete(0, END)
walls_width_south.delete(0, END)
walls_length_south.delete(0, END)
walls_width_west.delete(0, END)
walls_length_west.delete(0, END)

walls_width_north.get(), 
walls_length_north.get(), 
walls_width_east.get(), walls_length_east.get(),	
walls_width_south.get(), walls_length_south.get(), 
walls_width_west.get(), 
walls_length_west.get(),  # get current stuff inputted
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

e = Entry(root, width=35, borderwidth = 5)

#left walls
#define variables
walls_width_north = Entry(root, width=35, borderwidth = 5)
walls_length_north = Entry(root, width=35, borderwidth = 5)

walls_width_east = Entry(root, width=35, borderwidth = 5)
walls_length_east = Entry(root, width=35, borderwidth = 5)

walls_width_south = Entry(root, width=35, borderwidth = 5)
walls_length_south = Entry(root, width=35, borderwidth = 5)

walls_width_west = Entry(root, width=35, borderwidth = 5)
walls_length_west = Entry(root, width=35, borderwidth = 5)

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
button9 = Button(root, text = "9", padx=40, pady=20, command=lambda: buttonClick(9))

button0 = Button(root, text = "0", padx=138, pady=20, command=lambda: buttonClick(0))
buttonClear = Button(root, text = "Clear",padx=31,pady=20,command= buttonClear)

buttonPlus = Button(root, text = "+", padx=39, pady=52, command= buttonPlus)
buttonEquals = Button(root, text = "=", padx=39, pady=52, command= buttonEqual)

buttonMinus = Button(root, text = "-", padx=39, pady=20, command= buttonMinus)
buttonTimes = Button(root, text = "x", padx=39, pady=20, command= buttonTimes)
buttonDivide = Button(root, text = "÷", padx=39, pady=20, command= buttonDivide)

# put buttons on the screen

e.grid(row = 0, column = 0, columnspan = 5, padx=10, pady=10)

buttonClear.grid(row = 1, column = 0)
buttonDivide.grid(row = 1, column = 1)
buttonTimes.grid(row = 1, column = 2)
buttonMinus.grid(row = 1, column = 3)

buttonPlus.grid(row = 2, column = 3, rowspan = 2)
buttonEquals.grid(row = 4, column = 3, rowspan = 2)

walls_width_north.grid(row = 2, column = 2)
walls_length_north.grid(row = 2, column = 1)

walls_width_east.grid(row = 2, column = 0)
walls_length_east.grid(row = 3, column = 2)

walls_width_south.grid(row = 3, column = 1)
walls_length_south.grid(row = 3, column = 0)

walls_width_west.grid(row = 4, column = 2)
walls_length_west.grid(row = 4, column = 1)

button1.grid(row = 4, column = 0)

button0.grid(row = 5, column = 0, columnspan = 3)


root.mainloop()
